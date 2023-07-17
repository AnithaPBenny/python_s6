mysum=0
for i in range(5,11,2):
    mysum+=i
    if mysum == 5:
        continue
    mysum+=1
print(mysum)