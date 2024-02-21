## 6.100A Pset 1: Part c
## Name: Rafael Moreno Ribeiro
## Time Spent: 1 hour
## Collaborators: Ketevan Tsimakuridze

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit=float(input("What is your initial deposit? "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
#Setting up for a binary search:
down_payment=800000*0.12
high=1
low=0
r=(high+low)/2
months=36
steps=0
#Setting up the equation for amount saved as a function of months
amount_saved=initial_deposit*(1+r/12)**months

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
#If the initial deposit is already close enough, then there's no need for any interest rate, so r=0
if initial_deposit > down_payment - 100:
    r=0.0
    steps=0
#If it's not possible to ever reach the down payment, there isn't a valid interest rate that leads us to our goal, so r=None
elif initial_deposit*(1+1/12)**months < down_payment - 100:
    r=None
    steps=0
#Else, binary searching will help us find the interest rate value. Setting the loop up:
else :
    while abs(amount_saved - down_payment) > 100:
        if amount_saved < down_payment:
            low = r
        else:
            high = r
        r=(high+low)/2
        amount_saved=initial_deposit*(1+r/12)**months
        steps += 1

print(f'Best savings rate: {r}')
print(f'Steps in bisection search: {steps}')
