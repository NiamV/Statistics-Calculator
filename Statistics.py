import math
import random

def Choose(n,r):
    num = math.factorial(n)
    den = math.factorial(r)*math.factorial(n-r)
    return int(num/den)

#DistributionProbability gives the value of P(X=x)
#CumulativeDistribution gives the value of P(X<=x)
#DistributionValue gives a value generated from the distribution
#DistributionSample produces 1000 values from the distribution

#This section defines a binomial distribution

def BinomialProbability(n,p,x):
    term1=Choose(n,x)
    term2=p**x
    term3=(1-p)**(n-x)
    return(term1*term2*term3)

def CumulativeBinomial(n,p,x):
    total = 0
    for i in range(0,x+1):
        total += BinomialProbability(n,p,i)
    return total

def BinomialValue(n,p):
    prob = random.random()
    a = 0
    while prob > 0:
        prob -= BinomialProbability(n,p,a)
        a+=1
    return a-1

def BinomialSample(n,p):
    results = []

    for _i in range(0,n+1):
        results.append(0)

    for _i in range(0,1000):
        outcome = BinomialValue(n,p)
        results[outcome] = results[outcome] + 1

    return results

#This section defines a Poisson Distribution

def PoissonProbability(l,x):
    term1 = math.e**-l
    term2 = l**x
    term3 = math.factorial(x)
    return float(term1*term2)/float(term3)

def CumulativePoisson(l,x):
    total = 0
    for i in range(0,x+1):
        total += PoissonProbability(l,i)
    return total

def PoissonValue(l):
    prob = random.random()
    for i in range(0,math.floor(10*l)):
        prob -=PoissonProbability(l,i)
        if prob < 0:
            break
    return i

def PoissonSample(l):
    results = []

    for _i in range(0,math.floor(10*l)):
        results.append(0)

    for _i in range(0,1000):
        outcome = PoissonValue(l)
        results[outcome] = results[outcome] + 1

    return results

#This section defines a Normal Distribution

def XtoZ(x,mean,stdev):
    z = float((x - mean))/float(stdev)
    return z

def ZtoX(z,mean,stdev):
    x = stdev*z + mean
    return x

def NormalCDFExpansion(z,n):
    term1 = (-1)**(n+1)
    term2 = z**((2*n)-1)
    term3 = (2*n)-1
    term4 = 2**(n-1)
    term5 = math.factorial(n-1)
    numerator = term1*term2
    denominator = term3*term4*term5
    return float(numerator)/float(denominator)

def CumulativeNormal(mean,stdev,x):
    z = XtoZ(x,mean,stdev)
    if z < -5:
        return 0.000000573
    if z > 5:
        return 0.999999713
    prob = 0.5
    for i in range(1,100):
        nextTerm = float(NormalCDFExpansion(z,i))/float(math.sqrt(2*math.pi))
        prob += nextTerm
    return prob

def NormalValue(mean,stdev):
    prob = float(random.random())
    for i in range(-500,500):
        j = float(i)/float(100)
        if float(CumulativeNormal(0,1,j)) > prob:
            break
    return int(ZtoX(j,mean,stdev)+0.5)

def NormalSample(mean,stdev):
    results = []

    for _i in range(mean-5*stdev,mean+5*stdev+1):
        results.append(0)
    
    for _i in range(0,100):
        outcome = int(NormalValue(mean,stdev))
        index = outcome - (mean-5*stdev)
        results[index] = results[index] + 1
    
    return results

#This section defines a Geometric Distribution

def GeometricProbability(p,x):
     q = 1-p
     term1 = q**(x-1)
     term2 = p
     return term1*term2

def CumulativeGeometric(p,x):
    complement = (1-p)**x
    return 1 - complement

def GeometricValue(p):
    prob = random.random()
    highest = math.floor(float(8)/float(p))
    for i in range(1,highest):
        prob -= GeometricProbability(p,i)
        if prob < 0:
            break
    return i

def GeometricSample(p):
    results = []
    
    for _i in range(0,math.floor(float(8)/float(p))):
        results.append(0)
    
    for _i in range(0,1000):
        outcome = GeometricValue(p)
        results[outcome-1] = results[outcome-1] + 1
    
    return results

#This section defines a Negative Binomial Distribution

def NegativeBinomialProbability(r,p,n):
    if n < r:
        return 0
    else:
        binomialprob = BinomialProbability(n-1,p,r-1)
        return binomialprob * p

def CumulativeNegativeBinomial(r,p,n):
    morethan = CumulativeBinomial(n,p,r-1)
    return 1 - morethan

def NegativeBinomialValue(r,p):
    prob = random.random()
    highest = math.floor((float(r)*5)/float(p))
    for i in range(r,highest):
        prob -= NegativeBinomialProbability(r,p,i)
        if prob < 0:
            break
    return i

def NegativeBinomialSample(r,p):
    results = []

    for _i in range(r,math.floor((float(r)*5)/float(p))+1):
        results.append(0)
        
    for _i in range(0,1000):    
        outcome = NegativeBinomialValue(r,p)
        results[outcome-r] = results[outcome-r]+1
    
    return results

