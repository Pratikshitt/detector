from django.contrib import admin

# Register your models here.

from firstapp.models import topic,webpage,ModelForm,MyModel,GeneralRemedies,AuyervedicRemedies

admin.site.register(topic)
admin.site.register(webpage)
admin.site.register(ModelForm)
admin.site.register(MyModel)
admin.site.register(GeneralRemedies)
admin.site.register(AuyervedicRemedies)
