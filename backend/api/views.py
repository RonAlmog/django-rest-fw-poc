from django.forms.models import model_to_dict
from django.http import JsonResponse
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


# this makes it drf api view!
@api_view(['POST'])
def api_home(request, *args, **kwargs):
    
    serializer = ProductSerializer(request.data)
    if(serializer.is_valid):
         print(serializer.data)
         data = serializer.data
         return Response(data)