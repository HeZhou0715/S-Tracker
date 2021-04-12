from django.core.management.base import BaseCommand
from distutils.util import strtobool
import csv
import datetime

from app.models import Squirrel

class Command(BaseCommand):
    
    help = 'import data from .csv to the database'
    
    def add_arguments(self, parser):
        parser.add_argument('csv', help = 'the .csv file contains data')
        
    def handle(self, *args, **options):
        with open(options['csv']) as fp:
            data = csv.DictReader(fp)
            
            for i in data:
                day = i['Date']
                if day:
                    s_day = day[-4:] + '-' + day[:2] + '-' + day[2:4]
                    d = datetime.datetime.strptime(s_day, '%Y-%m-%d')
                else:
                    d = None

                s = Squirrel(
                    unique_squirrel_id = i['Unique Squirrel ID'],
                    X = i['X'],
                    Y = i['Y'],
                    shift = i['Shift'],
                    date = d,
                    age = i['Age'],
                    primary_fur_color = i['Primary Fur Color'],
                    location = i['Location'],
                    specific_location = i['Specific Location'],
                    running = strtobool(i['Running']),
                    chasing = strtobool(i['Chasing']),
                    climbing = strtobool(i['Climbing']),
                    eating = strtobool(i['Eating']),
                    foraging = strtobool(i['Foraging']),
                    other_activities = i['Other Activities'],
                    kuks = strtobool(i['Kuks']),
                    quaas = strtobool(i['Quaas']),
                    moans = strtobool(i['Moans']),
                    tail_flags = strtobool(i['Tail flags']),
                    tail_twitches = strtobool(i['Tail twitches']),
                    approaches = strtobool(i['Approaches']),
                    indifferent = strtobool(i['Indifferent']),
                    runs_from = strtobool(i['Runs from']),
                    )
            
                s.save()
                #self.stdout.write(self.style.SUCCESS('Added member success!'))
        
        self.stdout.write(self.style.SUCCESS('Successful import all data'))
        
