from django.contrib import admin

# Register your models here.
admin.site.site_header = "NearFix"
admin.site.site_title = "Nearfix Admin Portal"
admin.site.index_title = "Welcome to Nearfix Administration"

# templates
admin.site.login_template = "admin/login.html"