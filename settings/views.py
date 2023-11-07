from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from settings.models import Settings
from django.urls import reverse_lazy
from settings.forms import ProductForm,CategoryForm,TagFrom,SettingsForm
from product.models import Product,Category,Tag
from django.views.generic import CreateView,UpdateView,DeleteView,FormView,View
class BaseView(LoginRequiredMixin) :
    template_name = "settings/product.html"
    success_url = reverse_lazy("settings:settings")
class CreateProduct(BaseView,CreateView):
    form_class = ProductForm
class CreateCategoryView(BaseView,CreateView):
    form_class = CategoryForm
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = Category.objects.all() 
        context["url"] = "settings:category-delete"
        return context
class CreateTag(BaseView,CreateView):
    form_class = TagFrom
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = Tag.objects.all()
        context["url"] = "settings:delete-tag" 
        return context
class SettingsView(View):
    def get(self,request):
        return render(request,"settings/settings.html")
class UpdateProduct(BaseView,UpdateView):
    template_name = "settings/product.html"
    model = Product
    fields = ["name","price","discount","image","category","tags"]
    success_url = reverse_lazy("product:main")
class DeleteCategory(DeleteView):
    template_name = "product/main.html"
    model = Category
    success_url = reverse_lazy("product:main")
class DeleteTag(DeleteView):
    template_name = "product/main.html"
    model = Tag
    success_url = reverse_lazy("settings:settings")
class Total(View):
    def get(self,request):
        if request.user.is_staff:
            setting = Settings.objects.all().first()
            form = SettingsForm(instance=setting)
            return render(request,"settings/total.html",{"form":form})
    def post(self,request,slug=None):
        if request.user.is_staff:
            setting = Settings.objects.all().first()
            form = SettingsForm(request.POST,request.FILES,instance=setting)
            if form.is_valid():
                form.save()
                return redirect("settings:settings")
            return render(request,"settings/total.html",{"form":form})