# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from apps.home.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'received_date', 'replied_date', 'reply_subject', 'reply_message']
    search_fields = ['name', 'email', 'message']


admin.site.site_header = "91 IDUM"
admin.site.register(Contact, ContactAdmin)
