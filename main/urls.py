from django.contrib import admin
from django.urls import path

from charter.views import chartPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chartPage, name="chartPage")
]
