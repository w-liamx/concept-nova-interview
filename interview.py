a = [2, 3, 1, 19, 18, 12, 7, 18, 22, 32, 20, 11, 8, 5]

def checkTrend(a):
    uptrend = []
    downtrend = []
    returned = {"uptrend": False, "downtrend": False, "index": None}
    index = None
    up_idx = None
    up_count = 0
    down_idx = None
    down_count = 0
    for idx, value in enumerate(a):
        if idx == 0:
            uptrend.append(0)
            downtrend.append(0)
        else:
            if value > (a[idx - 1]):
                uptrend.append(idx)
                downtrend.clear()
            else:
                downtrend.append(idx)
                uptrend.clear()
        if len(uptrend) == 3 or len(downtrend) == 3 :
            if len(uptrend) == 3:
                index = uptrend[0]
            if len(downtrend) == 3:
                index = downtrend[0]
            break
    returned['uptrend'] = len(uptrend) == 3
    returned['downtrend'] = len(downtrend) == 3
    returned['index'] = index
    return returned
    



print(checkTrend(a))      
