from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


class Categories(models.Model):
    Choices = {
        ("food", "food"),
        ("clothes", "clothes"),
        ("shoes", "shoes"),
    }
    category = models.CharField(choices=Choices, default="selcect a category", max_length=40)

    # stringify output
    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"
        


# products
class Product(models.Model):
    name = models.CharField(max_length=400)
    main_price = models.PositiveIntegerField()
    discounted_price = models.PositiveIntegerField()
    view_count = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="media/images")
    
    # stringify output
    def __str__(self):
        return self.name

# cart item
class CartItem(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE ) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    amount = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True) 
    quantity = models.PositiveBigIntegerField(default=1)
   
    
    
    # stringify output
    def __str__(self):
       
        return str(self.product)
    
    # grand total
class GrandTotal(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE ) 
    total = models.PositiveIntegerField(default=0)
    
    def __str__(self):
           
        return str(self.total)
     
   


    
    # contact model 
class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
           
        return str(self.first_name)

    
class CustomerProfile(models.Model):
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email = models.EmailField()
    picture = models.ImageField(upload_to='profile_pics')
    date_joined = models.DateField(auto_now_add=True)
    username = models.CharField(max_length=300)
    address = models.CharField(max_length = 500)
    
    def __str__(self):
           
        return str(self.first_name)
         
    
     
