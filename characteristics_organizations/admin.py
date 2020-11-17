from django.contrib import admin
from .models import (CharacteristicsOrganization, HeadByBK, TypeInstitution,
                     TypeOrganization, StatusEGRUL,
                     StatusRYBPNYBP, IndustrySpecificTyping, )


admin.site.register(CharacteristicsOrganization)
admin.site.register(HeadByBK)
admin.site.register(TypeInstitution)
admin.site.register(TypeOrganization)
admin.site.register(StatusEGRUL)
admin.site.register(StatusRYBPNYBP)
admin.site.register(IndustrySpecificTyping)
