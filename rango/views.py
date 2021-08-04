from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views import View
from registration.forms import User

from rango.models import UserProfile, AnimalCategory, Animal, Comment
from django.shortcuts import redirect
from django.urls import reverse
from rango.forms import AnimalForm, AnimalCategoryForm, CommentForm
from rango.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from datetime import datetime


def index(request):
    category_list = AnimalCategory.objects.order_by('-views')[:5]
    animal_list = Animal.objects.order_by('-likes')[:5]

    context_dict = {'categories': category_list, 'animals': animal_list}

    visitor_cookie_handler(request)

    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    return render(request, 'rango/about.html', context=context_dict)


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = AnimalCategory.objects.get(slug=category_name_slug)
        animals = Animal.objects.filter(category=category)

        category.views = category.views + 1
        category.save()

        context_dict['animals'] = animals
        context_dict['category'] = category
    except AnimalCategory.DoesNotExist:
        context_dict['animals'] = None
        context_dict['category'] = None

    return render(request, 'rango/category.html', context=context_dict)


@login_required
def add_category(request):
    form = AnimalCategoryForm()
    if request.method == 'POST':
        form = AnimalCategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('rango:index'))
        else:
            print(form.errors)
    return render(request, 'rango/add_category.html', {'form': form})


@login_required
def add_animal(request, category_name_slug):
    try:
        category = AnimalCategory.objects.get(slug=category_name_slug)
    except:
        category = None

    if category is None:
        return redirect(reverse('rango:index'))

    form = AnimalForm()
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            if category:
                animal = form.save(commit=False)
                animal.category = category
                # animal.views = 0
                animal.likes = 0

                if 'picture' in request.FILES:
                    animal.picture = request.FILES['picture']
                animal.save()
                return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_animal.html', context=context_dict)


@login_required
def restricted(request):
    return render(request, 'rango/restricted.html')


def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits


class RegisterProfileView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = UserProfileForm()
        context_dict = {'form': form}
        return render(request, 'rango/profile_registration.html', context_dict)

    @method_decorator(login_required)
    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect(reverse('rango:index'))
        else:
            print(form.errors)

        context_dict = {'form': form}
        return render(request, 'rango/profile_registration.html', context_dict)


class ProfileView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        form = UserProfileForm({'phone': user_profile.phone,
                                'picture': user_profile.picture})

        return (user, user_profile, form)

    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('rango:index'))

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}

        return render(request, 'rango/profile.html', context_dict)

    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('rango:index'))

        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save(commit=True)
            user.email = request.POST['email']
            user.save()
            return redirect(reverse('rango:profile',
                                    kwargs={'username': username}))
        else:
            print(form.errors)

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}

        return render(request, 'rango/profile.html', context_dict)


class ListProfilesView(View):
    @method_decorator(login_required)
    def get(self, request):
        profiles = UserProfile.objects.all()

        return render(request, 'rango/list_profiles.html', {'user_profile_list': profiles})


class AnimalProfileView(View):
    def get_animal_details(self, animal_name):
        try:
            animal = Animal.objects.get(animal_name=animal_name)
            comments = Comment.objects.filter(animal=animal)
        except animal.DoesNotExist:
            animal = None
            comments = None

        form = CommentForm()

        return (animal, form, comments)

    @method_decorator(login_required)
    def get(self, request, animal_name):
        try:
            (animal, form, comments) = self.get_animal_details(animal_name)
        except TypeError:
            return redirect(reverse('rango:index'))

        context_dict = {'selected_animal': animal,
                        'form': form,
                        'comments': comments}

        return render(request, 'rango/animal_profile.html', context_dict)

    @method_decorator(login_required)
    def post(self, request, animal_name):
        try:
            (animal, form, comments) = self.get_animal_details(animal_name)
        except TypeError:
            return redirect(reverse('rango:index'))

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('rango:animal_profile',
                                    kwargs={'animal_name': animal_name}))
        else:
            print(form.errors)

        context_dict = {'selected_animal': animal,
                        'form': form,
                        'comments': comments}

        return render(request, 'rango/animal_profile.html', context_dict)


class LikeAnimalView(View):
    @method_decorator(login_required)
    def get(self, request):
        animal_id = request.GET['animal_id']
        try:
            animal = Animal.objects.get(id=int(animal_id))
        except Animal.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)

        animal.likes = animal.likes + 1
        animal.save()

        return HttpResponse(animal.likes)


class SearchAnimalView(View):
    def post(self, request, category_name_slug):
        if 'suggestion' in request.POST:
            suggestion = request.POST['suggestion']
        else:
            suggestion = ''

        context_dict = {}
        try:
            category = AnimalCategory.objects.get(slug=category_name_slug)
            animal_list = get_animal_list(max_results=8, starts_with=suggestion)

            if len(animal_list) == 0:
                animal_list = Animal.objects.order_by('-likes')

            context_dict['animals'] = animal_list
            context_dict['category'] = category
        except AnimalCategory.DoesNotExist:
            context_dict['animals'] = None
            context_dict['category'] = None

        return render(request, 'rango/category.html', context=context_dict)


def get_animal_list(max_results=0, starts_with=''):
    animal_list = []

    if starts_with:
        animal_list = Animal.objects.filter(animal_name__istartswith=starts_with)

    if max_results > 0:
        if len(animal_list) > max_results:
            animal_list = animal_list[:max_results]

    return animal_list


@login_required
def CommentPostView(request, animal_name, username):
    try:
        target_animal = Animal.objects.get(animal_name=animal_name)
        user = User.objects.get(username=username)
    except:
        target_animal = None
        user = None

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():

            comment = form.save(commit=False)

            comment.animal = target_animal
            comment.email = user.email
            comment.username = username
            comment.save()

            comment_list = Comment.objects.filter(animal=target_animal)

            new_comment_form = CommentForm()

            context_dict = {'selected_animal': target_animal,
                            'form': new_comment_form,
                            'comments': comment_list}

            return render(request, 'rango/animal_profile.html', context_dict)

        else:
            print(form.errors)

    context_dict = {'selected_animal': target_animal,
                    'form': form,
                    'comments': None}
    return render(request, 'rango/animal_profile.html', context=context_dict)
