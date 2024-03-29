from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        print(title)
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title 
        price = serializer.validated_data.get('price')
        if price is None:
            price=2.99

        serializer.save(price=price, content=content)

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
        

product_update_view = ProductUpdateAPIView.as_view()

class ProductListAPIView(generics.ListAPIView):
    # not going to use this
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

product_list_view = ProductListAPIView.as_view()



product_update_view = ProductUpdateAPIView.as_view()

class ProductDeleteAPIView(generics.DestroyAPIView):
    # not going to use this
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # if you need to do anything before delete, do it here
        # instance.xxx
        super().perform_destroy(instance)

product_delete_view = ProductDeleteAPIView.as_view()


@api_view(['GET','POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method=='GET':
        if pk is not None:
            # detail view
            queryset = Product.objects.filter(pk=pk)
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        
        #  else, its a list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if method=='POST':
        #create record
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
        
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title 
        
            serializer.save(content=content)

            return Response(serializer.data)
        
        return Response({"invalid": "not good data"}, status=400)