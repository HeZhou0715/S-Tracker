from django.core.management.base import BaseCommand

from app.models import Squirrel
import csv

class Command(BaseCommand):
    
    help = 'export data from the database to .csv'
    
    def add_arguments(self, parser):
        parser.add_argument('csv', help = 'the .csv file to input data')
        
    def handle(self, *args, **options):
        with open(options['csv'], 'w') as fp:
            i = dict()
            s = Squirrel.objects.all()
            k = 0 
            for j in s:
                i['Unique Squirrel ID'] = j.unique_squirrel_id
                i['X'] = j.X
                i['Y'] = j.Y
                i['Shift'] = j.shift
                i['Date'] = j.date
                i['Age'] = j.age
                i['Primary_Fur_Color'] = j.primary_fur_color
                i['Location'] = j.location
                i['Specific Location'] = j.specific_location
                i['Running'] = j.running
                i['Chasing'] = j.chasing
                i['Climbing'] = j.climbing
                i['Eating'] = j.eating
                i['Foraging'] = j.foraging     
                i['Other Activities'] = j.other_activities
                i['Kuks'] = j.kuks
                i['Quaas'] = j.quaas
                i['Moans'] = j.moans
                i['Tail flags'] = j.tail_flags
                i['Tail twitches'] = j.tail_twitches
                i['Approaches'] = j.approaches
                i['Indifferent'] = j.indifferent
                i['Runs from'] = j.runs_from
            
                row = csv.DictWriter(fp, delimiter = ",", fieldnames = i.keys())
                if k == 0:
                    row.writeheader()
                row.writerow(i)
                k += 1
                #self.stdout.write(self.style.SUCCESS('Added member success!'))
        
        self.stdout.write(self.style.SUCCESS('Successful export all data'))
        
