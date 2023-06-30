from import_export import resources
from .models import Product

class ProductResource(resources.ModelResource):
	class meta:
		model = Product

