#let's code a personal finance tracker with data visualization

import matplotlib.pyplot as plt
import numpy as np  #importing numpy library

#creating a dictionary to store the data
data = { 
        
        'January': 2000,
        'February': 3000,
        'March': 4000,
        'April': 5000,
        'May': 6000,
        'June': 7000,
        'July': 8000,
        'August': 9000,
        'September': 10000,
        'October': 11000,
        'November': 12000,
        'December': 13000
        }

#creating a list to store the months
months = list(data.keys())

#creating a list to store the values
values = list(data.values()) 

#plotting the data
plt.figure(figsize=(10,5))

plt.plot(months, values, color='red', marker='o', linestyle='dashed', linewidth=2, markersize=10)

plt.title('Personal Finance Tracker')
plt.xlabel('Months')
plt.ylabel('Amount in $')
plt.grid(True)
plt.show()

#calculating the total amount
total = sum(values)

print('Total amount:', total)

#calculating the average amount
average = total/len(data)

print('Average amount:', average)

#calculating the maximum amount
maximum = max(values)

print('Maximum amount:', maximum)

#calculating the minimum amount
minimum = min(values)

print('Minimum amount:', minimum)

#calculating the standard deviation
std_dev = np.std(values)

print('Standard deviation:', std_dev)

#calculating the variance
variance = np.var(values)

print('Variance:', variance)