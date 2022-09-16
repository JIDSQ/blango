from django.urls import path
from . import views


urlpatterns = [
  path ("",views.index),
  path("post/<slug>/", views.post_detail, name="blog-post-detail"),
  path("ip/" , views.get_ip, name="get-IP")
]