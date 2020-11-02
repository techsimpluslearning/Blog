
from django.contrib import admin
from django.urls import path
from Blog.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
path('', Home, name='blogs'),
path('blog_detail/<int:bid>/', Blogdetail, name="detail"),
path('Login/', LoginForm, name='login'),
path('Signup/', Signup, name='signup'),
path('UserPanel', AuthorPanel, name='panel'),
path('add_blog/',AddBlog,name ='add_blog'),
path('blog_comment/<int:bid>/', AddComment, name="comment"),
path('blog_like/<int:bid>/', LikeTheBlog, name="like"),
path('logout/', Logout, name='logout'),
]
