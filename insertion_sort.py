numbers = [ 1 , 3 ,5 ,7 ,8 , 9 , 2 , 4 , 6, 0 ]

for j in range(2, len(numbers)):
    key = numbers[j]
    i=j-1
    while i>=0 and numbers[i] > key:
        numbers[i+1] = numbers[i]
        i-= 1
    numbers[i+1] = key
print(numbers)