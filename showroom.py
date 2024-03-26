"""
Problem Statement:
create a class car showroom which has functions has follows:
 1. company it takes one argument which is the car company name and prints welcome to user selected car company.
 2. model according to the car company selected the models of the company will be listed. the user has to select a model from the list.
 3.price based on the car company and model.Calculate the onroad price which is equals to ex showroom price + cgst + sgst + insurance and displaying final price 
"""


class CarShowroom:
    def __init__(self):
        self.company_models = {
            "toyota": ["camry", "corolla", "rav4"],
            "honda": ["accord", "civic", "cr-v"],
            "ford": ["fiesta", "mustang", "escape"],
            "chevrolet": ["malibu", "equinox", "traverse"],
            "hyundai": ["sonata", "santa fe", "tucson"],
            "bmw": ["3 series", "5 series", "x5"]
        }
        self.prices = {
            "toyota": {"camry": 2500000, "corolla": 1800000, "rav4": 2800000},
            "honda": {"accord": 2700000, "civic": 2000000, "cr-v": 3000000},
            "ford": {"fiesta": 1500000, "mustang": 3500000, "escape": 2500000},
            "chevrolet": {"malibu": 2400000, "equinox": 2900000, "traverse": 3500000},
            "hyundai": {"sonata": 2300000, "santa fe": 3200000, "tucson": 2600000},
            "bmw": {"3 series": 4000000, "5 series": 5000000, "x5": 6000000}
        }
        self.cgst = 0.06
        self.sgst = 0.06
        self.insurance_rate = 0.05
    
    def company(self, company_name):
        print("Welcome to", company_name.capitalize(), "Family")
    
    def model(self, company_name):
        print("Models available for", company_name.capitalize(), "are:")
        models = self.company_models.get(company_name.lower(), [])
        attempts = 0
        while True:
            for model in models:
                print(model.capitalize())
            choice = input("Select a model by entering its name: ")
            if choice in models:
                return choice
            else:
                attempts += 1
                print("Invalid choice. Please select a valid model.")
                if attempts >= 5:
                    print("Maximum attempts reached. Exiting...")
                    break
    
    def calculate_price(self, company_name, selected_model):
        ex_showroom_price = self.prices[company_name.lower()][selected_model]
        insurance = ex_showroom_price * self.insurance_rate
        onroad_price = ex_showroom_price + (ex_showroom_price * self.cgst) + (ex_showroom_price * self.sgst) + insurance
        return onroad_price

def main():
    showroom = CarShowroom()
    company_name = input("Enter the car company name: ")
    showroom.company(company_name)
    selected_model = showroom.model(company_name)
    final_price = showroom.calculate_price(company_name, selected_model)
    print("Final onroad price for", selected_model.capitalize(), "is:", final_price)

if __name__ == "__main__":
    main()
