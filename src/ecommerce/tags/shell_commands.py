# Shell session 1
from ecommerce.tags.models import Tag

qs = Tag.objects.all()
print(qs)
black = Tag.objects.last()
black.title
black.slug

black.products
"""
Returns what? check it by yourself
"""

black.products.all()
"""
This is an actual queryset of PRODUCTS
Much like products.objects.all(), but in this case it's ALL of the products that are related to the "Black" tag
"""
black.products.all().first()
"""
return the first instance, if any
"""

exit()


# Session 2
from products.models import Product

qs = Product.object.all()
print(qs)
tshirt = qs.first()
tshirt.title
tshirt.description

tshirt.tag
"""
raises an error because the product model doesn't have a field "tag"
"""

tshirt.tags
"""
Raises an error because the product model doesn't have a field "tags"
"""

tshirt.tag_set
"""
This works because the Tag model has the "products" field with the ManyToMany to Product
"""

tshirt.tag_set.all()
"""
Returns an actual queryset of the Tag model related to this product
"""

tshirt.tag_set.filter(title__icontains='black')
