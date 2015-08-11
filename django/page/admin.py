from django.contrib import admin

from models import Event

class EventAdmin(admin.ModelAdmin):
    
    def activate(self, request, queryset):
        rows_updated = queryset.update(active=True)
        
        if rows_updated == 1:
            message_bit = "1 event was"
        else:
            message_bit = "%s event were" % rows_updated
        self.message_user(request, "%s successfully activated." % message_bit)
    
    activate.short_description = "Activate Events"

    actions = [activate]
    list_display = ['event_date','weekday', 'time_range', 'active']    

admin.site.register(Event, EventAdmin)