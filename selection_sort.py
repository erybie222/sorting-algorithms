numbers = [ 1 , 3 ,5 ,7 ,8 , 9 , 2 , 4 , 6, 0 ]
for i in range(len(numbers)-1):
    smallest_index = i
    for j in range(i+1, len(numbers)):
        if numbers[j] < numbers[smallest_index]:
            smallest_index = j
    numbers[i] , numbers[smallest_index] = numbers[smallest_index] , numbers[i]

print(numbers)