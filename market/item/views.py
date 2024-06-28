from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db.models import Q
from .models import *
from .forms import *

def validate_text(category_name):
    category_name=category_name.lower()
    exist_cat = Category.objects.all()
    for catt in exist_cat:
        if catt.name.lower()==category_name:
            raise ValidationError('Category Already Exists!')
            return redirect('dashboard:index')

def browse(request):
    query = request.GET.get('query','')
    category_id = request.GET.get('category',0)
    items = Item.objects.filter(is_sold=False)
    categories =  Category.objects.all()
    
    if query:
        items = items.filter(Q(name__icontains=query) |  Q(description__icontains=query))
    if category_id:
        items = items.filter(cat_id=category_id)
    return render(request, 'item/browse.html',{
        'items':items,
        'query':query, 
        'categories':categories,
        'category_id':int(category_id),
        } )

def detail(request,pk):
    item = get_object_or_404(Item,pk=pk)
    related_items = Item.objects.filter(cat=item.cat,is_sold=False).exclude(pk=pk)[0:3] 
    return render(request,'item/detail.html',{'item':item,'related_items':related_items})

@login_required
def new(request):
    if(request.method=='POST'):
        form = NewItemForm(request.POST,request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('item:detail',pk=item.id)

    else:    
        form = NewItemForm()


        return render(request,'item/form.html',{'form':form,'title':'New Item'})


@login_required
def newcat(request):
    if(request.method=='POST'):
        form = NewCatForm(request.POST)
        if form.is_valid():
            form.save()
            #cattemp = form.save(commit=False)
            #cattemp.save()
            return redirect('dashboard:index')
        else:
            #form=NewCatForm()
            return render(request,'item/newcat.html',{'form':form,'title':'Add New Category'})
    else:
        form = NewCatForm()
        return render(request,'item/newcat.html',{'form':form,'title':'Add New Category'})
            
            




@login_required
def delete(request,pk):
    item =get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()
  
    return redirect('dashboard:index')

@login_required
def edit(request,pk):
    item =get_object_or_404(Item,pk=pk,created_by=request.user)
    if(request.method=='POST'):
        
        form = EditItemForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail',pk=item.id)

    else:    
        form = EditItemForm(instance=item)


        return render(request,'item/form.html',{'form':form,'title':'Edit Item'})
    

