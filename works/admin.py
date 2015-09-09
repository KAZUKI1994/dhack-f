from django.contrib import admin

from .models import Works
# Register your models here.

'''
class WorksAdmin(admin.ModelAdmin):
	fields = [
		(None, {'fields' : ['title']}),
		(u'投稿者', {'fields' : ['publisher'], ['pub_phone'], ['pub_mail']}),
		(u'募集案件', {'fields' : ['content'], ['condition']}),
		(u'場所', {'fields' : ['canvas'], ['location']}),
		(u'期間', {'fields' : ['work_start'], ['work_finish']}),
		(u'報酬', {'fields' : ['money_kind'], ['money_amount']}),
	]
'''
admin.site.register(Works)