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


# class CategoryForm(forms.ModelForm):
#     name = forms.CharField(max_length=Category.NAME_MAX_LENGTH, help_text="Please enter the category name.")
#     views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#     likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#     slug = forms.CharField(widget=forms.HiddenInput(), required=False)
#
#     class Meta:
#         model = Category
#         fields = ('name',)


class AnimalForm(forms.ModelForm):
    # animal_name = forms.CharField(max_length=Animal.NAME_MAX_LENGTH, help_text="Please enter the name of this animal.")
    # brief = forms.CharField(max_length=200, help_text="Please enter the breif of this animal.")
    # likes = forms.IntegerField(initial=0)
    # picture = forms.ImageField()

    class Meta:
        model = Animal
        fields = ('animal_name', 'brief', 'picture')
        exclude = ('category',)

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     url = cleaned_data.get('url')
    #
    #     if url and not url.startswith('http://'):
    #         url = f'http://{url}'
    #         cleaned_data['url'] = url
    #
    #     return cleaned_data

# class PageForm(forms.ModelForm):
#     title = forms.CharField(max_length=Page.TITLE_MAX_LENGTH, help_text="Please enter the title of the page.")
#     url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
#     views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#
#     class Meta:
#         model = Page
#         exclude = ('category',)
#
#     def clean(self):
#         cleaned_data = self.cleaned_data
#         url = cleaned_data.get('url')
#
#         if url and not url.startswith('http://'):
#             url = f'http://{url}'
#             cleaned_data['url'] = url
#
#         return cleaned_data


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
        # 指定一些 Meta 选项以改变 form 被渲染后的样式
        model = Comment # form 关联的 Model

        # fields = ['username', 'email', 'content']
        fields = ('content',)

        # fields 表示需要渲染的字段，这里需要渲染username、email、content
        # 这样渲染后表单会有三个文本输入框，分别是输入user_name、user_email、body的输入框

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