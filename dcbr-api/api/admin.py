from django.contrib import admin
from api.models import (
    Operator,
    Address,
    Inspection,
    Risk_Factor_Operation,
    Risk_Factor_Animal,
    Association_Membership,
)

admin.site.register(Operator)
admin.site.register(Address)
admin.site.register(Inspection)
admin.site.register(Risk_Factor_Operation)
admin.site.register(Risk_Factor_Animal)
admin.site.register(Association_Membership)
