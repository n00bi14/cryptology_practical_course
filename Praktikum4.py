from random import SystemRandom

def getXdach(a, b, g):
    r = [a,b]
    x = []
    q = [0,0]
    k = 2

    x.append(1)
    x.append(0)

    while r[k-1] != g:
        r.append(r[k-2] % r[k-1])
        q.append(r[k-2] // r[k-1])
        x.append(q[k] * x[k-1] + x[k-2])

        k += 1

    return ((-1)**(k-1)) * x[k-1]

def euklid(c, d, m):
    if c >= 0 and d >= 0 and m > 0:
        g = gcd(c,m)
        if(d % g == 0):
            xDach = getXdach(c,m,g)
            return ((d / g) * xDach) % m

    return -1

def gcd(a,b):
    return gcd_run(a,b)

def gcd_run(a,b):
    if a % b == 0:
        return b
    return gcd_run(b, (a % b))

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


def encrypt(m, e, n):
    c = pow(m,e,n)
    return c

def decrypt(c, d, n):
    m = pow(c,d,n)
    return m

#Public Hoever
e_hoever = 23
n_hoever = 80838935643632347602689406251916492097256843104786631171171136456894311297084228755070725430240723776343069111225050752902571341583566366600578313441710584699499981601286903467954723125645821950643557

#Public Gath
n_gath = 4993977088673899617945645970224821274948475280315390584131209195195015050936748731238441935278119391732327211009956455799929205757456300436982211390998471005527202341115944446758821094590475528086362962424793472891006317
e_gath = 36349

#Private Gath
d_gath = 2356507607497722805221704027106554086987709373241893292773350026575281249928942040721938872428135679303223646337601272361039189505827263850754138514432452268282791652291957380023588558378809735459460084348720015149513557



#Hoever Datei:
encrypted_session_key_hoever = 4129421140656027232379311404061298024143579235884801474329555032623630998465237763888633722734861591625903215194456825699656979228427743272534109831806578297352579244629080229346763684495833511081756853474985228530591112
signature_hoever = 76275632408289628438136528549554768804773457542686823699171861767406511460264060908917620757953961257269207646111035121568088464344925976535806377690175053291904402377663734447681813143987396018437220
decrypted_session_key_hoever = hex(decrypt(encrypted_session_key_hoever, d_gath, n_gath))
decrypted_signature_hoever = hex(encrypt(signature_hoever, e_hoever, n_hoever))
hash_karte_pdf = 0x91a9accee30c344f190e11d9c3ba844df340a325

print "Decrypted session key hoever: " + str(decrypted_session_key_hoever)
print "Decrypted signature hoever: " + str(decrypted_signature_hoever)
print "Compare hash and signature: " + str(hex(hash_karte_pdf) == decrypted_signature_hoever)
print ""
print ""
print ""

#Gath Datei:
session_key_gath = int(0xFBDFFDEEE164E26E8F415F0FEF4FF08EAAL)
hash_foto_png = int(0xbdb5f22c312cc19e78151b0411d018ffe5f684eeL)
encrypted_session_key_gath = encrypt(session_key_gath, e_hoever, n_hoever)
#encrypted_session_key_gath = encrypt(session_key_gath, e_gath, n_gath) #Only for testing
encrypted_hash_foto_png = decrypt(hash_foto_png, d_gath, n_gath)


print "Encrypted session key gath: " + str(encrypted_session_key_gath)
print "Encrypted signature gath: " + str(encrypted_hash_foto_png)
print ""
print ""
print ""

#Check:
decrypted_session_key_gath = hex(decrypt(encrypted_session_key_gath, d_gath, n_gath)) # Works only with testing encryption
decrypted_signature_gath = hex(encrypt(encrypted_hash_foto_png, e_gath, n_gath))

print "Decrypted session key gath: " + str(decrypted_session_key_gath)
print "Decrypted signature gath: " + str(decrypted_signature_gath)
print "Compare hash and signature: " + str(hex(hash_foto_png) == decrypted_signature_gath)