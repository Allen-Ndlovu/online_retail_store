from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model  = OrderItem
        fields = ['product','quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model  = Order
        fields = ['id','created','status','items']

    def create(self, validated):
        items_data = validated.pop('items')
        order = Order.objects.create(**validated)
        objs = [OrderItem(order=order, **item) for item in items_data]
        OrderItem.objects.bulk_create(objs)
        return order
