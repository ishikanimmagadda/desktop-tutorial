def factorial(number): 
    i = number 
    final = 1
    while i > 0: 
        final = final * i 
        i = i - 1
    return final 

print(factorial(5))
print(factorial(20))