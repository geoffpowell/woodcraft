from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import HomePage, Feature
# # , Slide


class FeatureInline(TabularDynamicInlineAdmin):
		model = Feature

class HomePageAdmin(PageAdmin):
		inlines = [FeatureInline]

# # admin.site.register(HomePage, HomePageAdmin)

admin.site.register(HomePage, HomePageAdmin)