class Income:
    def __init__(self, monthly_rental, laundry, storage, misc):
        self.monthly_rental = monthly_rental or 0
        self.storage = storage or 0
        self.laundry = laundry or 0
        self.misc = misc or 0

    def calc(self):
        return self.monthly_rental + self.storage + self.laundry + self.misc

class Expense:
    def __init__ (self, tax_expense, insurance, electricity, water, sewer, garbage, gas, hoa, lawn_care, snow, vacancy, repairs, capex, pm, mortgage):
        self.tax_expense = tax_expense or 0
        self.insurance = insurance or 0
        self.electricity = electricity or 0
        self.water = water or 0
        self.sewer = sewer or 0
        self.garbage = garbage or 0
        self.gas = gas or 0
        self.hoa = hoa or 0
        self.lawn_care = lawn_care or 0
        self.snow = snow or 0
        self.vacancy = vacancy or 0
        self.repairs = repairs or 0
        self.capex = capex or 0
        self.pm = pm or 0
        self.mortgage = mortgage or 0
        
    def calc(self):
        return self.tax_expense + self.insurance + self.electricity + self.water + self.sewer + self.garbage + self.gas + self.hoa + self.lawn_care + self.snow + self.vacancy + self.repairs + self.capex + self.pm + self.mortgage


monthly_rental = input("How much monthly rental income?")
has_slm = input("Do you have any laundry storage or misc?" "Yay or Nay?")
if has_slm:
    storage = input("What is your monthly storage income??")
    laundry = input("What is your monthly laundry??")
    misc = input("What is your monthly misc??")

print("------------")
print ("Lets look at your expenses!!!!!")
tax_expense = input("What is your monthly tax expense?")
insurance = input("What is your monthly insurance?")
has_utility = input("Do you have any utility expenses?")
if has_utility:
    electricity = input("What is your monthly electricity?")
    water = input("What is your monthly water?")
    sewer = input("What is your monthly sewer?")
    garbage = input("What is your monthly garbage?")
    gas = input("What is your monthly gas?")
hoa = input("What is your monthly hoa?")
has_sl = input("Do you have snow or lawn care?")
if has_sl:
    lawn_care = input("What is your monthly lawn_care?")
    snow = input("What is your monthly snow?")
vacancy = input("What is your monthly vacancy?")
repairs = input("What is your monthly repairs?")
capex = input("What is your monthly capital expenditure?")
pm = input("What is your monthly project management fee?")
mortgage = input("What is your monthly mortgage?")

income = Income(monthly_rental, laundry, storage, misc)
expense = Expense(tax_expense, insurance, electricity, water, sewer, garbage, gas, hoa, lawn_care, snow, vacancy, repairs, capex, pm, mortgage)
print("Your monthly income is " + income.calc())
print("Your monthly expense is " + expense.calc())