from django.contrib import admin

# Register your models here.
from app.models import Babysitter, Contact, Decoration,Book_Deco
 
admin.site.register(Contact)
admin.site.register(Decoration)
admin.site.register(Book_Deco)
admin.site.register(Babysitter)
