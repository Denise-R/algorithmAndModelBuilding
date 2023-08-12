"""The function idealU() takes the exceptable range of values our participant is willing to consider for a particular job
factor and assigns a standardized numeric value (1-5) based on the upper and lower bounds.
This function is called when the participants ideal value is the upper bound.
For example, this function may be called for a factor like 'miles from job site'."""


def idealU(lower, upper, x):
    changeRate = (upper - lower) / 3
    rangeList = [upper]
    for i in range(3):
        value = rangeList[i] - changeRate
        rangeList.append(value)
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


"""The function idealL() is almost identical to idealU(), but assigns the numeric value 1-5 when the participants ideal 
value for a particular job factor is the upper bound.
For example, this function may be called for a factor like 'pay'."""


def idealL(lower, upper, x):
    changeRate = (lower - upper) / 3
    rangeList = [lower]
    for i in range(3):
        value = rangeList[i] - changeRate
        rangeList.append(value)
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


"""The function idealM() is almost identical to the functions previously mentioned, but assigns the numeric value 1-5 
when the participants ideal value for a particular job factor is the middle value between the upper and lower bounds.
For example, this function may be called for a factor like 'required remote work' when a range of 1-20hrs is 
given and 10hrs is the ideal."""


def idealM(lower, upper, x):
    mid = (upper - lower) / 2
    changeRate = mid / 4
    rangeList = [mid - changeRate]
    rangeList2 = [mid + changeRate]
    for i in range(3):
        value1 = rangeList[i] - changeRate
        rangeList.append(value1)
        value1 = rangeList2[i] + changeRate
        rangeList2.append(value1)
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


"""Similar to previous functions, idealM() assigns the numeric value 1-5 when the participants ideal value for a job 
factor is neither the upper bound, lower bound, or mid value.
For example, this function may be called for a factor like 'required remote work' when a range of 1-20hrs is 
given and 5hrs is the ideal"""

def idealW(lower, upper, ideal, x):
    right = (upper - ideal) / 4
    left = (ideal - lower) / 4
    rangeListR = [(ideal + right)]
    for i in range(3):
        value = rangeListR[i] + right
        rangeListR.append(value)
    rangeListL = [(ideal - left)]
    for i in range(3):
        value = rangeListL[i] - left
        rangeListL.append(value)
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


"""The functions from lines 112 - ### allow the us to determine the determine the rating of a given job factor (x) 
based on the ideal value type (ideal upper, lower, mid, or wildcard value). Each of these ratings are then multiplied by
 the weight each factor was assigned by our participant."""


def pay(x):
    rating = idealU(1, 5, x)
    # 2 is the weight
    return rating * 2


def weekend(x):
    rating = idealU(1, 5, x)
    return rating * 2


def location(x):
    rating = idealL(5, 20, x)
    return rating * 5


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


""" The function allFactors is used to determine the overall score for a given job based on each job factor listed in 
the job announcement."""


def allFactors(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, x, y, z, aa, bb, cc, dd, ee, ff, gg,
               hh, ii, jj, kk, ll):
    all = pay(a) + weekend(b) + location(c) + hours(d) + shift(e) + hybrid(f) + travel(g) + negotiation(h) + osha(i) + \
          reviews(j) + managmentStyle(k) + workStress(l) + benifits(m) + retension(n) + educationAndTraining(o) + \
          strengthWeakness(p) + pastWork(q) + advancement(r) + techniqualSkills(s) + vacationTime(t) + \
          PoliticalAffiliation(u) + PoliticalInvolvement(v) + amentities(x) + m_e_ratio(y) + softSkills(z) + \
          flexibleSchedule(aa) + CommunityInvolement(bb) + ManegementLevels(cc) + groupSize(dd) + workspace(ee) + \
          socialOutings(ff) + HQLocation(gg) + dress(hh) + screenTime(ii) + coffee(jj) + lunch(kk) + coAge(ll)
    return all


"""The function perfectJob is used to determine the score of a job that would be a 100% match for our participant."""


def perfectJob(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, x, y, z, aa, bb, cc, dd, ee, ff, gg,
               hh, ii, jj, kk, ll):
    val = allFactors(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, x, y, z, aa, bb, cc, dd, ee, ff,
                     gg, hh, ii, jj, kk, ll)
    return val


