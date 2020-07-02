'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''

import csv

# specify that the delimiter is a tab character
# make sure that the path in Spyder (top right hand corner) is set to to dataset folder
with open('chipotle.tsv', 'rU') as f:
    data = [row for row in csv.reader(f, delimiter='\t')]

'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''
header=data[0]
data_file=data[1:]
'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''


price =[]
order_list = []
for orders in range(len(data_file)):
    order_list.append(orders)
    
    




































price_column=[]
price=[]
for order in range(len(data_file)):
    orders_order=data_file[order]
    for cost in orders_order:
        if '$' in cost:
            price_column.append(cost)
for money in range(len(price_column)):
    price.append(float(price_column[money].strip('$')))
    
print('$',sum(price))
'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''
sodas=[]
orders_with_soda=[]
for soda_order in range(len(data_file)):
    soda_orders=data_file[soda_order]
    for part in soda_orders:
        if 'Canned Soda' in part:
            orders_with_soda.append(soda_orders)
        elif 'Canned Soft Drink' in soda_orders:
            orders_with_soda.append(soda_orders)
        else:
            pass
for fizzy in range(len(orders_with_soda)):
    drinks_fizzy=orders_with_soda[fizzy]
    for brand in drinks_fizzy:
        if "[" in brand:
            sodas.append(brand)
print(set(sodas))    
    

'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''
orders_with_toppings=[]

for owt in range(len(data_file)):
    toppings=data_file[owt]
    for tops in toppings:
        if 'Bowl' in tops:
            orders_with_toppings.append(tops)
        elif 'Tacos' in tops:
            orders_with_toppings.append(tops)
        elif 'Burritos' in tops:
            orders_with_toppings.append(tops)
        else:
            pass
            
'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''


'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''
