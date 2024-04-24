from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap

from . import views

from blog.models import Post

info_dict = {
    "queryset": Post.objects.all(),
    "date_field": "updated_date",
}

app_name = "core"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),

    path("profile/logout/", views.LogoutView.as_view(), name="logout"),
    path("profile/password_change/", views.PasswordChangeView.as_view(), name="password_change"),
    path("profile/password_change/done/", views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("profile/password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path("profile/password_reset/done/", views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("profile/reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("profile/reset/done/", views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("profile/", views.ProfileView.as_view(), name="profile"),

    path("sitemap.xml", sitemap, {"sitemaps" : { "blog_posts": GenericSitemap(info_dict) }}, name="sitemap")
]
