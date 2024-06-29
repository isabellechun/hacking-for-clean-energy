from django.apps import AppConfig
from .models import HouseholdInfo
import csv

class EliConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eli'

class App:
    def read_csv(filename):
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    x = HouseholdInfo.fromRow(row)
                    if line_count % 20 == 0:
                        print(x)
                    line_count += 1
            print(f'Processed {line_count} lines.')
