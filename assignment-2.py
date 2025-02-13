# Write a for loop the prints out all the element between -5 and 5 using the range function.
for i in range(-5,6):
    print(i)
    
    
# Write a for loop that prints out the following list: squares=['red', 'yellow', 'green', 'purple', 'blue']
squares=['red', 'yellow', 'green', 'purple', 'blue']
for item in squares:
    print(item)


# Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. Stop and exit the loop if the value on the list is not 'orange':
list=['orange','orange','banana','pear','lemon']
new_list=[]

for item in list:
    if item == 'orange':
        new_list.append(item)
    else:
        break
print(new_list)   

# Consider the variable d use slicing to print out the first three elements:
d="youssef"
print(d[0:3])

# Print out a backslash ( \ ):
print('\\')
print(s"\")