def check(value): 
    if value == 0: 
        return 0 
    if value > 0:
        return "positive"
    if value < 0: 
        return "negative"

print(check(-9))
print(check(3))
print(check(0))