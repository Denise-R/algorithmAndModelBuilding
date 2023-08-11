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
# where the ideal value is not the middle
def idealW(lower, upper, ideal, x):
    right = (upper - ideal) / 4
    left = (ideal - lower) / 4
    rangeListR = [(ideal + right)]
    for i in range(3):
        value = rangeListR[i] + right
        rangeListR.append(value)
        print(rangeListR)
    rangeListL = [(ideal - left)]
    for i in range(3):
        value = rangeListL[i] - left
        rangeListL.append(value)
        print(rangeListL)
    if x > rangeListL[0] and x < rangeListR[0] or x == rangeListR[0] or x == rangeListL[0]:
        return 5
    elif x > rangeListL[1] and x < rangeListL[0] or x == rangeListL[1] or x == rangeListR[1] or rangeListR[0] < x < \
            rangeListR[1]:
        return 4
    elif x > rangeListL[2] and x < rangeListL[1] or x == rangeListL[2] or x == rangeListR[2] or rangeListR[1] < x < \
            rangeListR[2]:
        return 3
    elif x > rangeListL[3] and x < rangeListL[2] or x == rangeListL[3] or x == rangeListR[3] or rangeListR[2] < x < \
            rangeListR[3]:
        return 2
    else:
        return 1
def pay(x):
    rating = idealU(1, 5, x)
    return rating * 2
def weekend(x):
    rating = idealU(1, 5, x)
    return rating * 2
def location(x):
    rating = idealL(5, 20, x)
    return rating * 5
    # 5 is the weight
def hours(x):
    rating = idealU(1, 5, x)
    return rating * 2
def shift(x):
    rating = idealU(1, 5, x)
    return rating * 2
def hybrid(x):
    rating = idealM(0, 20, x)
    return rating * 1
def travel(x):
    rating = idealU(1, 5, x)
    return rating * 2
def negotiation(x):
    rating = idealU(1, 5, x)
    return rating * 2
def osha(x):
    rating = idealU(1, 5, x)
    return rating * 2
def reviews(x):
    rating = idealU(1, 5, x)
    return rating * 2
def managmentStyle(x):
    rating = idealU(1, 5, x)
    return rating * 2
def workStress(x):
    rating = idealU(1, 5, x)
    return rating * 2
def benifits(x):
    rating = idealU(1, 5, x)
    return rating * 2
def retension(x):
    rating = idealU(1, 5, x)
    return rating * 2
def educationAndTraining(x):
    rating = idealU(1, 5, x)
    return rating * 2
def strengthWeakness(x):
    rating = idealU(1, 5, x)
    return rating * 2
def pastWork(x):
    rating = idealU(1, 5, x)
    return rating * 2
def advancement(x):
    rating = idealU(1, 5, x)
    return rating * 2
def techniqualSkills(x):
    rating = idealU(1, 5, x)
    return rating * 2
def vacationTime(x):
    rating = idealU(1, 5, x)
    return rating * 2
def PoliticalAffiliation(x):
    rating = idealU(1, 5, x)
    return rating * 2
def PoliticalInvolvement(x):
    rating = idealU(1, 5, x)
    return rating * 2
def amentities(x):
    rating = idealU(1, 5, x)
    return rating * 2
def m_e_ratio(x):
    rating = idealU(1, 5, x)
    return rating * 2
def softSkills(x):
    rating = idealU(1, 5, x)
    return rating * 2
def flexibleSchedule(x):
    rating = idealU(1, 5, x)
    return rating * 2
def CommunityInvolement(x):
    rating = idealU(1, 5, x)
    return rating * 2
def ManegementLevels(x):
    rating = idealU(1, 5, x)
    return rating * 2
def groupSize(x):
    rating = idealU(1, 5, x)
    return rating * 2
def workspace(x):
    rating = idealU(1, 5, x)
    return rating * 2
def socialOutings(x):
    rating = idealU(1, 5, x)
    return rating * 2
def HQLocation(x):
    rating = idealU(1, 5, x)
    return rating * 2
def dress(x):
    rating = idealU(1, 5, x)
    return rating * 2
def screenTime(x):
    rating = idealU(1, 5, x)
    return rating * 2
def coffee(x):
    rating = idealU(1, 5, x)
    return rating * 2
def lunch(x):
    rating = idealU(1, 5, x)
    return rating * 2
def coAge(x):
    rating = idealU(1, 5, x)
    return rating * 2


def allFactors(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll):
    all = pay(a)+weekend(b)+location(c)+hours(d)+shift(e)+hybrid(f)+travel(g)+negotiation(h)+osha(i)+reviews(j)+\
          managmentStyle(k)+workStress(l)+benifits(m)+retension(n)+educationAndTraining(o)+strengthWeakness(p)+\
          pastWork(q)+advancement(r)+techniqualSkills(s)+vacationTime(t)+PoliticalAffiliation(u)+\
          PoliticalInvolvement(v)+amentities(x)+m_e_ratio(y)+softSkills(z)+flexibleSchedule(aa)+\
          CommunityInvolement(bb)+ManegementLevels(cc)+groupSize(dd)+workspace(ee)+socialOutings(ff)+HQLocation(gg)+\
          dress(hh)+screenTime(ii)+coffee(jj)+lunch(kk)+coAge(ll)
    return all

def perfectJob(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll):
    val = allFactors(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll)
    return val



def eachFactor(a,b,c,d,e,f,g):
    listMax = []
    listMin = []
    list1 = [[a,'pay(a)'],[b,'weekend(b)'],[c,'location(c)'],[d,'hours(d)'],[e,'shift(e)'],\
            [f,'hybrid(f)'],[g,'travel(g)']]
    list2 = [[a,'pay(a)'],[b,'weekend(b)'],[c,'location(c)'],[d,'hours(d)'],[e,'shift(e)'],\
            [f,'hybrid(f)'],[g,'travel(g)']]
    for i in range(5):
        valueMax = max(list1)
        list1 = [ele for ele in list1 if ele != valueMax]
        listMax.append(valueMax)
        if len(listMax) == 5 or len(listMax) > 5:
            break

    for i in range(5):
        valueMin = min(list2)
        list2 = [ele for ele in list2 if ele != valueMin]
        listMin.append(valueMin)
        if len(listMin) == 5 or len(listMin) > 5:
            break
    return listMin, listMax


print(eachFactor(1,11,1,-4,1,1,0))
def score():
    score = allVal
    # must be 80% match
    xval = perfectJobVal * 0.8
    if score > xval or score == xval:
        print("The job had a score of " + str(score) + ", you will see the posting")
    else:
        print("The job had a score of " + str(score) + ", you will not see the posting")

# print(idealL(5, 20, 17))
# print(idealU(35, 100, 35.7))
# print(idealM(0, 20, 16))
# print(idealW(6, 13, 10, 14))

perfectJobVal = perfectJob(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37)
allVal = allFactors(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,0)
score()