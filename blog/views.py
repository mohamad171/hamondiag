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
    def get(self,request,slug):
        try :
            self.blog = Blog.objects.get(slug=slug)
        except Blog.DoesNotExist:
            pass
        self.last_blogs = Blog.objects.all().order_by("-created")[0:5]
        for content in self.blog.contents.all():
            pass

        return render(request,"blog/edit-blog.html",{"textform":"form1","pictureform":"form2"
                      ,"blog":self.blog,"last_blogs":self.last_blogs})
    # def post(self,request,slug):
    #     form1 = TextContentForm(data=request.POST)
    #     form2 = PicturContentForm(request.POST,request.FILES)
    #     if form1.is_valid():
    #         obj = form1.save()
    #         content = Content.objects.create(content_object=obj,blog_id=
    #                 Blog.objects.get(slug=slug).id)
    #         return redirect("edit-blog",slug)
    #     if form2.is_valid():
    #         obj = form2.save()
    #         content = Content.objects.create(content_object=obj, blog_id=
    #         Blog.objects.get(slug=slug).id)
    #         return redirect("edit-blog", slug)
    #     return render(request,"blog/edit-blog.html",{"textform":form1,"pictureform":form2
    #                   ,"blog":self.blog,"last_blogs":self.last_blogs})

class BlogListView(ListView):
    template_name = "blog/blogs.html"
    model = Blog
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["last_blogs"] = Blog.objects.all().order_by("-created")[0:5]
        return context
class BlogDetailView(DetailView):
    template_name = "blog/blog.html"
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