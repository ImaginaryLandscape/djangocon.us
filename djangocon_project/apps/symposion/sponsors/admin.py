from django.contrib import admin

from symposion.sponsors.models import SponsorLevel, Sponsor, SponsorLogo

class SponsorAdmin(admin.ModelAdmin):
    model = SponsorLevel
    list_display = ('name','order')
    list_editable = ('order',)


class SponsorLogoInline(admin.StackedInline):
    model = SponsorLogo
    extra = 1


admin.site.register(SponsorLevel, SponsorAdmin)
admin.site.register(Sponsor,
    inlines = [
        SponsorLogoInline
    ]
)
