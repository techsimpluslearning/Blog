from django.shortcuts import render,redirect

# Create your views here.
from .models import *
from django.contrib.auth import authenticate,login,logout

def Home(request):
    blogs = BlogModel.objects.all()
    d = {"blogs": blogs}
    return render(request,'allblog.html',d)

def Blogdetail(request,bid):
    data = BlogModel.objects.get(id = bid)
    comments = UserComment.objects.filter(blog = data)
    author = request.user
    status = False
    if request.user.is_authenticated:
        LikeDisLike = LikeBlog.objects.filter(blog=data, author=author)
        if LikeDisLike:
            status = True
    d = {"detail":data,"comments":comments, "status":status}
    return render(request,'blog_detail.html',d)

def LoginForm(request):
    error = False
    if request.method == "POST":
        dic = request.POST
        u = dic['user']
        p = dic['pwd']
        user = authenticate(username = u,password = p)
        if user:
            login(request,user)
            return redirect('blogs')
        else:
            error = True

    dic = {"error": error}
    return render(request,'login.html',dic)

def Signup(request):
    error = False
    if request.method == "POST":
        d = request.POST
        first = d['fname']
        last = d['lname']
        em = d['email']
        u = d['uname']
        p = d['pwd']
        user = User.objects.filter(username = u)
        if user:
            error = True
        else:
            User.objects.create_user(username=u,password=p,
                                     email=em,first_name = first,
                                     last_name = last)
            return redirect('login')


    dic = {"error":error}
    return render(request,'signup.html',dic)

def AuthorPanel(request):
    if not request.user.is_authenticated:
        return redirect('login')
    author_blogs = BlogModel.objects.filter(author = request.user)
    d = {"blogs":author_blogs}

    return render(request, 'panel.html',d)

def AddBlog(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        dic = request.POST
        bname = dic['bname']
        des = dic['des']
        auth_data = request.user
        BlogModel.objects.create(author = auth_data,title = bname,description = des)
        return redirect('panel')

    return render(request,'add_blog.html')

def LikeTheBlog(request,bid):
    if not request.user.is_authenticated:
        return redirect('login')
    blogdata = BlogModel.objects.get(id=bid)
    author = request.user
    data = LikeBlog.objects.filter(blog = blogdata,author = author)
    if not data:
        LikeBlog.objects.create(blog = blogdata,author = request.user)
    else:
        data.delete()

    return redirect('detail',bid)


def AddComment(request,bid):
    if not request.user.is_authenticated:
        return redirect('login')
    blogdata = BlogModel.objects.get(id = bid)
    author = request.user
    if request.method == "POST":
        msg = request.POST['msg']
        UserComment.objects.create(author = author,blog = blogdata,comment = msg)
    return redirect('detail',bid)

def Logout(request):
    logout(request)
    return redirect('blogs')

