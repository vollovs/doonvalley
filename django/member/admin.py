from django.contrib import admin

from models import Member, MemberHistory
from datetime import datetime


class MemberAdmin(admin.ModelAdmin):
    
    def is_enrolled(self, member, year):
        mun_of_match = MemberHistory.objects.filter(member=member, year=year).count()
        return mun_of_match > 0
    
    def member_enroll(self, request, queryset):
        #queryset.update(status='p')
        #selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        #ct = ContentType.objects.get_for_model(queryset.model)
        
        rows_updated = 0
        for member in queryset:
            year = datetime.now().year
            if not self.is_enrolled(member, year):
                memberHistory = MemberHistory(member=member, year=year)
                memberHistory.save()
                rows_updated += 1
            else:
                print 'member name={0}, year={1} already enrolled.'.format(member, year)
        
        if rows_updated == 1:
            message_bit = "1 member was"
        else:
            message_bit = "%s members were" % rows_updated
        self.message_user(request, "%s successfully enrolled." % message_bit)
    
    member_enroll.short_description = "Enroll member"

    actions = [member_enroll]
    list_display = ['club','chinese_name','english_name', 'email', 'phone','created','active']    
    list_filter = ['club']
    
class MemberHistoryAdmin(admin.ModelAdmin):
    
    def get_chinese_name(self, obj):
        return obj.member.chinese_name
    
    list_display = ['get_chinese_name','year']
    list_filter = ['year']   
        
admin.site.register(Member, MemberAdmin)
admin.site.register(MemberHistory, MemberHistoryAdmin)