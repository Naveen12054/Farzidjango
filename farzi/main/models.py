from django.db import models

from accounts.models import CustomUser,Product,Category

# Create your models here.
class BookCart(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    status=models.BooleanField(default=False)
    quantity = models.CharField(max_length=255, null=True,default=1)
    
    def str(self):
        # return self.book.title
        return f"cart details {self.user.email}: {self.product.product_name}"

class Wishlist(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    status=models.BooleanField(default=False)
    
    def str(self):
        # return self.book.title
        return f"wishlist details {self.user.email}: {self.product.product_name}"