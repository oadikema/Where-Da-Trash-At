from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import datetime

from .serializers import TrashImageSerializer, LightweightTrashImageSerializer
from .models import TrashImageModel

from rest_framework_gis.filters import DistanceToPointFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.parsers import JSONParser

from rest_framework.decorators import api_view

import json

#google cloud
import io
import os

# ===========LOGGIGNG
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
import base64

#

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ="/home/artic/Desktop/Coding/WebApps/TrashFindFrontend/trash_backend/trash_backend/trash_api/My First Project-28fdd5c60886.json"

# Instantiates a client
client = vision.ImageAnnotatorClient()


# Create your views here.

class TrashImageViewSet(viewsets.ModelViewSet):
    queryset = TrashImageModel.objects.all()
    serializer_class = LightweightTrashImageSerializer

class LightTrashImageViewSet(viewsets.ModelViewSet):
    queryset = TrashImageModel.objects.all()
    serializer_class = LightweightTrashImageSerializer

    

# class AltTrashView(viewsets.ModelViewSet):
#     queryset = AltTrashImageModel.objects.all()
#     serializer_class = AltTrashImageSerializer

@api_view(['POST', 'GET'])
def log_response(request):

    if request.method == "POST":
        message_dictionary = JSONParser().parse(request)
        logger.error(message_dictionary)




@api_view(['POST', 'GET'])
def post_trash_image(request):

    """
    *   { image : "....... ", 
    *     coordinates: [ latitude, longitude  ],       
    *       }
    *

    * location = JSONField()
    * image = models.TextField()
    * trash_density = models.DecimalField(max_digits=16, decimal_places=8)
    * google_ml_json = JSONField()
    * time_taken = models.DateField(default=None, blank=True, null=True)
    * before_after_cleaning = models.BooleanField()
    * description = models.CharField(max_length=150)
    *
    *

    """

    trash_database_ai = ["bottle","plastic", "paper", "card", "can", "wrapper", "plastic bottle", "soda can"]


    # os.system('export GOOGLE_APPLICATION_CREDENTIALS="My First Project-28fdd5c60886.json"')

    if request.method == "POST":

        logger.error(" ============================================= TRYING TO CONNECT TO GCLOUD ============================================= ")
        #logger.error(request)
        #message_dictionary = json.loads(request)
        message_dictionary = JSONParser().parse(request)

        #logger.error(message_dictionary)

        image_base_64_str = message_dictionary["image"]

        location_data = message_dictionary["coordinates"]

        image_base_64_bytes = image_base_64_str.encode('utf-8') # file is a bytes array

        b64Image = base64.b64decode(image_base_64_bytes) # take file from bytes array to b64 byte array

        b = io.BytesIO(b64Image)

        image_view = b.read()

        # logger.error(type(image_view))
        
        #fileName = "/home/artic/Desktop/Coding/WebApps/TrashFindFrontend/trash_backend/trash_backend/imageToSend.png.png"
        # logger.error("============ past getting data =========")

        # with open(, "wb") as image_to_send:
        #     image_to_send.write(base64.decodebytes(image_base_64_bytes))

        # with io.open(file_name, 'rb') as image_file:
        #     content = image_file.read()

        logger.error("============ past encoding =========")

        image = types.Image(content=image_view)
        response = client.label_detection(image=image)
        labels = response.label_annotations

        logger.error(response)

        # google_json = JSONParser().parse(response)
        # logger.error(google_json)


        logger.error("============ LABELS =========")
        logger.error(len(labels))
        accumulator = ""
        num_trash = 0
        for label in labels:

            logger.error(label.description.lower())
            
            if label.description.lower() in trash_database_ai:

                num_trash +=1

        
        shit_json = {"hard": "code"}
        
        trashModel = TrashImageModel(

            location = location_data,
            google_ml_json = shit_json,
            image = image_base_64_str,
            trash_density = num_trash,
            time_taken = "2019-09-07",
            before_after_cleaning = False,
            description = "deadlines are deadlines"

        )

        trashModel.save()

        return HttpResponse(status=200)

       

        
        




