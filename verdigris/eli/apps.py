from django.apps import AppConfig
from .models import HouseholdInfo
import requests
import csv
import json

class EliConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eli'

class App:
    def read_csv(filename):
        result = []
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    householdInfo = HouseholdInfo.fromRow(row)
                    potentialTargetCustomer = App.get_customers_and_incentives_household_info(householdInfo)
                    if bool(potentialTargetCustomer):
                        print("Potential customer: " + str(householdInfo))
                        result.append(potentialTargetCustomer)
                    line_count += 1
            print(f'Processed {line_count} lines.')
        return result
    
    def writeJson(resultList, filename):
        with open(filename, 'w') as json_file:
            json.dump(resultList, json_file, indent=4)
    
    def get_customers_and_incentives_household_info(hhInfo):
        meta = hhInfo.toDictionary()

        dict = App.get_customers_and_incentives(
            hhInfo.firstName, hhInfo.lastName, int(hhInfo.income), hhInfo.homeValue, hhInfo.mortgageValue, hhInfo.homeAge, hhInfo.propertyType, hhInfo.addressZipCode, meta
        )
        
        return dict

    # Returns dictionary of customer name to object with list of incentive names and metadata
    def get_customers_and_incentives(first_name, last_name, income_level, home_value, mortgage_value, home_age, property_type, zip_code, meta):
        customer_name = first_name + ' ' + last_name
        url = "https://api.eli.build/incentives"
        payload = {
            "address": {
                "zipcode": zip_code
            },
            "property_type": property_type,
            "household_income": income_level,
        }

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": "Bearer raxc4KI9bNXrEkUJgIfv3OIAU1JsoRCKfrgTqwMSKr0Z"
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code != 200:
            print("Failed response {}, {}.".format(response.status_code, response.json()["details"]))
            return {}
        
        final_incentives = set()
        for incentive in response.json()["incentives"]:
            benefit_type = incentive["benefit_type"]
            if benefit_type == 'no-cost':
                final_incentives.add(incentive['upgrade_measures'][0])
        meta["incentives"] = list(final_incentives)
        return meta
    
    #if customer has incentives, pass the first incentive as prompt to open ai. get the image.
 
# get_customers_and_incentives("Tanisha", "Guzman", 3050000, 531541, 531541, 2006, "single_family", "80012")
# for row in csv: get_customers_and_incentives(row[0], ...)
# [John Smith: [], Lucas Ho: []]