"""The function max5min5factors() returns the 5 factors with the highest and lowest score for a given job. 
This function takes each factor value listed on a job announcement for a given job.
If there is a tie for 5th place, more than 5 values will be returned."""


def max5min5factors(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, x, y, z, aa, bb, cc, dd, ee, ff, gg,
               hh, ii, jj, kk, ll):
    factorVals = [pay(a), weekend(b), location(c), hours(d), shift(e), hybrid(f), travel(g), negotiation(h), osha(i),
                  reviews(j), managmentStyle(k), workStress(l), benifits(m), retension(n), educationAndTraining(o),
                  strengthWeakness(p), pastWork(q), advancement(r), techniqualSkills(s), vacationTime(t),
                  PoliticalAffiliation(u), PoliticalInvolvement(v), amentities(x), m_e_ratio(y), softSkills(z),
                  flexibleSchedule(aa), CommunityInvolement(bb), ManegementLevels(cc), groupSize(dd), workspace(ee),
                  socialOutings(ff), HQLocation(gg), dress(hh), screenTime(ii), coffee(jj), lunch(kk), coAge(ll)]
    factors = ['pay(a)','weekend(b)','location(c)','hours(d)','shift(e)','hybrid(f)','travel(g)','negotiation(h)',
               'osha(i)','reviews(j)',' managmentStyle(k)','workStress(l)','benifits(m)','retension(n)',
               'educationAndTraining(o)','strengthWeakness(p)','pastWork(q)','advancement(r)','techniqualSkills(s)',
               'vacationTime(t)','PoliticalAffiliation(u)','PoliticalInvolvement(v)','amentities(x)','m_e_ratio(y)',
               'softSkills(z)','flexibleSchedule(aa)','CommunityInvolement(bb)','ManegementLevels(cc)','groupSize(dd)',
               'workspace(ee)','socialOutings(ff)','HQLocation(gg)','dress(hh)','screenTime(ii)','coffee(jj)',
               'lunch(kk)','coAge(ll)']
    listMin = []
    listMax = []
    factorVals2 = factorVals.copy()
    factors2 = factors.copy()
    """Maximum 5 factors affecting overall score"""
    for i in range(5):
        valueMax = max(factorVals)
        indices = []
        for j in range(len(factorVals)):
            if factorVals[j] == valueMax:
                indices.append(j)
                listMax.append([factors[j], factorVals[j]])
        factorVals = [element for i, element in enumerate(factorVals) if i not in indices]
        factors = [element for i, element in enumerate(factors) if i not in indices]
        if len(listMax) == 5 or len(listMax) > 5:
            break
    """Minimum 5 factors affecting overall score"""
    for i in range(5):
        valueMin = min(factorVals2)
        indices = []
        for j in range(len(factorVals2)):
            if factorVals2[j] == valueMin:
                indices.append(j)
                listMin.append([factors2[j], factorVals2[j]])
        factorVals2 = [element for i, element in enumerate(factorVals2) if i not in indices]
        factors2 = [element for i, element in enumerate(factors2) if i not in indices]
        if len(listMin) == 5 or len(listMin) > 5:
            break
    print("Min factors: " + str(listMin))
    print("Max factors: " + str(listMax))
    return listMax, listMin


"""The function score() is used determine if a given job posting will or will not be seen by a user. This function 
takes one parameter, percentMatch, to allow the AI designers to set the minimum required percent match a job positing 
(jobScore)must be when compared to the users ideal job (peferctJobVal)."""


def score(percentMatch):
    x = perfectJobVal * percentMatch
    if jobScore > x or jobScore == x:
        print("The job had a score of " + str(jobScore) + ", you will see the posting")
    else:
        print("The job had a score of " + str(jobScore) + ", you will not see the posting")


"""Verifying/testing the 4 ideal functions"""
# print(idealL(5, 20, 17))
# print(idealU(35, 100, 35.7))
# print(idealM(0, 20, 16))
# print(idealW(6, 13, 10, 14))


"""Below are the only function calls that need to be made for testing the accuracy of our rule-based AI model. """
perfectJobVal = perfectJob(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                           26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37)
print("perfect job score: " + str(perfectJobVal))


jobScore = allFactors(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                      27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 0)
print("Job score: " + str(jobScore))


percentMatch = 0.8
score(percentMatch)


max5min5factors(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                      27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 0)


