# Question 1 
# The most suprising thing is how easy they make it to store information, and how attainable it becomes once the information is a list.

# Question 2
# One business thing that could be stored is customer orders, so instead of manually entering evrything in excel, I could make the list and solve everything else from there.

# -- Exercise 1 --

# Creating the inventory list
inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)

count = len(inventory)
print(count)


# -- Exercise 2 --

print(inventory[0])

print(inventory[-1])

# Finding and printing the middle item
middle = len(inventory) // 2
print(inventory[middle])


# -- Exercise 3 --

# Printing the first three items
print(inventory[:3])

# Printing the last two items
print(inventory[-2:])

# Printing every other item
print(inventory[::2])


# -- Exercise 4 --

# Adding envelope to the list
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

# Sorting the list alphabetically
inventory.sort()
print(inventory)


# -- Exercise 5 --

coords = (40.7128, -74.0060)

# Trying to change the first coordinate
try:
    coords[0] = 99

except TypeError:
    print("Tuples cannot be changed after they are created. They are useful for coordinates.")

# Printing the original coordinates
print(coords)


# -- Exercise 6 --

sales = [100, 250, 75, 480, 200]

# Calculating the total sales
total = sum(sales)
print(f"Total: {total}")

# Counting the number of sales
count = len(sales)
print(f"Count: {count}")

# Calculating the average sales
average = total / count
print(f"Average: {average}")

best = max(sales)
worst = min(sales)

print(f"Best: {best}")
print(f"Worst: {worst}")


# -- Exercise 7 --

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

# Creating an empty discounted list
discounted = []

# Applying a 10% discount to each price
for price in prices:
    new_price = price * 0.90
    discounted.append(round(new_price, 2))

# Printing the original and discounted lists
print(prices)
print(discounted)


# -- Exercise 8 --

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

# Creating an empty list for high sales
high_sales = []

# Finding sales greater than 300
for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)

# Counting the high sales days
count = len(high_sales)
print(f"Count: {count}")

# Calculating the average of high sales
total = sum(high_sales)
average = total / count

print(f"Average: {average:.2f}")
