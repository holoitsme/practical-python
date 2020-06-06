# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > payment:
	if month >= extra_payment_start_month and month <= extra_payment_end_month:
		principal = principal * (1+rate/12) - payment - extra_payment
		total_paid = total_paid + payment + extra_payment
	else:
		principal = principal * (1+rate/12) - payment
		total_paid = total_paid + payment
	month = month + 1
	print(f'Month: {month}, total paid: ${total_paid:0.2f}, remaining: ${principal:0.2f}')

print(f'Total paid: ${total_paid:0.2f}')
print(f'Months: {month}')
