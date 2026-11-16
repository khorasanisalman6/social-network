from django.shortcuts import render , redirect , get_object_or_404
from django.views import View

# Create your views here.
from .models import Post
from .forms import PostCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from django.contrib import messages
class HomePage(View):
    template_name = 'blog/home.html'
    def get(self,request):
        posts = Post.objects.all()
        return render(request,self.template_name , {'posts':posts})

class PostCreateView(LoginRequiredMixin,View):
    template_name = 'blog/create.html'
    form = PostCreateForm
    def get(self,request):
        form = PostCreateForm()
        return render(request,self.template_name , {'form':form})
    def post(self,request):
        form = PostCreateForm(request.POST , request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.slug = slugify(post.content)[:30]
            post.save()
            messages.success(request, 'Post created successfully','success')
            return redirect('blog:home')
        messages.error(request, 'Error in post.','danger')
        return render(request , self.template_name , {'form':form})

class PostUpdateView(LoginRequiredMixin,View):
    template_name = 'blog/update.html'
    form = PostCreateForm
    def setup(self,request,*args,**kwargs):
        self.post_instance = get_object_or_404(Post,pk = kwargs['pk'])
        return super().setup(request,*args,**kwargs)

    def dispatch(self,request,*args,**kwargs):
        post = self.post_instance
        if post.user.id != request.user.id:
            return redirect('blog:home')
        return super().dispatch(request,*args,**kwargs)
    def get(self,request,*args,**kwargs):
        post = self.post_instance
        form = self.form(instance=post)
        return render(request,self.template_name , {'form':form})
    def post(self,request,*args,**kwargs):
        post = self.post_instance
        form = self.form(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.slug = slugify(post.content)[:30]
            post.save()
            messages.success(request, 'Post Update successfully','success')
            return redirect('blog:home')
        messages.error(request, 'post Update Error','danger')
        return render(request , self.template_name , {'form':form})

class PostDetailView(LoginRequiredMixin,View):
    template_name = 'blog/detail.html'
    def setup(self,request,*args,**kwargs):
        self.post_instance = get_object_or_404(Post,slug = kwargs['slug'],pk = kwargs['pk'])
        return super().setup(request,*args,**kwargs)
    def get(self,request,*args,**kwargs):
        post = self.post_instance
        return render(request,self.template_name , {'post':post})

class PostDeleteView(LoginRequiredMixin,View):
    template_name = 'blog/delete.html'
    def setup(self,request,*args,**kwargs):
        self.post_instance = get_object_or_404(Post,pk = kwargs['pk'])
        return super().setup(request,*args , **kwargs)
    def dispatch(self,request,*args,**kwargs):
        if self.post_instance.user.id != request.user.id:
            return redirect('blog:home')
        return super().dispatch(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        post = self.post_instance
        if post:
            post.delete()
            messages.success(request, 'Post deleted successfully','success')
            return redirect('blog:home')
        messages.error(request, 'post delete error.','danger')
