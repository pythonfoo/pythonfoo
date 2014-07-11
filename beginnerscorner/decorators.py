
#Dekoratoren
#-----------

# Dekoratoren sind Funktionen, die Funktionen verändern.

# Zuerst brauchen wir eine Funktion, die irgend etwas macht:
# Signatur: `f`: int -> int
def f(n):
    """Addiert etwas zum gegebenen Argument."""
    return n + 4 # garantiert zufällig gewählt
f(13)

    
# Nehmen wir an, wir wollen wissen, wann die Funktion aufgerufen wird, z.B. zum Debuggen.
# Wir könnten eine andere Funktion machen, die die Aufrufe protokolliert:
# Signatur: `fDebug`: int -> int
def fDebug(n):
    """Addiert etwas zum gegebenen Argument und protokolliert das."""
    print("  aufgerufen mit %d" % n)
    res = n + 4
    print("  Ergebnis ist: %d" % res)
    return res
fDebug(13)


# Das ist nicht so toll, weil wir dann jeden Aufruf der Funktion durch unsere Debug-Funktion
# austauschen müssen -- und wenn wir wieder fertig sind, dann müssen wir die Funktion wieder
# zurücktauschen.

fPrime = f
# Eine andere Variante wäre, die Funktion selbst zu modifizieren oder auszutauschen:
# Signatur: `f`: int -> int
def f(n):    # debug-variante
    """Addiert etwas zum gegebenen Argument und protokolliert das."""
    print("  aufgerufen mit %d" % n)
    res = n + 4
    print("  Ergebnis ist: %d" % res)
    return res
f(13)

# und wieder zurück für später:
f = fPrime



# Auch hier ist das Problem, dass wir unsere Funktion austauschen und hinterher wieder
# zurücktauschen müssen. Und diese Lösung ist auch nicht wiederbenutzbar.
# Besser wäre es also, wenn wir die Funktion (die das macht, was wir wollen), mit dem
# Verhalten, das wir zusätzlich/temporär haben wollen, zu modifizieren.
# Signatur: `fDebugProtocol`: int -> int
def fDebugProtocol(n):
    print("  aufgerufen mit %d" % n)
    res = f(n)
    print("  Ergebnis ist: %d" % res)
    return res
fDebugProtocol(13)


# Auch hier: die Funktion ist speziell für `f` gemacht, also nicht wiederverwendbar.
# Immerhin haben wir schon das Verhalten aus-faktoriert.
# Die Wiederverwendbarkeit erreichen wir jetzt, indem wir der `debugProtocol` die
# Funktion übergeben, die wir protokollieren wollen:
# Signatur: `debugProtocolForFunction`: (`f`: int -> int, int) -> int
def debugProtocolForFunction(someF, n):
    print("  aufgerufen mit %d" % n)
    res = someF(n)
    print("  Ergebnis ist: %d" % res)
    return res
debugProtocolForFunction(f, 13)

# Besser, aber immer noch nicht toll: Wir müssen jeden Aufruf von `f` durch
# das `debugProtocol` ersetzen.
# Besser wäre es doch, die Funktion direkt zu modifizieren. Das erreichen wir, indem
# wir eine Funktion machen, die `f` als Argument nimmt und wieder eine Funktion zurückgibt.
# Das heißt, die Signatur ist 
# debugF: (int -> int) -> (int -> int)
def debugF(someF):
    # wir müssen wieder eine Funktion zurückgeben, also müssen wir eine machen:
    def aux(n):
        print("  aufgerufen mit %d" % n)
        res = someF(n)   # warum können wir hier f benutzen? Weil hier eine "Closure" vorhanden ist.
        print("  Ergebnis ist: %d" % res)
        return res
    return aux

# direkter Aufruf:
debugF(f)(13)

# und für später:
f2 = debugF(f)
# beliebieger Code 
f2(13)

# Weil das sehr praktisch ist, gibt es dafür in Python eine spezielle Syntax: die @-Syntax.
# Dadurch wird `debugF` zum Dekorator.
@debugF
def f3(n):
    """Gleiche Funktion wie vorhin!"""
    return n + 4
    
def f7(n):
    return n ** 2
f7 = debugF(f7)

# Jede Funktion, die eine Funktion nimmt und eine Funktion zurückgibt, kann als Dekorator benutzt werden.
# (Auch, wenn sich die Signaturen verändern (was auch sehr nützlich sein kann).)

def needsPassword(f):
    def aux(password, n):
        if password != 'vErYsEcReT':
            raise ValueError('password unknown')
        return f(n)
    return aux

@needsPassword
def g(n):
    return n + 7

g(7)                 # Falsche Signatur!
g('meinPasswort', 7) # ValueError weil falsches Passwort
g('vErYsEcReT', 7)   # yay!



# Komplizierter wird es, wenn der Dekorator auch noch ein Argument haben soll.

def addTo(N):
    def addNTo(f):
        def aux(n):
            return f(n) + N
        return aux
    return addNTo


# addTo: int -> ((int -> int) -> (int -> int))
@addTo(7)  # (int -> int) -> (int -> int)
def f(n):
    return n * 2





# Dekorator, der zu jeder Ausgabe auch die Uhrzeit ausgibt.
# >>> output("hallo")   # output: * -> None
# 19:30   hallo

def timeOut(f):
    def aux(*ausgabe):
        print("the time is now!",)
        f(*ausgabe)
        # return None
    return aux



@timeOut
def output(*ausgabe):
    print(*ausgabe)
    



lambda x : (x + 1)

def no_name(x):
    return x + 1





