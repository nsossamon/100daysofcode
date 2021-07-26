# Lists are a data structure, or a way of organizing and storing data
# Separated by a bracket, and can store multiple data types (strings, integers, etc.):
fruits = ["Apple", "Cherry", "Grapes"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)

# Ordering of items in your list can be referenced later in your code and is called indexing, based on offset:
print(fruits[0])

# Starting at zero is common in code, is called an "offset" as the first item is at 0 offset, and you go from there
# Offset can also be negative, e.g. [-1] would start at the end of a list
print(fruits[-1])

# Offset can be used to change or add a piece of data in a list as well:
fruits[0] = "Cranberry"
fruits.append("Kiwi")
print(fruits)

# Nested lists are two lists described by one variable:

vegetables = ["Kale", "Broccoli"]

food = [fruits, vegetables]
print(food)

# output = [['Cranberry', 'Cherry', 'Grapes', 'Kiwi'], ['Kale', 'Broccoli']]

print(food[1][1])


