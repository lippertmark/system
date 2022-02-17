from django.contrib import admin
from .models import Goods, Question, Form, Profile
# Register your models here.

admin.site.register(Goods)
admin.site.register(Question)
admin.site.register(Form)
admin.site.register(Profile)