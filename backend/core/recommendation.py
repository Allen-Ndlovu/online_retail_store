import joblib, numpy as np
from django.conf import settings
from .models import Product
from .serializers import ProductSerializer

try:
    model = joblib.load(settings.RECOMMEND_MODEL_PATH)
except:
    model = None

def get_ml_recommendations(product_id, top_k=5):
    if model:
        vec = np.array([product_id]).reshape(1,-1)
        sim_ids = model.predict(vec)[:top_k]
        qs = Product.objects.filter(id__in=sim_ids)
        return ProductSerializer(qs, many=True).data
    # fallback: next products
    qs = Product.objects.exclude(id=product_id)[:top_k]
    return ProductSerializer(qs, many=True).data
