from django.db import models
this_session_quantity= 0
this_session_total_charges=0.00
# Create your models here.
class ItemManager(models.Manager):
    
    def single_item_price(self, postData):
        b=Item.objects.get(id=postData['item_id'])
        unit_cost = float(b.price)
        return  unit_cost

    def total_price_calculator(self, postData):
        global this_session_total_charges
        total_charged=0.00
        units=int(postData['quantity'])
        b=Item.objects.get(id=postData['item_id'])
        unit_cost = float(b.price)
        total_charged += (unit_cost * units)
        this_session_total_charges += total_charged
        return total_charged
    
    def this_session_quantity(self, postData):
        global this_session_quantity 
        this_session_quantity+= int(postData['quantity'])
        return this_session_quantity

    def this_session_total(self):
        global this_session_total_charges
        return this_session_total_charges


class Item(models.Model):
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=7, decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=ItemManager()