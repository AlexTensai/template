from django.db import models

# Many-to-one

class Category(models.Model):
	categoryId = models.AutoField(primary_key=True)
	category_name = models.CharField(max_length=30)
	type_name = models.CharField(max_length=30)

	def __str__(self):
		return f"[{self.categoryId}] {self.category_name} {self.type_name}"

class Product(models.Model):
	productId = models.AutoField(primary_key=True)
	headline = models.CharField(max_length=100)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default = None)

	def __str__(self):
		return f"[{self.productId}] {self.headline} (Category: {self.category})"


