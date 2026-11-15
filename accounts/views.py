from django.shortcuts import render , redirect , get_object_or_404
from django.views import View
from accounts.models import User , Profile
from accounts.forms import UserRegistrationForm, UserLoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class UserRegisterView(View):
    template_name = 'accounts/register.html'
    form_class = UserRegistrationForm
    def dispatch(self, request, *args, **kwargs) :
        if request.user.is_authenticated:
            return redirect('blog:home')
        return super().dispatch(request,*args,**kwargs)
    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully' , 'success')
            return redirect('account:login')
        return render(request,self.template_name,{'form':form})
class UserLoginView(View):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm
    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form = self.form_class(request.POST)
        self.next = request.GET.get('next')
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'], password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'Successfully logged in' , 'success')
                if self.next:
                    return redirect(next)
                return redirect('blog:home')
            messages.error(request,'Invalid Credentials' , 'danger')
        return render(request,self.template_name,{'form':form})

class UserLogoutView(LoginRequiredMixin,View):
    def post(self,request):
        logout(request)
        messages.success(request,'Successfully logged out' , 'success')
        return redirect('account:login')

class UserUpdateView(LoginRequiredMixin,View):
    template_name = 'accounts/update.html'
    form_class = UserUpdateForm
    def setup(self, request, *args, **kwargs):
        self.user = get_object_or_404(User, pk=kwargs['user_id'])
        return super().setup(request,*args,**kwargs)
    def dispatch(self, request, *args, **kwargs):
        if request.user != self.user :
            return redirect('blog:home')
        return super().dispatch(request,*args , **kwargs)
    def get(self,request,*args,**kwargs):
        form = self.form_class(instance=self.user)
        return render(request,self.template_name,{'form':form , 'user':self.user})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST, instance=self.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully updated account' , 'success')
            return redirect('blog:home')
        messages.error(request,'Invalid Credentials' , 'danger')
        return render(request,self.template_name,{'form':form , 'user':self.user})

class UserProfileView(LoginRequiredMixin, View):
    template_name = 'accounts/profile.html'
    def get(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)

        return render(request,self.template_name,{'profile': profile})

class ProfileUpdateView(LoginRequiredMixin, View):
    template_name = 'accounts/profile_update.html'

    form_class_profile = ProfileUpdateForm
    form_class_user = UserUpdateForm

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        self.profile, self.created = Profile.objects.get_or_create(
            user=request.user
        )

    def get(self, request, *args, **kwargs):
        form_profile = self.form_class_profile(
            instance=self.profile
        )
        form_user = self.form_class_user(
            instance=request.user
        )

        return render(request, self.template_name, {
            'profile_form': form_profile,
            'user_form': form_user,
        })

    def post(self, request, *args, **kwargs):
        form_profile = self.form_class_profile(
            request.POST,
            request.FILES,
            instance=self.profile
        )

        form_user = self.form_class_user(
            request.POST,
            instance=request.user
        )

        if form_profile.is_valid() and form_user.is_valid():
            form_profile.save()
            form_user.save()

            messages.success(request, 'Successfully updated profile')
            return redirect('account:profile')

        messages.error(request, 'Please correct the errors.')

        return render(request, self.template_name, {
            'profile_form': form_profile,
            'user_form': form_user,
        })