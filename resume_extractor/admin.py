from django.contrib import admin
from . import models

admin.site.register(models.ResumeBasicInfoModel)
admin.site.register(models.ResumeEducationInfoModel)
admin.site.register(models.ResumeExperienceInfoModel)
admin.site.register(models.LicenceInfoModel)
admin.site.register(models.AvailableStates)
admin.site.register(models.ActiveInfoModel)
admin.site.register(models.SpecialitiesModel)