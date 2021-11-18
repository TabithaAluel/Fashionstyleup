from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Avg, Count
from django.forms import ModelForm
from django.db.models.fields import URLField


class Category(models.Model):
	name = models.CharField(max_length=50,unique=True,null=True)
	slug = models.SlugField(max_length=50,unique=True,null=True)
	image = models.ImageField(upload_to='product', blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2,null=True)


	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='category',blank=True) 
	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def get_url(self):  
		return reverse('shop:products_by_category', args=[self.slug]) 

	def __str__(self): 
		return '{}'.format(self.name)


class Product(models.Model):
	pair_with = models.ManyToManyField(User, related_name='pair_with'	, blank=True)

	
	name = models.CharField(max_length=50, unique=True,null=True)
	slug = models.SlugField(max_length=50, unique=True,null=True) 
	description = models.TextField(blank=True,null=True)
	#product_id = models.AutoField(primary_key=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	discount=models.BigIntegerField(default="1")
	
	image = models.ImageField(upload_to='product', blank=True)
	# image1 = models.ImageField(upload_to='product', blank=True)
	# image2 = models.ImageField(upload_to='product', blank=True)
	# image3 = models.ImageField(upload_to='product', blank=True)
	# image4 = models.ImageField(upload_to='product', blank=True)
	stock = models.BigIntegerField(null=True)
	available = models.BooleanField(default=True,null=True) 
	created = models.DateTimeField(auto_now=True,null=True)
	updated = models.DateTimeField(auto_now=True,null=True)


	favourite = models.ManyToManyField(User ,related_name='favourite',blank=True,null=True)
	


	class Meta:
		ordering = ('name',)
		verbose_name = 'product'
		verbose_name_plural = 'products'

	def get_url(self):
		return reverse('shop:ProdCatDetail', args=[self.category.slug, self.slug])
	
	def __str__(self):
		return '{}'.format(self.name)


