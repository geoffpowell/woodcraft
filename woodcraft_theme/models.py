# from django.db import models
# from django.utils.translation import ugettext_lazy as _

# from mezzanine.core.fields import FileField
# from mezzanine.core.models import Orderable, SiteRelated
# from mezzanine.pages.models import Page
# from mezzanine.utils.models import upload_to

# class HomePage(Page):
# 		'''
# 		Custom HomePage
# 		'''
# 		welcome_heading = models.CharField( max_length = 45,
# 																				help_text = 'Welcome Heading')
# 		welcome_paragraph = models.CharField( max_length = 450,
# 																					help_text = 'Welcome Paragraph',
# 																					null = True)
# 		class Meta:
# 				verbose_name = _('Home Page')
# 				verbose_name_plural = _('Home Pages')

# class Slide(Orderable):
# 		'''
# 		Slider for the HomePage
# 		'''
# 		homepage = models.ForeignKey( HomePage, related_name='slides' )
# 		image = FileField( verbose_name = _('Image'),
# 											upload_to = ('theme.Slide.Image', 'slider'),
# 											format = 'Image',
# 											max_length = 255, null = True, blank = True)

