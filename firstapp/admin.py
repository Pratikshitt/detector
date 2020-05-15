from django.contrib import admin

# Register your models here.

from firstapp.models import topic,webpage,ModelForm,MyModel,GeneralRemedies,AuyervedicRemedies,HomeopathicRemedies,ip

admin.site.register(topic)
admin.site.register(webpage)
admin.site.register(ModelForm)
admin.site.register(MyModel)
admin.site.register(GeneralRemedies)
admin.site.register(AuyervedicRemedies)
admin.site.register(HomeopathicRemedies)
admin.site.register(ip)
