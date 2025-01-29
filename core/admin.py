from django.contrib import admin

# Register your models here.
from .models import Marca

class Marcas(admin.ModelAdmin):

    list_display = ['id','nombre','categorias','descripcion','estado','created_at','updated_at','deleted_at']
    list_filter = ('categorias','estado',)
    search_fields = ('nombre',)


    class Meta:
        model = Marca


admin.site.register(Marca,Marcas)