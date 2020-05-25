from random import SystemRandom
import multiprocessing as mp

def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step

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


def getNextPrim(n, it):
    while isCompositeMillerRabin(n,it):
        n = n + 1

    return n

def monteCarloNextPrim(anz, n, it):
    cryptogen = SystemRandom()

    result = 0

    for i in range(anz):
        randomNumber = cryptogen.randint(1, n)
        distance = 0
        #print "Number = " + str(randomNumber)

        while isCompositeMillerRabin(randomNumber, it):
            randomNumber = randomNumber + 1
            distance = distance + 1

        result = result + distance
        i = i + 1

    return (result // anz)

def countWitness(n):
    count = 0
    for i in range(1, n-1):
        if isCompositeWitness(i, n):
            count = count + 1
    return count



#Aufgabe 1
print("Aufgabe 1:")
print("Ist moeglicherweise Prim? " + str((not isCompositeMillerRabin(17, 5))))
print("Ist moeglicherweise Prim? " + str((not isCompositeMillerRabin(32, 5))))
print("Ist moeglicherweise Prim? " + str((not isCompositeMillerRabin((10 ** 100), 10))))

print("")
print("")

#Aufgabe 2
print("Aufgabe 2:")
print("Naechste Primzahl : " + str(getNextPrim(17, 5)))
print("Naechste Primzahl : " + str(getNextPrim(32, 5)))
print("Naechste Primzahl : " + str(getNextPrim((10 ** 100), 10)))

print("")
print("")

#Aufgabe 3
print("Aufgabe 3:")
print("Anzahl Zeugen: " + str(countWitness(9)))
print("Anzahl Zeugen: " + str(countWitness(325)))

print("")
print("")


def parallelSim(anz, rangeTo):
    fobj_out = open("generated_files/"+str(anz) + "_sims_nextPrim","w")
    for i in drange(2, rangeTo, 0.5):
        print(str(anz) + " Simulationen, i = " + str(i))
        fobj_out.write(str((i*2+1)) + "\t" + str(monteCarloNextPrim(anz, 100**i, 10)) + "\n")

    fobj_out.close()

#Aufgabe 4
a = [50, 100, 200]
processes = [mp.Process(target=parallelSim, args=(x, 50)) for x in a]

# Run processes
for p in processes:
    p.start()

# Exit the completed processes
for p in processes:
    p.join()

