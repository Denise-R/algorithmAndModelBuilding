# where upper is ideal
def idealU(lower, upper, x):
    changeRate = (upper - lower) / 3
    rangeList = [upper]
    for i in range(3):
        value = rangeList[i] - changeRate
        rangeList.append(value)
        # print(rangeList)
    if x > rangeList[0] or x == rangeList[0]:
        return 5
    elif x > rangeList[1] or x == rangeList[1]:
        return 4
    elif x > rangeList[2] or x == rangeList[2]:
        return 3
    elif x > rangeList[3] or x == rangeList[3]:
        return 2
    else:
        return 1


# where lower is ideal
def idealL(lower, upper, x):
    changeRate = (lower - upper) / 3
    rangeList = [lower]
    for i in range(3):
        value = rangeList[i] - changeRate
        rangeList.append(value)
        # print(rangeList)
    if x < rangeList[0] or x == rangeList[0]:
        return 5
    elif x < rangeList[1] or x == rangeList[1]:
        return 4
    elif x < rangeList[2] or x == rangeList[2]:
        return 3
    elif x < rangeList[3] or x == rangeList[3]:
        return 2
    else:
        return 1



# where middle is ideal
def idealM(lower, upper,x):
    mid = (upper - lower) / 2
    changeRate = mid / 4
    rangeList = [mid - changeRate]
    rangeList2 = [mid + changeRate]
    for i in range(3):
        value1 = rangeList[i] - changeRate
        rangeList.append(value1)
        # print(rangeList)
        value1 = rangeList2[i] + changeRate
        rangeList2.append(value1)
        # print(rangeList2)
    if x < rangeList2[0] and x > rangeList[0] or x == rangeList[0] or x == rangeList2[0]:
        return 5
    elif x < rangeList2[1] and x > rangeList[1] or x == rangeList[1] or x == rangeList2[1]:
        return 4
    elif x < rangeList2[2] and x > rangeList[2] or x == rangeList[2] or x == rangeList2[2]:
        return 3
    elif x < rangeList2[3] and x > rangeList[3] or x == rangeList[3] or x == rangeList2[3]:
        return 2
    else:
        return 1



print(idealL(5, 20, 17))
print(idealU(35, 100, 35.7))
print(idealM(0, 20, 16))

def location(x):
    rating = idealL(5, 20, x)
    return rating * 5
    # 5 is the weight

def pay(x):
    rating = idealU(35, 100, x)
    return rating * 2

def remoteWork(x):
    rating = idealM(0, 20, x)
    return rating * 1

def perfectJob():
    x = location(5) + pay(100) + remoteWork(10)
    return x

def score(locationX, payX, remoteWorkX):
    score = location(locationX) + pay(payX) + remoteWork(remoteWorkX)
    # must be 80% match
    x = perfectJob() * 0.8
    if score > x or score == x:
        print("The job had a score of " + str(score) + ", you will see the posting")
    else:
        print("The job had a score of " + str(score) + ", you will not see the posting")


"""For a job that is 
    1. located 17 miles away
    2. pays 35.7K/year
    3. has an average of 16 hrs/week of remote work"""
score(17, 35.7, 16)
print(perfectJob())
