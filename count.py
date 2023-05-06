list1 = [21,3
         ,4,6,33,2,3,1,5,75]
even_count, odd_count = 0 , 0
# enhanced for loop
for num in list1:
    # even numbers
    if num % 2 == 0:
        even_count += 1
        #odd numbers
    else:
        odd_count += 1
        print("Even numbers available in the list:", even_count)
        print("odd numbers available in the list:", odd_count)
