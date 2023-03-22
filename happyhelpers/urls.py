
from django.contrib import admin
from django.urls import path,include 

admin.site.site_header = "Happy Helpers Admin"
admin.site.site_Title = "Happy Helpers Admin portal"
admin.site.index_title = "Welcome to Happy Helpers Database"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
