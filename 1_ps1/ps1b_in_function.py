def part_b(annual_salary, percent_saved, total_cost_of_home, semi_annual_raise):
	#########################################################################
	percent_down_payment = 0.12
	r = 0.06
	amount_saved=0
	months=0
	need = total_cost_of_home*percent_down_payment
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ##
	###############################################################################################
	while amount_saved <= need:
	    amount_saved += annual_salary/12*percent_saved + amount_saved*(r/12)
	    if months % 6 == 0 and months != 0:
	        annual_salary += annual_salary*semi_annual_raise
	    months += 1
	
	print(f'Number of months: {months}')
	return months