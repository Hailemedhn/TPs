import random
import math
import matplotlib.pyplot as plt
import numpy as np

def coin_toss(p):
    if p < 0 or p > 1:
        print("P doit etre entre 0 and 1")
        return 
    else:
        coin = random.choices([0,1], weights=[1-p,p], k=1)
    return(coin[0])

def toss_1000():
    count = 0
    for i in range(10000):
        count += coin_toss(.25)
    print(count)

def n_times_toss(n,p):
    if p < 0 or p > 1 or n < 0:
        print("P doit etre entre 0 and 1 and n ne peut pas etre negatif")
        return 
    else:
        count = 0
        for i in range(n):
            count += coin_toss(p)
        return count
    
def binomial_toss(n,p):
    arr = list(range(n))
    weight = [math.comb(n,i)* (p**i) *((1-p)**(n-i)) for i in range(n)]
    
    return random.choices(arr,weights=weight)[0]

def throw_die_A():
    die_1 = random.choice([1,2,3,4,5,6])
    die_2 = random.choice([1,2,3,4,5,6])
    die_3 = random.choice([1,2,3,4,5,6])

    if die_1 == die_2 and die_2 == die_3:
        return True
    else:
        return False

def throw_die_B():
    die_1 = random.choice([1,2,3,4,5,6])
    die_2 = random.choice([1,2,3,4,5,6])
    die_3 = random.choice([1,2,3,4,5,6])

    if die_1 == 3 or die_2 == 3 or die_3== 3:
        return True
    else:
        return False

def throw_die_C():
    die_1 = random.choice([1,2,3,4,5,6])
    die_2 = random.choice([1,2,3,4,5,6])
    die_3 = random.choice([1,2,3,4,5,6])

    if die_1 + die_2 + die_3 == 4:
        return True
    else:
        return False

def A_B_C():
    return (throw_die_A() or throw_die_B() or throw_die_C())

def union_A_B_C():
    count = 0
    for i in range(1000): 
        if A_B_C() == True:
            count += 1
    return count/1000       

def binomial(n,p):
    """Simuler la distribution binomial et retour un resultat"""
    arr = list(range(n))
    weight = [math.comb(n,i)* (p**i) *((1-p)**(n-i)) for i in range(n)]
    return random.choices(arr,weights=weight)[0]
def lambda_bino(n,lam):
    p = lam/n
    return binomial(n,p)

def bino_histogramme(n,lam):
    x = []
    for i in range(1000):
        x = x + [lambda_bino(n,lam) for i in range(lam)]
  
    plt.hist(x, bins = 20, range=None, density=True, weights=None, cumulative=False)
    plt.title("Binomial Distribution Probabilité : n = " + str(n))
    plt.xlabel("X")
    plt.ylabel("Probabilité")

    plt.show()

def poisson(lam):
    """simule la distribution de poisson et donne une resultat"""
    arr = list(range(150))
    weight = [(np.e **-lam)* (lam**i)/math.factorial(i) for i in arr]

    return random.choices(arr,weights=weight)[0]

def poisson_histogramme(lam):
    """Simule le distribution poisson pour Z < 150 et lambda = 2"""
    x = []
    for i in range(10000):
        x.append(poisson(lam))
  
    plt.hist(x, bins = 20, range=None, density=True, weights=None, cumulative=False)
    plt.title("Binomial Poisson Probabilité")
    plt.xlabel("X")
    plt.ylabel("Probabilité")

    plt.show()

poisson_histogramme(2)      #Simuler la distribution poisson pour lambda = 2
bino_histogramme(50,2)   # Simuler la binomial distribution pour lambda = 2 et n= 50
bino_histogramme(100,2)   # Simuler la binomial distribution pour lambda = 2 et n= 100
bino_histogramme(200,2)   # Simuler la binomial distribution pour lambda = 2 et n= 200
