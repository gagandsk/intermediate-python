def sum_with_range(min, max):
    sum = 0
    for x in range(min,max):
        sum += x
    return sum
    
result = sum_with_range(1,10)
result2 = sum_with_range(result,result * 2)
result3 = sum_with_range(result2,result2 * 2)
result4 = sum_with_range(result3,result3 * 2)

print(result)
print(result2)
print(result3)
print(result4)