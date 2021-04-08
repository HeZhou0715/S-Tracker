from django.db import models

from django.utils.translation import gettext as _




class Squirrel(models.Model):


    unique_squirrel_id = models.CharField(
        max_length=100,
        help_text=_('Unique id of squirrel'),
        primary_key=True,
    )

    X = models.FloatField(
        max_length=100,
        help_text=_('Latitude'),
        default=None,
    )

    Y = models.FloatField(
        max_length=100,
        help_text=_('Longitude'),
        default=None,
    )
    
    PM = 'PM'
    AM = 'AM'

    SHIFT_CHOICES = [
        (PM, _('PM')),
        (AM, _('AM')),
    ]

    shift = models.CharField(
        max_length=2,
        help_text=_('Occur before or after noon'),
        choices=SHIFT_CHOICES,
    )

    date = models.DateField(
        help_text=_('Occur Date'),
        blank=True,
        default=None,
    )
    
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE_CHOICES = [
        (ADULT, _('Adult')),
        (JUVENILE, _('Juvenile')),
    ]

    age = models.CharField(
        max_length=10,
        help_text=_('Age of squirrel_Adult or Juvenile'),
        blank=True,
        choices=AGE_CHOICES,
    )
    
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    
    PRIMARY_FUR_COLOR_CHOICES = [
        (GRAY, _('Gray')),
        (CINNAMON, _('Cinnamon')),
        (BLACK, _('Black')),
    ]
    
    primary_fur_color = models.CharField(
        max_length=15,
        help_text=_('Choose the primary fur color for the squirrel'),
        choices=PRIMARY_FUR_COLOR_CHOICES,
        blank=True,
    )
    
    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    
    LOCATION_CHOICES = [
        (GROUND_PLANE, _('Ground Plane')),
        (ABOVE_GROUND, _('Above Ground')),
    ]
    
    location = models.CharField(
        max_length=30,
        help_text=_('Location of squirrel, choose from options'),
        choices=LOCATION_CHOICES,
    )
    
    specific_location = models.TextField(
        blank=True,
        help_text=_('Additional location information'),
    )
    
    running = models.BooleanField(
        help_text=_('Is squirrel seen running'),
        default=False,
    )
    
    chasing = models.BooleanField(
        help_text=_('Is squirrel seen chasing'),
        default=False,
    )
    
    climbing = models.BooleanField(
        help_text=_('Is squirrel seen climbing'),
        default=False,
    )
    
    eating = models.BooleanField(
        help_text=_('Is squirrel seen eating'),
        default=False,
    )
    
    foraging = models.BooleanField(
        help_text=_('Is squirrel seen foraging'),
        default=False,
    )
    
    other_activities = models.TextField(
        blank=True,
        help_text=_('Additional activities information'),
    )
    
    kuks = models.BooleanField(
        help_text=_('Is squirrel seen kuks'),
        default=False,
    )
    
    quaas = models.BooleanField(
        help_text=_('Is squirrel seen quaas'),
        default=False,
    )
    
    moans = models.BooleanField(
        help_text=_('Is squirrel seen moans'),
        default=False,
    )
    
    tail_flags = models.BooleanField(
        help_text=_('Is squirrel flaging tail'),
        default=False,
    )
    
    tail_twitches = models.BooleanField(
        help_text=_('Is squirrel twitching tail'),
        default=False,
    )
    
    approaches = models.BooleanField(
        help_text=_('Is squirrel approaching human'),
        default=False,
    )
    
    indifferent = models.BooleanField(
        help_text=_('Is squirrel indifferent with human'),
        default=False,
    )
    
    runs_from = models.BooleanField(
        help_text=_('Is squirrel avoiding human'),
        default=False,
    )
    
    def __str__(self):
        return self.unique_squirrel_id
    
    
