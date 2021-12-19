#exercise 3
numList = []
while True :
    num = input("Enter any interger or 'done to stop! ")
    if num == "done":
        break
    else:
        try:
            num = int(num)
            numList.append(num)
        except:
            print("Invalid Input")

#smallest
smallest = None
for n in numList:
    if smallest is None:
        smallest = n
    elif n < smallest:
        smallest = n
print("Minimum", smallest) 

#largest
largest = None
for n in numList:
    if largest is None:
        largest = n
    elif n > largest:
        largest = n
print("Maximum",largest)
    
    
    
