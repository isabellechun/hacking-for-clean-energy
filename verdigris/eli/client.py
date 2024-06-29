import requests

def get_customers_and_incentives(first_name, last_name, income_level, home_value, mortgage_value, home_age, property_type, zip_code):
    customers_and_incentives = {}
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
    #print(response.text)
    incentives = response.json()['incentives']
    for incentive in incentives:
        benefit_type = incentive['benefit_type']
        if benefit_type == 'no-cost':
            upgrade_measures = incentive['upgrade_measures']
            if not customer_name in customers_and_incentives:
                customers_and_incentives[customer_name] = upgrade_measures
            else:
                customer_upgrade_measures = customers_and_incentives[customer_name]
                customers_and_incentives[customer_name] = customer_upgrade_measures + upgrade_measures
    print(customers_and_incentives)
    #if customer has incentives, pass the first incentive as prompt to open ai. get the image.

get_customers_and_incentives("Tanisha", "Guzman", 3050000, 531541, 531541, 2006, "single_family", "80012")
# for row in csv: get_customers_and_incentives(row[0], ...)
# [John Smith: [], Lucas Ho: []]