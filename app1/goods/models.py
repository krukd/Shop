from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=300, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'


    def __str__(self) -> str:
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=300, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'
        ordering = ('id',)

    def __str__(self) -> str:
        return f'{self.name} Количество - {self.quantity}'
    
    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        
        return self.price