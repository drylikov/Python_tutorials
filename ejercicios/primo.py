# Implementar un generador de primos , usando
# itertools y el modulo count a partir del siguiente
# codigo

# Por ejemplo

def is_primo(n):
    if n < 2:
        return False
    for i in xrange(2,n):
        if not n %i:
            return False

    else:
        return True

# Generador de numero primo

def primo_gen():
    i = 1
    while True:
        if is_primo(i): yield i
        i += 1

# Prueba de 30 primeros primos
primer_iter = primo_gen()

for i in range(100):
    print primer_iter.next()
