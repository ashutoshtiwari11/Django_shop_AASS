from django.contrib import admin

from .models import Product
from  .models import Orders
from .models import Contactdata

admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Contactdata)
#here we need to register our app model in admin

