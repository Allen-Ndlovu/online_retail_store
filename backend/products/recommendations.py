import random
from .models import Product

def get_recommendations():
    """
    Dummy recommendation engine: returns IDs of randomly selected products.
    Replace this with an actual AI-based recommendation in the future.
    """
    all_ids = list(Product.objects.values_list('id', flat=True))
    if not all_ids:
        return []
    num_recommendations = min(3, len(all_ids))
    return random.sample(all_ids, num_recommendations)
