from django.contrib import admin
from django.urls import path
from Penolong.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', daftar,name='daftar'),
    path('tambah-hewan/',tambah_hewan,name='tambah_hewan'),
    path('hewan/ubah/<int:id_hewan>',ubah_hewan,name='ubah_hewan'),
]