#This section defines a Discrete Uniform Distribution

def DiscreteUniformProbability(min,max):
    difference = max + 1 - min
    return float(1)/float(difference)

def CumulativeDiscreteUniform(min,max,x):
    difference = x + 1 - min
    prob = DiscreteUniformProbability(min,max)*difference
    return prob
 
def DiscreteUniformValue(min,max):
    prob = random.random()
    a = 0
    while prob > 0:
        prob -= DiscreteUniformProbability(min,max)
        a += 1
    return a-1

def DiscreteUniformSample(min,max):
    results = []

    for _i in range(min,max+1):
        results.append(0)

    for _i in range(0,1000):
        outcome = DiscreteUniformValue(min,max)
        results[outcome] = results[outcome] + 1
        
    return results

#Binomial = 1
N = 10              
P_binomial = float(0.2)      
#Poisson = 2
L = 2.3             
#Normal = 3
mean = 1000
stdev = 10
#Geometric = 4
P_geometric = 0.5             
#Negative Binomial = 5
r = 3
P_negativeBinomial = 0.8
#Discrete Uniform = 6
min = 1
max = 10

#This section does a hypothesis test

alpha = 0.05
distribution = 3        # Can use distribution 1(Binomial), 2(Poisson), 3(Normal), 4(Geometric)
testStatistic = 5

def HypothesisTest(dist,test,sig):
    if dist == 1:
        prob = CumulativeBinomial(N,P_binomial,test)
    if dist == 2:
        prob = CumulativePoisson(L,test)
    if dist == 3:
        prob = CumulativeNormal(mean,stdev,test)
    if dist == 4:
        prob = CumulativeGeometric(P_geometric,test)
    
    print("The probability that the test statistic occured is", prob)

    if prob < sig or prob > 1 - sig:
        return "Reject H0, there is sufficient evidence that the assumption is incorrect"
    else:
        return "Accept H0, there is insuffienct evidence that the assumptions is incorrect"

#print(HypothesisTest(distribution,testStatistic,alpha))

#This section creates the sample means from a given distribution

distribution = 1

def sampleMean(dist):
    sampleSize = 10
    sum = 0
    
    for _i in range(0,10):
        if dist == 1:
            outcome = BinomialValue(N,P_binomial)
        if dist == 2:
            outcome = PoissonValue(L)
        if dist == 3:
            outcome = NormalValue(mean,stdev)
        if dist == 4:
            outcome = GeometricValue(P_geometric)
        if dist == 5:
            outcome = NegativeBinomialValue(r,P_negativeBinomial)
        sum += outcome
        
    average = math.floor(sum/sampleSize)
    return average

def sampleMeansSample(dist):
    results = []
    
    if dist == 1:
        number = N+1
    if dist == 2:
        number = 10*L
    if dist == 3:
        number = 10*stdev + 1
    if dist == 4:
        number = math.floor(float(8)/float(P_geometric))
    if dist == 5:
        number = math.floor((float(r)*5)/float(P_negativeBinomial))

    for _i in range(0,number+1):
        results.append(0)

    for _i in range(0,10000):
        sample = sampleMean(dist)        
        if dist == 1:
            index = sample
        if dist == 2:
            index = sample
        if dist == 3:
            index = sample - (mean-5*stdev)
        if dist == 4:
            index = sample - 1
        if dist == 5:
            index = sample - r
        results[index] = results[index] + 1

    return results

#print(sampleMeansSample(distribution))

#This section does a Chi-Squared test

table = open("F:\\Other\\Coding Stuff\\Statistics\\ChiSquaredTable.txt")
data = table.readlines()

def SigToColumn(nu):
    levels = ["v",0.995,0.990,0.975,0.950,0.900,0.100,0.050,0.025,0.010,0.005]
    try:
        index = levels.index(nu)
        return index
    except:
        print("Invalid Significance Level")
    
distribution = 1            # Can use distribution 1(Binomial), 2(Poisson), 4(Geometric), 5(Negative Binomial)
significanceLevel = 0.05
observed = [12,28,28,17,7,4,2,2,0]
parametersNeeded = 0

def totalFrequency(list):
    total = 0
    for i in list:
        total += i
    return total

def generateExpected(dist,freqTotal,cellsTotal):
    E = []
    for i in range(0,cellsTotal-1):
        if dist == 1:
            if cellsTotal > N+1:
                return "Too many cells for a Binomial Distribution"
            prob = BinomialProbability(N,P_binomial,i)
        if dist == 2:
            prob = PoissonProbability(L,i)
        if dist == 4:
            prob = GeometricProbability(P_geometric,i+1)  #Geometric Starts from 1 not 0
        if dist == 5:
            prob = NegativeBinomialProbability(r,P_negativeBinomial,i+r)
        nextValue = round(prob*freqTotal,2)
        E.append(nextValue)
    lastValue = freqTotal - totalFrequency(E)
    E.append(round(lastValue,2))
    return E

