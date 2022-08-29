class roi():
    def __init__(self, income, expenses, cashflow, roi):
        self.income = income
        self.expenses = expenses
        self.cashflow = cashflow
        self.roi = roi

    def rentalincome(self):
        income = input('How much do you make monthly from the property?')
        print('Your monthly income property is {self.income}')



    def rentalexpenses(self):
        expenses = input('How much are your monthly expenses? (Be sure to include tax, insurance, mortgage, etc)') 
        print('Your monthly expenses are {self.expenses}')

        


    def rentalcashflow(self):
        cashflow = (self.income - self.expenses)
        print('Your cashflow on this property is {self.cashflow}')



    def rentalroi(self):
        totalinvestment = input('What was your total initial investment?')
        roi = (self.cashflow // totalinvestment)

test = roi()


def roirunner():
    while True:
        user_choice = input('Would you like to calculate your return on investment?')
        if user_choice == 'yes':
            test.rentalincome
            test.rentalexpenses
            test.rentalcashflow
            test.rentalroi
            break
            
    
        
        
roirunner()



