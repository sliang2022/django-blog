from django.contrib import admin

# Register your models here.
# a new import
from polling.models import Poll

# and a new admin registration
admin.site.register(Poll)