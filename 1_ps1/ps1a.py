## 6.100A Pset 1: Part a
## Name: Rafael Moreno Ribeiro
## Time Spent:
## Collaborators: None

##################################################################################
## Get user input for annual_salary, percent_saved and total_cost_of_home below ##
##################################################################################
annual_salary=float(input("What is your annual salary? "))
percent_saved=float(input("What percentage of your salary do you wish to save? "))
total_cost_of_home=float(input("How much does your dream home cost? "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
percent_down_payment = 0.12
r = 0.06
amount_saved=0
months=0
need = total_cost_of_home*percent_down_payment

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ##
###############################################################################################
while 0 == 0:
    if amount_saved > need:
        break
    amount_saved += annual_salary/12*percent_saved + amount_saved*(r/12)
    months += 1

print(f'Number of months: {months}')
