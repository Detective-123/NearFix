from django.contrib import admin


# Register your models here.
admin.site.site_header = "NearFix"
admin.site.site_title = "Nearfix Admin Portal"
admin.site.index_title = "Welcome to Nearfix Administration"

# templates
admin.site.login_template = "admin/login.html"
from .models import userprofile
@admin.register(userprofile)
class userprofileAdmin(admin.ModelAdmin):
    list_display = ("phone", "full_name", "email", "created_at")  # columns to show
    search_fields = ("phone", "full_name", "email")  # search bar
    list_filter = ("created_at",)  # filter options