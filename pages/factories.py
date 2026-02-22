import factory
from .models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("company")
    price = factory.Faker("random_int", min=200, max=9000)


# Faker genera nombres falsos
# Genera precios entre 2000 a 9000
# Crea objeto Product
