from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Vote)
admin.site.register(PollChoice)
admin.site.register(Poll)
admin.site.register(Follow)
admin.site.register(Choice)
