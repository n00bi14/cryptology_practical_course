from random import SystemRandom

def gcd(a,b):
    return gcd_run(a,b, 1)

def gcd_run(a,b, rounds):
    if a % b == 0:
        return (b,rounds)
    return gcd_run(b, (a%b), rounds+1)

def monteCarloSim(anz, n):
    middle = 0
    cryptogen = SystemRandom()

    for a in range(1,anz):
        [a,b] = [cryptogen.randrange(n-1) for i in range(2)]
        while b == 0:
            [a,b] = [cryptogen.randrange(n-1) for i in range(2)]
        [result, rounds] = gcd(a,b)
        middle += rounds

    return middle / anz

def getXdach(a, b, g):

    #print a
    #print b

    r = [a,b]
    x = []
    q = [0,0]
    k = 2

    if a > b:
        x.append(0)
        x.append(1)
    else:
        x.append(1)
        x.append(0)

    #print "g=" + str(g)

    while r[k-1] != g:

        #k ist immer k+1

        r.append(r[k-2] % r[k-1])
        q.append(r[k-2] // r[k-1])
        x.append(q[k] * x[k-1] + x[k-2])

        #print "Round " + str(k)
        #print "rk=" + str(r[k])
        #print "rk-1=" + str(rkMinusEins)
        #print "qk=" + str(q[k])
        #print "xk=" + str(x[k])
        #print "xk-1=" + str(xkMinusEins)

        k += 1

    return x[k-1]

def euklid(c, d, m):
    if c >= 0 and d >= 0 and m > 0:
        [g,rounds] = gcd(c,m)
        if(d % g == 0):
            xDach = getXdach(m,c,g)
            #print "d=" + str(d) + "   g=" + str(g) +  "   xDach=" + str(xDach)
            return ((d / g) * xDach) % m


    return -1


"""
#Aufgabe 1 und Aufgabe 2:
[result1, rounds1] = gcd(282,240)
print "gcd(282,240) = " + str(result1) + " in " + str(rounds1) + " rounds."

[result2, rounds2] = gcd((9**100)+1,(10**100)+1)
print "gcd(9^100+1,10^100+1) = " + str(result2) + " in " + str(rounds2) + " rounds."


#Aufgabe 3 und Aufgabe 4:
print "Monte-Carlo-Sim mit anz = 50 und n von 1-99"
#for i in range(1,100):
#    print "n=" + str(i) + "; stellen=" + str((i*2+1))  + "; middle=" + str(monteCarloSim(100, 100**i))

fobj_out = open("50_sims","w")
for i in range(1,100):
    fobj_out.write(str((i*2+1))  + "\t" + str(monteCarloSim(50, 100**i)) + "\n")

fobj_out.close();

print "Monte-Carlo-Sim mit anz = 100 und n von 1-99"

fobj_out = open("100_sims","w")
for i in range(1,100):
    fobj_out.write(str((i*2+1))  + "\t" + str(monteCarloSim(100, 100**i)) + "\n")

fobj_out.close();

print "Monte-Carlo-Sim mit anz = 200 und n von 1-99"

fobj_out = open("200_sims","w")
for i in range(1,100):
    fobj_out.write(str((i*2+1))  + "\t" + str(monteCarloSim(200, 100**i)) + "\n")

fobj_out.close();
"""

#Aufgabe 5
print euklid(12, 20, 56)
print euklid(86, 13, 64)
print euklid(19, 14, 61)
print euklid(6, 3, 15)
print 10**100+1
print euklid(9**100+1, 8**100+1, 10**100+1)
