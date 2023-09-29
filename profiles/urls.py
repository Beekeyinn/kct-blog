from django.urls import path

from profiles.views import ProfileEditView

urlpatterns = [
    path("profile/", ProfileEditView.as_view(), name="profile"),
]
