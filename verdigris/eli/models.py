from django.db import models

import json

class HouseholdInfo:
    # addressStreet, addressCity, addressState,
    def __init__(self, firstName, lastName, income, homeValue, mortgageValue, homeAge, addressZipCode, propertyType):
        self.firstName = firstName
        self.lastName = lastName
        self.income = income # int
        self.homeValue = homeValue,
        self.mortgageValue = mortgageValue,
        self.homeAge = homeAge,
        # self.addressStreet = addressStreet # String "123 Bush St"
        # self.addressCity = addressCity
        # self.addressState = addressState
        self.addressZipCode = addressZipCode # "94117"
        self.propertyType = propertyType # "single_family", "multifamily", "commercial"

    def __str__(self):
        return "Household for {} {} in {}. Property type: {}.".format(
            self.firstName, self.lastName, self.addressZipCode, self.propertyType
        )

    def fromRow(row):
        return HouseholdInfo(
            firstName=row[0],
            lastName=row[1],
            income=row[2],
            homeValue=row[3],
            mortgageValue=row[4],
            homeAge=row[5],
            propertyType=row[6],
            addressZipCode=row[7],
        )

class ApiResult:
    def __init__(self, firstName, lastName, incentives):
        self.firstName = firstName
        self.lastName = lastName
        self.incentives = incentives

class Incentive:
    def __init__(self, id, name, benefit_type, upgrade_measures):
        self.id = id
        self.name = name
        self.benefit_type = benefit_type
        self.upgrade_measures = upgrade_measures

class Program:
    def __init__(self, name, url):
        self.name = name
        self.url = url

class OutputFile:
    def __init__(self):
        self.people = []

    def addPerson(self, person):
        self.people.append(person)

    def toJson(self):
        return json.dumps(self.__dict__)