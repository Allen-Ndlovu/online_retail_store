from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .recommendation import get_ml_recommendations

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields    = ['name','description']
    ordering_fields  = ['price','rating','stock']
    ordering         = ['-rating']

    @action(detail=True, methods=['get'])
    def recommend(self, request, pk=None):
        return Response(get_ml_recommendations(int(pk)))