def combineCells(O,E):
    i = 0
    while i < len(E) - 1:
        if E[i] < 5:
            E[i] = E[i] + E[i+1]
            E.remove(E[i+1])
            O[i] = O[i] + O[i+1]
            O.remove(O[i+1])
        else:
            i += 1
    if E[len(E)-1] < 5:
        E[len(E)-2] = E[len(E)-1] + E[len(E)-2]
        E.remove(E[len(E)-1])
        O[len(O)-2] = O[len(O)-1] + O[len(O)-2]
        O.remove(O[len(O)-1])
    return O,E

def chiSquaredcalc(O,E):
    sum = 0
    for i in range(0,len(O)):
        sum += float(O[i]*O[i])/float(E[i])
    stat = sum - totalFrequency(O)
    return stat

def chiSquaredTest(O,parametersCalculated):
    total = totalFrequency(observed)
    cells = len(observed)
    E = generateExpected(distribution,total,cells)

    if type(E) == str:
        return E
    
    observedFinal = combineCells(O,E)[0]
    expectedFinal = combineCells(O,E)[1]
    
    testStatistic = chiSquaredcalc(observedFinal,expectedFinal)
    
    degreesOfFreedom = len(O) - parametersCalculated - 1
    CriticalValue = float(data[degreesOfFreedom].split(" ")[SigToColumn(significanceLevel)])
    
    print("The Chi Squared Statistic is", testStatistic)
    print("The critical value is", CriticalValue)
    
    if testStatistic > CriticalValue:
        return "Reject H0, the distribution does not fit the data"
    else:
        return "Accept H0, the distribution does fit the data"

#print(chiSquaredTest(observed,parametersNeeded))

#This section analyses univariate data

def Mean(nums):
    total = 0
    for i in nums:
        total += i

    freq = len(nums)

    return float(total)/float(freq)

def Median(nums):
    freq = len(nums)
    if freq % 2 == 1:
        mid = math.floor((freq + 1)/2)
        value = nums[mid]
    elif freq % 2 == 0:
        mid = math.floor(freq/2)
        value = float(nums[mid]+nums[mid+1])/float(2)
    return value
    
def Mode(nums):
    currentMode = 0
    maxCount = 0

    localnums = []
    for i in nums:
        localnums.append(i)
    
    while len(localnums)>1:
        firstValue = localnums[0]
        count = 0
        i = 0
        while i < len(localnums):
            if localnums[i] == firstValue:
                count += 1
                localnums.pop(i)
            else:
                i += 1
        if count > maxCount:
            currentMode = firstValue
            maxCount = count

    return currentMode

def Variance(nums):
    mu = Mean(nums)
    total = 0
    for i in nums:
        displacement = i - mu
        squaredDistance = displacement ** 2
        total += squaredDistance
    var = float(total)/len(nums)
    return var

def StDev(nums):
    var = Variance(nums)
    stdev = math.sqrt(var)
    return stdev

#This section analyses bivariate data    

x_values = [1,2,3,4,5,6,7,8]
y_values = [2,5,4,7,6,5,9,12]

def Sxy(numsx, numsy):
    sumOfx = 0
    sumOfy = 0
    sumOfxy = 0
    for i in range(0,len(numsx)):
        sumOfx += numsx[i]
        sumOfy += numsy[i]
        sumOfxy += numsx[i]*numsy[i]
    term1 = sumOfxy
    term2 = float(sumOfx * sumOfy)/float(len(numsx))
    return term1 - term2

def b_value(numsx, numsy):
    num = Sxy(numsx, numsy)
    den = Sxy(numsx, numsx)
    return float(num)/float(den)

def a_value(numsx, numsy):
    term1 = Mean(numsy)
    term2 = b_value(numsx, numsy) * Mean(numsx)
    return term1 - term2

def PMCC(numsx, numsy):
    num = Sxy(numsx, numsy)
    den = math.sqrt(Sxy(numsx, numsx) * Sxy(numsy, numsy))
    return float(num)/float(den)

#This section does a regression hypothesis test

RegressionTable = open("F:\\Other\\Coding Stuff\\Statistics\\RegressionTable.txt")
RegressionData = RegressionTable.readlines()

def RegressionSigToColumn(nu):
    levels = ["n",0.10,0.05,0.025,0.01,0.005]
    try:
        index = levels.index(nu)
        return index
    except:
        print("Invalid Significance Level")

def RegressionHypothesisTest(numsx, numsy, sig):
    r = PMCC(numsx, numsy)
    n = len(numsx)

    CriticalValue = float(RegressionData[n-3].split(" ")[RegressionSigToColumn(sig)])

    if abs(r)>CriticalValue:
        return "Reject H0, there is sufficient evidence that there is a correlation between the two variables"
    else:
        return "Accept H0, there is insufficient evidence that there is a correlation between the two variables"

#print(RegressionHypothesisTest(x_values, y_values, 0.05))

print("Done")