from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, SITE_INFO
from .forms import CreatePostForm, EditPostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


# Create your views here.
def index(request):
    all_posts = Post.objects.filter(is_draft=False, is_delete=False)
    context = {
        'all_posts': all_posts,
        'contacts': SITE_INFO['contacts'],
        "site_info": SITE_INFO['site_info'],
        'about': 'Эта страничка показывает наши навыки как FrontEnd так и BackEnd',
        'Follow_on_Twitter': 'https://twitter.com/?lang=ru',
        'Like_on_Facebook': 'https://www.facebook.com/',
        'description_vlog': 'За частую нам хочется поведать всему миру о том или ином событии '

    }
    return render(
        request=request,
        template_name='vlog_app/index.html',
        context=context
    )


@ login_required()
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, is_draft=False, is_delete=False)

    context = {
        'post': post,
        'contacts': SITE_INFO['contacts'],
        "site_info": SITE_INFO['site_info'],
    }
    return render(
        request=request,
        template_name='vlog_app/post_detail.html',
        context=context,
    )


@ login_required()
def create_post(request):
    form = CreatePostForm()

    context = {
        'form': form,
        'contacts': SITE_INFO['contacts'],
        "site_info": SITE_INFO['site_info'],
    }

    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(user_id=request.user.id)
            return redirect('my-profile')

    return render(
        request=request,
        template_name='vlog_app/post_create.html',
        context=context
    )


def registration(request):
    form = UserCreationForm()
    context = {
        'form': form,
        'contacts': SITE_INFO['contacts'],
        "site_info": SITE_INFO['site_info'],
    }

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(
                request=request,
                user=user
            )
            return redirect('/')
    return render(
        request=request,
        template_name='registration/sing-up.html',
        context=context,
    )


def edit_post(request, post_id):
    post = get_object_or_404(
        Post, pk=post_id,
        user_id__id=request.user.id,
        is_delete=False
    )
    form = EditPostForm(
        instance=post
    )

    context = {
        'form': form,
        'contacts': SITE_INFO['contacts'],
        "site_info": SITE_INFO['site_info'],
    }

    if request.method == 'POST':
        form = EditPostForm(
            request.POST,
            request.FILES,
            instance=post,
        )
        if form.is_valid():
            form.save()
            return redirect('my-profile')

    return render(
        request=request,
        template_name='vlog_app/post-edit.html',
        context=context,
    )


@login_required
def my_profile(request):
    all_posts = Post.objects.filter(user_id__id=request.user.id, is_delete=False)
    context = {
        'all_posts': all_posts,
        'contacts': SITE_INFO['contacts'],
        "site_info": SITE_INFO['site_info'],
        # 'Follow_on_Twitter': 'https://twitter.com/?lang=ru',
        # 'Like_on_Facebook': 'https://www.facebook.com/',
        # 'description_vlog': 'За частую нам хочется поведать всему миру о том или ином событии '

    }
    return render(
        request=request,
        template_name='vlog_app/my-profile.html',
        context=context
    )
