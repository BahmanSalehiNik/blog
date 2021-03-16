from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .forms import PostModelForm
from .models import PostModel
from datetime import datetime, date


def temp_test(request):
    template = 'blog/test-view.html'
    projects_list = ["Market Place", "Bonds Data", "PMService", "Algorithm"]
    context = {
        "name": "Bahmani",
        "lucky": 75,
        "buffer": 35,
        "bdate": date(1985,6,28),
        "objects_list":projects_list,
        "title": "Ava"
    }
    messages.success(request, "Test", fail_silently=True, extra_tags='test')
    return render(request, template, context)


def post_model_create_view(request):
    # if request.method == "POST":
    #     print(request.POST)
    #     form = PostModelForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         print(form.cleaned_data)

    form = PostModelForm(request.POST or None)
    context ={
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        print(form.cleaned_data)
        obj.save()
        messages.success(request, "Created a new blog post")
        context = {
            "form": PostModelForm()
        }
        return HttpResponseRedirect(f"/blog/{obj.id}")

    template = "blog/create-view.html"
    return render(request, template, context)


def post_model_delete_view(request, id):
    target_obj = get_object_or_404(PostModel, id=id)
    if request.method == 'POST':
        target_obj.delete()
        #messages.success(request, "Post deleted")
        return HttpResponseRedirect("/blog/")

    context = {
        "object": target_obj
    }
    template = "blog/delete-view.html"
    return render(request, template, context)


def post_model_update_view(request, id):
    target_obj = get_object_or_404(PostModel, id=id)
    form = PostModelForm(request.POST or None, instance=target_obj)
    context = {
        "object": target_obj,
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        print("Form updated successfully")
        obj.save()
        messages.success(request, f"Updated post with id {id} successfully")
        context = {
            "form": PostModelForm()
        }
        return HttpResponseRedirect(f"/blog/{id}")

    template = "blog/update-view.html"

    return render(request, template, context)
def post_model_detail_view(request, id):
    # try:
    #     obj = PostModel.objects.get(id=id)
    # except ObjectDoesNotExist:
    #     obj = f"No post with id {id}"
    obj = get_object_or_404(PostModel, id=id)
    context = {
        "object": obj
    }
    template = "blog/detail-view.html"
    return render(request, template, context)


#@login_required()
def post_model_list_view(request):
    print(request.GET)
    query = request.GET.get("q")
    qs = PostModel.objects.all()
    if not(query is None):
        qs = qs.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    print(request.user)

    print(qs)

    context = {
        "object_list": qs,
        "name_list": ['Bahman', 'Salehi']
    }
    if request.user.is_authenticated:
        template = 'blog/list-view.html'
        context['user_status'] = 'Authenticated'
    else:
        template = 'blog/list-view-public.html'
        context['user_status'] = 'public'
        #raise Http404

    return render(request, template, context)