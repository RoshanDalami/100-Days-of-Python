is_on = True
collection = []
while(is_on):
    number = float(input("Enter the number (negative number to quite): "))
    
    if(number < 0):
        is_on = False
    else:
        collection.append(number)


smallest = collection[0]
for i in range(0,len(collection)):
    if(smallest > collection[i]):
        smallest = collection[i]
print(f"smallest non-negative value is : {smallest}")       
