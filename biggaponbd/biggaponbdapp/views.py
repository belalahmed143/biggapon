from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import Userpost,TopAdd,Caro,HonerProfile,Category,Contuct
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm,UserUpdateform,ProfileUpdateForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  CreateView,UpdateView,DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


# Create your views here.
def home(request):
    topadds =TopAdd.objects.all()
    caros = Caro.objects.all()
    post =HonerProfile.objects.all()
    category =Category.objects.all()
    userposts =Userpost.objects.all().order_by('-id')

    context={
        'topadds':topadds,
        'caros':caros,
        'post':post,
        'userposts':userposts,
        'category':category,
    }
    if request.method == 'POST':
        name =request.POST['name']
        email =request.POST['email']
        phone =request.POST['phone']
        message =request.POST['message']
        sumbit=Contuct(name=name, email=email, phone=phone, message=message)
        sumbit.save()
    return render( request,"home.html",context)


def toletCategory (request, name):
    category =Category.objects.all()
    cat=get_object_or_404(Category,category_name=name)
    userposts =Userpost.objects.filter(category=cat.id)
    return render(request,'category.html',{'userposts':userposts, 'cat':cat, 'category':category,})


class PostDetailView(DetailView):
    model =Userpost

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        category =Category.objects.all()      
        context['category'] = category
        return context

class PostCreateView(CreateView,UserPassesTestMixin):
    model = Userpost
    fields =['img','title','location','mobile_number','details','category','tolet_category']
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        category =Category.objects.all()      
        context['category'] = category
        return context

class PostUpdateView(UpdateView,LoginRequiredMixin,UserPassesTestMixin):
    model = Userpost
    fields =['img','title','location','mobile_number','details','category','tolet_category']
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.author= self.request.user
        return super(PostUpdateView, self).form_valid(form)
    
    def test_func(self):
        userpost = self.get_object()
        if self.request.user == userpost.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        category =Category.objects.all()      
        context['category'] = category
        return context

class PostDeleteView(DeleteView,LoginRequiredMixin,UserPassesTestMixin):
    model = Userpost
    template_name ='delete.html'
    success_url ='/'

    def test_func(self):
        post = self.get_objects()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category =Category.objects.all()
        context['category'] = category
        return context
        
def register(request):
    category =Category.objects.all()
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')      
            messages.success(request,f'Account created for {username}! You are now able to login')
            return redirect('login')
    else:
        form =UserRegistrationForm()
    return render(request, 'register.html',{'form':form,'category':category })


def searchposts(request):
    category =Category.objects.all()
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')
        
        if query is not None:
            lookups= Q(title__icontains=query) |Q(location__icontains=query)
            userposts= Userpost.objects.filter(lookups).distinct()

            context ={
                'userposts':userposts,
                'submitbutton':submitbutton,
                'category':category
            }
            return render(request,'search.html', context)
        else:
            return render(request, 'search.html')
    else:
        return render(request, 'search.html')

@login_required
def profile(request):
    category =Category.objects.all()
    userposts =Userpost.objects.all()
    context = {
        'category':category,
        'userposts':userposts
    }
    return render(request, 'profile.html',context)


@login_required
def up_profile(request):
    category =Category.objects.all()
    if request.method =='POST':
        u_form =UserUpdateform(request.POST, instance=request.user)
        p_form =ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Yor account has been update')
            return redirect('profile')
    else:
        u_form =UserUpdateform(instance=request.user)
        p_form =ProfileUpdateForm(instance=request.user.profile)
   
    context ={
        'u_form':u_form,
        'p_form':p_form,
        'category':category
    }
    return render(request, 'up_profile.html',context)

