from django import forms
from rango.models import Animal, AnimalCategory,UserProfile,Comment

from django.contrib.auth.models import User


class AnimalCategoryForm(forms.ModelForm):
    category_name = forms.CharField(max_length=AnimalCategory.NAME_MAX_LENGTH, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = AnimalCategory
        fields = ('category_name',)


class AnimalForm(forms.ModelForm):
    # animal_name = forms.CharField(max_length=Animal.NAME_MAX_LENGTH, help_text="Please enter the name of this animal.")
    # brief = forms.CharField(max_length=200, help_text="Please enter the breif of this animal.")
    # likes = forms.IntegerField(initial=0)
    # picture = forms.ImageField()

    class Meta:
        model = Animal
        fields = ('animal_name', 'brief','size','distribution_area', 'picture')
        exclude = ('category',)

        help_texts={
            'animal_name': "Please enter the name of this animal",
            'brief': "Please enter the brief of this animal",
            'size': "Please enter the normal height and weight of this animal ",
            'distribution_area': "Please enter the main distribution area of this animal",
            'picture': "Please submit the picture of this animal"
        }
        widgets={
            'animal_name': forms.TextInput(attrs={
                'class': 'form-control',
                'aria-describedby': "sizing-addon1",
            }),
            'brief': forms.Textarea(attrs={
                'class': 'form-control',
                'aria-describedby': "sizing-addon1",
            }),
            'size': forms.Textarea(attrs={
                'class': 'form-control',
                'aria-describedby': "sizing-addon1",
            }),
            'distribution_area': forms.Textarea(attrs={
                'class': 'form-control',
                'aria-describedby': "sizing-addon1",
            }),

        }




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'picture')



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        widgets = {
            # 为各个需要渲染的字段指定渲染成什么html组件，主要是为了添加css样式。
            # 例如 user_name 渲染后的html组件如下：
            # <input type="text" class="form-control" placeholder="Username" aria-describedby="sizing-addon1">

            # 'username': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': "please enter your username",
            #     'aria-describedby': "sizing-addon1",
            # }),
            # 'email': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': "please enter your e_mail",
            #     'aria-describedby': "sizing-addon1",
            # }),
            'content': forms.Textarea(attrs={'placeholder': 'please enter your comment'}),
        }