from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post, Contact, BlogComment

from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login as dj_login, logout
from datetime import datetime
from django.utils.text import slugify

def blog(request):
    posts = Post.objects.all()
    params = {"posts" : posts}
    return render(request,"blog/blogs.html",params)

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.info(request, "Please fill the form correctly")
            
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.info(request, "Your query/suggestion has been successfully sent")
            
    return render(request, "blog/contact.html")

def blogpost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    #context = {"post":post}
    comments = BlogComment.objects.filter(post=post)
    context = {"post":post, "comments" : comments, "user" : request.user}
    return render(request, "blog/blogPost.html", context)
    
def home(request):
    return render(request,"blog/home.html")

def signup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['name']
        email=request.POST['email']
        pass1=request.POST['password']
        pass2=request.POST['re-password']

        # check for errorneous input
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        #myuser.first_name= fname
        #myuser.last_name= lname
        myuser.save()
        messages.success(request, "Your iCoder has been successfully created")
        return redirect("blogHome")
    return render(request, "blog/signup.html")

    
def login(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user = authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            dj_login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("blogHome")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("blogHome")
    return render(request, "blog/login.html")

def logOut(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('blogHome')

def addBlog(request):
    if request.method=="POST":
        title=request.POST['title']
        author= request.user
        timeStamp= datetime.now()
        content=request.POST['desc']
        thumbnail = request.POST['img']
        slug= slugify(title)

        newPost = Post(title=request.POST['title'],author= request.user,timeStamp= datetime.now(), content=request.POST['desc'], thumbnail = request.POST['img'],slug= slugify(title))
        newPost.save()
    return render(request, "blog/blogtemplate.html")

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        comment=BlogComment(comment= comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
        
    return redirect(f"/{post.slug}")

    #messages.success(request, "Your comment has been posted successfully")









