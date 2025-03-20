numbers = [ 1 , 3 ,5 ,7 ,8 , 9 , 2 , 4 , 6, 0 ]
for j in range(len(numbers), 0, -1):
    for i in range(j-1):
        if numbers[i]>numbers[i+1]:
           numbers[i] , numbers[i+1] = numbers[i+1] , numbers[i]
            
print(numbers)
    

