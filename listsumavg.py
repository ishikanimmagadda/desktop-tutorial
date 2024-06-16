def listsumavg (lstNums): 
    totalSum = 0 
    length = len(lstNums)
    for i in range(length):
        totalSum = totalSum + lstNums[i]
    
    average = totalSum / length
    
    return (totalSum, average)

print(listsumavg([2,3,4,6,4,3]))
print(listsumavg([20,30,43,54]))