from django import forms

from blog.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','image','status']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'status': forms.CheckboxInput(attrs={'class':'form-control'}),
        }
