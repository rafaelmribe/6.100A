def part_a(annual_salary, percent_saved, total_cost_of_home):
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
	return months