# update O(1)
# Query O(n)

'''

l ~ h 을 업데이트한다면 update 만큼 증가시킨다면 ...
list[l] += update 
list[h+1] -= update

이후 0 ~ h 를 다 더헤서 구할 수 있다.

'''

updateArr = [0] * 10

def update_range(l, h, updateValue):
    updateArr[l] += updateValue
    updateArr[h+1] -= updateValue
    
def getPoint(idx):
    sum = 0
    for i in range(idx+1):
        sum += updateArr[i]
    return sum
