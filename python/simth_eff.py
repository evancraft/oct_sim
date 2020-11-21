"""
Written by: Evan Craft (November 2020)

Calculates theoretical efficiency

"""


import random
import math

def comb(n, r):

  num = math.factorial(n)
  denom = math.factorial(n-r)*math.factorial(r)

  return int(num/denom)

def choosing(array, m):

    comboList = [];
    combo = [random.randint(0, len(array)-1)]

    fixed = array.copy()

    for i in range(m-1):

      index = random.randint(0, len(array)-1)

      while index in combo:

        index = random.randint(0, len(array)-1)

      combo.append(index)

    comboList.append(combo.sort()) 

    return combo

def prob(combo, array): 

  fixed = array.copy();

  isprob = 1;
  notprob = 1;

  for i in combo:

    isprob = isprob*array[i]

  for i in combo:

    array[i] = -1;

  for i in combo:

    array.remove(-1)

  for j in range(len(array)):

    array[j] = 1-array[j]

  for j in range(len(array)):

    notprob = notprob*array[j] 

  return isprob*notprob  

def combogenerate(array, m):  

  combo = choosing(array, m);

  comboList = [combo];

  top = comb(len(array),m);

  for i in range(top-1):

    combo = choosing(array, m);

    while combo in comboList:

      combo = choosing(array, m);

    comboList.append(combo)  

  return comboList  

def probGenerate(comboList, array):

  probarray = [];
  probsum = 0;
  
  for combo in comboList:

    fixed = array.copy();

    proba = prob(combo, fixed);

    probarray.append(proba)
    probsum = probsum + proba;

  return(probsum)

def incrementer(array, m):

  probArray = [];
  probSum = 0;

  length = m;

  fixed = array.copy();

  for i in range(m, len(array)): 
    
    combos = combogenerate(array, length);
    sum = probGenerate(combos, array)
    length = length+1;
    probArray.append(sum)
  
  final = 1;  

  for i in range(len(fixed)):

      final = final*fixed[i]

  probArray.append(final)

  for k in range(len(probArray)):

    probSum = probSum + probArray[k]    

  return probSum;  
    
#print(choosing([.9, .3, .8], 2))
#print(prob(choosing([.9, .3, .8,.7], 2),[.9, .3, .8,.7]))
#print(combogenerate([.9, .3, .8,.7], 2))
#print(probGenerate(combogenerate([.9, .3, .8,.7], 2), [.9, .3, .8,.7]))

#print(incrementer([.3, .3, .3,.3], 3))


x = .1;
for i in range(10):
  print(x)
  print(round(pow(incrementer([x, x, x, x],3),2),3))
  #print(round(pow(incrementer([x, x, x, x, x, x, x, x],6),1),3))
  print("")
  x = round(x + .1,2);
