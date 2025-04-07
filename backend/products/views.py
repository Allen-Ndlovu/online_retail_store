from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .recommendations import get_recommendations

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'])
    def recommendations(self, request):
        recommended_ids = get_recommendations()  # List of product IDs
        products = Product.objects.filter(id__in=recommended_ids)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
