a = [2, 3, 1, 19, 18, 12, 7, 18, 22, 32, 20, 11, 8, 5]
b = [32, 12, 11, 21, 5, 10, 11, 18, 5, 2]
c = [32, 12, 15, 11, 22, 11, 18, 18, 15, 7]

def checkTrend(a):
    uptrend = []
    downtrend = []
    index = -1
    returned = {"uptrend": False, "downtrend": False, "index": -1}
    for idx, value in enumerate(a):
        if value > (a[idx - 1]):
            uptrend.append(idx - 1)
            downtrend.clear()
        else:
            downtrend.append(idx - 1)
            uptrend.clear()

        if len(uptrend) == 3 or len(downtrend) == 3 :
            if len(uptrend) == 3:
                index = uptrend[0]
            if len(downtrend) == 3:
                index = downtrend[0]
            break
    returned['uptrend'] = up_count == 3
    returned['downtrend'] = down_count == 3
    returned['index'] = index
    return returned
    



print(checkTrend(a))      
print(checkTrend(b))      
print(checkTrend(c)) 
