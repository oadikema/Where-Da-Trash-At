from rest_framework import serializers
from rest_framework import serializers

# from django.contrib.auth.models import User, Group

from .models import TrashImageModel
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class TrashImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TrashImageModel
        fields = ("image", "trash_density", "google_ml_json", "time_taken", "before_after_cleaning", "description", "location", "id", "url")



# class AltTrashImageSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = TrashImageModel
#         fields = ("image", "trash_density", "google_ml_json", "time_taken", "before_after_cleaning", "description")


