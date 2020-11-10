from django.contrib import admin
from .models import (CharacteristicsOrganization, HeadByBK, TypeInstitutions,
                     TypeOrganizations, StatusEGRUL,
                     StatusRYBPNYBP, IndustrySpecificTyping, BudgetLevel)


admin.site.register(CharacteristicsOrganization)
admin.site.register(HeadByBK)
admin.site.register(TypeInstitutions)
admin.site.register(TypeOrganizations)
admin.site.register(StatusEGRUL)
admin.site.register(StatusRYBPNYBP)
admin.site.register(IndustrySpecificTyping)
