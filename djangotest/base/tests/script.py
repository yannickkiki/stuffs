from base.models import Product

Product.objects.filter(id__lt=0).all()
