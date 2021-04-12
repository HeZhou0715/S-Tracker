from django.core.management.base import BaseCommand

from app.models import Squirrel
import csv

class Command(BaseCommand):
    
    help = 'import data from .csv to the database'
    
    def add_arguments(self, parser):
        parser.add_argument('csv', help = 'the .csv file contains data')
        
    def handle(self, *args, **options):
        with open(options['csv']) as fp:
            data = csv.DictReader(fp)
            
        for i in data:
            s = Squirrel(
                unique_squirrel_id = i['Unique Squirrel ID'],
                X = i['X'],
                Y = i['Y'],
                shift = i['Shift'],
                date = i['Date'],
                age = i['Age'],
                primary_fur_color = i['Primary_Fur_Color'],
                location = i['Location']
                specific_Location = i['Specific Location']
                running = str(i['Running']) == 'TRUE'
                chasing = str(i['Chasing']) == 'TRUE'
                climbing = str(i['Climbing']) == 'TRUE'
                eating = str(i['Eating']) == 'TRUE'
                foraging = str(i['Foraging']) == 'TRUE'
                other_Activity = i['Other Activities']
                kuks = str(i['Kuks']) == 'TRUE'
                quaas = str(i['Quaas']) == 'TRUE'
                moans = str(i['Moans']) == 'TRUE'
                tail_Flags = str(i['Tail flags']) == 'TRUE'
                tail_Twitches = str(i['Tail twitches']) == 'TRUE'
                approaches = str(i['Approaches']) == 'TRUE'
                indifferent = str(i['Indifferent']) == 'TRUE'
                runs_From = str(i['Runs from']) == 'TRUE'
                )
            
            s.save()
            self.stdout.write(self.style.SUCCESS('Added member success!'))
        
        self.stdout.write(self.style.SUCCESS('Successful import all data'))
        
