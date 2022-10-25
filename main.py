'''IMPORTS'''
from tkinter import *



master = Tk()

'''
e = Entry(master)
ee = Entry(master)


e.pack(side='left')
ee.pack(side='right')

e.focus_set()


def callback():
    print( float(e.get()) * 10) # This is the text you may want to use later

b = Button(master, text = "OK", width = 10, command = callback)
b.pack()


'''

'''ENTRY BOXES'''


E_mortgage_total = Entry(master) #total amount in USD
E_term = Entry(master) #in years
E_interest = Entry(master) #percent
E_federal = Entry(master) #federal tax rate in percent
E_state = Entry(master) #state tax rate in percent

E_location = Entry(master) #state location for average rent
E_bedrooms = Entry(master) #number of bedrooms
#OR
E_estimated_rent = Entry(master)

E_mortgage_total.pack()
E_term.pack()
E_interest.pack()
E_federal.pack()
E_state.pack()
E_location.pack()
E_bedrooms.pack()
E_estimated_rent.pack()

while not E_estimated_rent:
    print('running')

'''CONVERTING TO FLOATS'''

mortgage_total = E_mortgage_total.get()


def callback():
    print(mortgage_total)
    print(type(float(mortgage_total)))# This is the text you may want to use later

b = Button(master, text = "OK", width = 10, command = callback)
b.pack()

'''
mortgage_total = float(mortgage_total)
term = float(E_term.get())
interest = float(E_interest.get())
federal = float(E_federal.get())
state = float(E_state.get())

location = E_location.get()
bedrooms = float(E_bedrooms.get())
#OR
estimated_rent = float(E_estimated_rent.get())




#CALCULATE INTEREST

def calc_interest(loan = mortgage_total):

    total_interest = 0
    monthly_principal = mortgage_total / (term * 12)
    
    month = 0
    annual_interest = []
    
    while loan > 0:
        monthly_interest = loan * (interest / 100)
        total_interest += monthly_interest
    
        loan -= monthly_principal
    
        month += 1
        if month%12 == 0:
            try:
                annual_interest.append(total_interest - annual_interest[-1])
    
            except: annual_interest.append(total_interest)
    return annual_interest, total_interest


#CALCULATE MONTHLY NET
if mortgage_total < 750000:
    annual_interest, total_interest = calc_interest(mortgage_total)

    monthly_interest = total_interest / (term * 12)
    monthly_payment = monthly_principal + monthly_interest
    tax_savings = np.array([annual_interest]) * ((federal + state) / 100)
    
else:
    annual_interest, total_interest = calc_interest(loan = 750000)

    monthly_interest = total_interest / (term * 12)
    monthly_payment = monthly_principal + monthly_interest
    tax_savings = np.array([annual_interest]) * ((federal + state) / 100)
    

if estimated_rent:
    monthly_net = estimated_rent + tax_savings - monthly_payment
    

'''






mainloop()

