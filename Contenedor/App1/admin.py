from django.contrib import admin
from .models import AutorDb, FraseDb, ProfesionDb
# Register your models here.


# Para crear frases en Autores

admin.site.site_header = "Administración de tablas"
admin.site.site_title = "Administración de tablas"
admin.site.index_title = "Bienvenido a la administración de tablas"


@admin.register(ProfesionDb)
class ProfesionAdmin(admin.ModelAdmin):
    '''This is the admin for the phrases'''
    list_display = ['nombre']
    fields = ['nombre']


class FrasesInline(admin.TabularInline):
    '''This is the inline for the phrases'''
    model = FraseDb
    extra = 1


class AutorAdmin(admin.ModelAdmin):
    '''This is the admin for the authors'''
    fields = ('nombre', 'fecha_nacimiento', 'profesion',
              'fecha_fallecimiento', 'nacionalidad')
    list_display = ('nombre', 'fecha_nacimiento',
                    'fecha_fallecimiento', 'nacionalidad')
    search_fields = ('nombre', 'profesion', 'nacionalidad')
    # list_filter = ('profesion', 'nacionalidad')
    inlines = [FrasesInline]

    def actulizar_o(self, request, queryset):
        '''This is the action for the admin'''
        for obj in queryset:
            if "A" in obj.nombre:
                nombre_aux = obj.nombre
                obj.nombre = nombre_aux.replace("A", "a")
                obj.save()
        self.message_user(request, "Se han actualizado los nombres")
    actulizar_o.short_description = "Actualizar nombres"

    actions = ['actulizar_o']


admin.site.register(AutorDb, AutorAdmin)


@admin.register(FraseDb)
class FraseAdmin(admin.ModelAdmin):
    '''This is the admin for the phrases'''
    fields = ('cita', 'autor_fk')
    list_display = ('cita', 'autor_fk')
    search_fields = ('cita', 'autor_fk')
    list_filter = ('autor_fk',)
