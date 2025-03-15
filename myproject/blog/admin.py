from django.contrib import admin
from .models import post, Category, about_us
# Register your models here.


#customizing the admin panel
class postAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    search_fields = ('title','content')
    list_filter = ('category','createdAt')

    def category(self,obj):
        return 


admin.site.register(post,postAdmin)
admin.site.register(Category)
admin.site.register(about_us)