# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
	total = 0.0
	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			try:
				numshares = int(row[1])
				price = float(row[2])
				total = total + (numshares * price)
			except ValueError:
				print("Couldn't parse", row)
	return total

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'
	
cost = portfolio_cost(filename)
print('Total cost:', round(cost, 2))
