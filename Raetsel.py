from random import SystemRandom
import multiprocessing as mp

def getWitness(n):
    cryptogen = SystemRandom()
    return cryptogen.randint(1, n-1)

# berechnet m hoch e mod n
def modexp(m, e, n):
    if e == 0:
        return 1
    if e % 2 == 1:
        return m * modexp(m, e-1, n) % n
    x = modexp(m, e//2, n)
    p = x * x % n
    # zusaetzliche Pruefung:
    # x^2 = 1 mehr als die Loesungen 1 und -1
    if p == 1 and x != 1 and x != n-1:
        raise
    return p

def isCompositeWitness(a, n):
    try:
        p = modexp(a, n-1, n)
    except:
        return True
    return p != 1   #p negieren, da kein zusammengesetzter Zeuge

def isCompositeMillerRabin(n, k):
    if n == 2:
        return False
    for i in range(k):
        a = getWitness(n)
        if isCompositeWitness(a, n):
            return True
    return False



n = 80838935643632347602689406251916492097256843104786631171171136456894311297084228755070725430240723776343069111225050752902571341583566366600578313441710584699499981601286903467954723125645821950643557
nHalf = n // 2
part = nHalf // 6

p = 2
q = 0


def getNextPrim(current):
    current += 1
    while isCompositeMillerRabin(current, 5):
        current += 1
    return current

def testP(number, start):
    global q
    x = (number-1) * start
    if x == 0:
        x = 2
    while n % x != 0 and x <= number*start:
        x = getNextPrim(x)
        #print str(number) + ": " + str(x)                 #Only Debug!
    q = p


print "n = " + str(n)
print "nHalf = " + str(nHalf)
print "part = " + str(part)

processes = [mp.Process(target=testP, args=(x, x*part)) for x in range(1,6)]

# Run processes
for p in processes:
    p.start()

# Exit the completed processes
for p in processes:
    p.join()

print q
