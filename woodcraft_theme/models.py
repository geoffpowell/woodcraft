from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField
from mezzanine.core.models import Orderable, SiteRelated
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to

class HomePage(Page):
		'''
		Custom HomePage
		'''
		welcome_heading = models.CharField( max_length = 45,
																				help_text = 'Welcome Heading',
																				default = 'Hello!')
		welcome_paragraph = models.CharField( max_length = 450,
																					help_text = 'Welcome Paragraph',
																					default = 'Welcome, here\'s your first paragraph...')
		class Meta:
				verbose_name = _('Home Page')
				verbose_name_plural = _('Home Pages')

# class Slide(Orderable):
# 		'''
# 		Slider for the HomePage
# 		'''
# 		homepage = models.ForeignKey( HomePage, related_name='slides' )
# 		image = FileField( verbose_name = _('Image'),
# 											upload_to = ('theme.Slide.Image', 'slider'),
# 											format = 'Image',
# 											max_length = 255, null = True, blank = True)

class Feature(Orderable):
		'''
		Featured Products displayed on the HomePage
		'''
		homepage = models.ForeignKey(HomePage, related_name='features')
		image = FileField( verbose_name = _('Image'),
											upload_to = upload_to('theme.Feature.image', 
																						'featured_images'),
											format = 'Image',
											max_length = 255, null = True, blank = True)

		caption_heading = models.CharField (max_length = 60,
																			default = 'Heading for feature')

		caption_blurb = models.CharField (max_length = 100,
																			default = 'Blurb for feature')