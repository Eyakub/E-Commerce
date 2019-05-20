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
from ecommerce.products.models import Product

qs = Product.object.all()
print(qs)
tshirt = qs.first()
tshirt.title
tshirt.description

tshirt.tag
"""
raises an error because the product model doesn't have a field "tag"
Product object has no attribute 'tag'
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


# OR queries
# queryset = User.objects.filter(
#     first_name__startwith='E'
#     ) | User.objects.filter(
#     last_name__startwith='S'
# )
# or by importing (from django.db.models import Q)
# qs = User.objects.filter(Q(first_name__startwith='E') |
#                          Q(last_name__startwith='S'))


# AND queries

# queryset = User.objects.filter(
#     first_name__startwith='E'
#     ) & User.objects.filter(
#     last_name__startwith='S'
# )
#
# queryset1 = User.objects.filter(
#     first_name__startwith='E',
#     last_name__startwith='S'
# )
#
# or by importing (from django.db.models import Q)
# queryset2 = User.objects.filter(Q(first_name__startwith='E') &
#                          Q(last_name__startwith='S'))


# BULK_CREATE (to create multiple object at once)

# Author.objects.bulk_create([
#     Author(name='spike', email='spike@mail.com'),
#     Author(name='tyke', email='tyke@mail.com'),
#     Author(name='droopy', email='droopy@mail.com'),
# )


# VALUE_LIST (return multiple column field value)

# Author.objects.values_list("id", "name")
# <QuerySet [(1, 'tom'), (2, 'jerry'), (3, 'spike'), (4, 'tyke'), (5, 'droopy')]>
# Author.objects.filter(id__gt=3).values_list("id", "name")
# <QuerySet [(4, 'spike'), (5, 'tyke'), (6, 'droopy')]>

# VALUES() same as VALUE_LIST but it returns a QuerySet where each element is a dictionary instead of tuple.
# r = Author.objects.filter(id__gt=3).values("id", "name")
#
# QuerySet [{'name': 'spike', 'id': 4}, {'name': 'tyke', 'id': 5}, {'name': 'droo
# py', 'id': 6}]
