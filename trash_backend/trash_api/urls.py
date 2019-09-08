from django.urls import path, include, re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('trash_images', views.TrashImageViewSet)

# router.register('images_light', views.LightTrashImageViewSet)

# router.register('alt_trash_images', views.AltTrashView)


urlpatterns = [
    path('', include(router.urls)),
    path('trash_images_post', views.post_trash_image)
]

