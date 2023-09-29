from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from profiles.forms import ProfileForm


# Create your views here.
class ProfileEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = ProfileForm(instance=request.user.profile)
        return render(request, "account/profile.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = ProfileForm(
            data=request.POST, files=request.FILES, instance=request.user.profile
        )
        if form.is_valid():
            form.save()
            return redirect(reverse("home"))
        return render(request, "account/profile.html", {"form": form})
