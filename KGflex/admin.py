from django.contrib import admin
from KGflex.models import KGflex, Notice, KDrama, entertainment, KMovie, UMovie
# Register your models here.
admin.site.register(KGflex)
admin.site.register(Notice)
admin.site.register(KDrama)
admin.site.register(KMovie)
admin.site.register(UMovie)
admin.site.register(entertainment)