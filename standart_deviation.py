import pandas
import plotly.express as px
import csv 
import math

with open('csvfiles/data.csv', newline = '') as f:
	reader = csv.reader(f)
	filedata = list(reader)

data = filedata[0]
total = 0
mean = 0
number_of_instances = len(data)
squared_list = []
summed_value = 0
divisor = number_of_instances - 1
divided_value = 0
standard_deviation = 0


for number in data:
	total += int(number)

mean = total/number_of_instances

for number in data:
	subtracted_value = float(number) - mean
	squared_value = subtracted_value**2

	squared_list.append(squared_value)

for number in squared_list:
	summed_value += number

divided_value = summed_value/divisor

standard_deviation = math.sqrt(divided_value)
print(standard_deviation)