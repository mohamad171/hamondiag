from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.base import View
from blog.models import Blog
# ,Text,Picture,Content
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.apps import apps
from django.views.generic.list import ListView
from blog.forms import BlogForm
class BlogView(View):
    def get(self,request):
        form = BlogForm()
        blogs = Blog.objects.all().order_by("-created")
        return render(request,"blog/add-blog.html",{"form":form,"blogs":blogs})
    def post(self,request):
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            object = form.save()
            return redirect("edit-blog",object.slug)
        return render(request,"blog/add-blog.html",{"form":form})
class BlogContent(View):
    blog = None
    last_blogs =None
    model = None
    form = None
    def get(self,request,slug):

        try :
            self.blog = Blog.objects.get(slug=slug)
            self.form = BlogForm(instance=self.blog)
        except Blog.DoesNotExist:
            pass
        self.last_blogs = Blog.objects.all().order_by("-created")[0:5]

        return render(request,"blog/edit-blog.html",{"form":self.form
                      ,"blog":self.blog,"last_blogs":self.last_blogs})
    def post(self,request,slug):
        try :
            self.blog = Blog.objects.get(slug=slug)
            self.form = BlogForm(request.POST, request.FILES,instance=self.blog)
        except Blog.DoesNotExist:
            pass
        if self.blog:
            if self.form.is_valid():
                object = self.form.save()
                return redirect("edit-blog", object.slug)

class BlogListView(ListView):
    template_name = "blog/blogs.html"
    model = Blog
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["last_blogs"] = Blog.objects.all().order_by("-created")[0:5]
        return context

class BlogDetailView(View):
    def get(self,request,slug):
        blog = Blog.objects.get(slug=slug)
        last_blogs = Blog.objects.all().order_by("-created")[0:5]
        return render(request,"blog/blog.html",{"blog":blog,"last_blogs":last_blogs})
class BlogDeleteView(View):
    def get(self,request,slug):
        blog = Blog.objects.get(slug=slug)
        blog.delete()
        return redirect("add-blog")