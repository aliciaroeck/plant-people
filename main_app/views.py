from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# models
from .models import Profile, Post
# forms
from .forms import Create_Profile_Form, EditProfileForm, ImageForm, NewContentPostForm
# Create your views here.


# Home/login Route
def landing(request):
    form = Create_Profile_Form()
    error_message = ''
    if request.method == 'POST':
        form = Create_Profile_Form(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(email = request.POST['email'], location = request.POST['location'], full_name= request.POST['full_name'], user = user)
            login(request,user)
            return redirect('community')
        else:
            error_message = 'Invalid form'

    context = {'form':form, 'error_message': error_message}
    return render(request, 'landing.html', context)

# Login Route
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('profile')
    else:
        return render(request,'landing.html',{'error':'Invalid Username or Password'})


# Community Posts Route
def community(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'community/index.html', {'page_obj': page_obj})



def listing(request):
    contact_list = Contact.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list.html', {'page_obj': page_obj})




# Personal Profile Route
def profile(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('/profile')
        else:
            print(form.errors)
    else:
        posts = Post.objects.all().filter(user=request.user.profile.id)
    context = {'posts': posts, 'edit_profile_form': EditProfileForm(initial={'full_name':request.user.profile.full_name, 'location':request.user.profile.location, 'bio':request.user.profile.bio}), 'view_user': request.user, 'image_form': ImageForm()}
    return render(request, 'registration/profile.html', context)

# Edit Profile 
def edit_profile(request):
    user = request.user.profile
    form = EditProfileForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        user.full_name = request.POST.get('full_name')
        user.location = request.POST.get('location')
        user.bio = request.POST.get('bio')
        user.save()
        return redirect('profile')

# Create Post
def create_post(request):
    form = NewContentPostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.profile = request.user.profile
        post.save()
    return redirect(f'/community/{post.id}')
