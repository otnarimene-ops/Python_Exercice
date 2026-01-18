# combinations.py

from math import factorial

def trivial_comb(n, k):
    """Calculer le nombre de façons de choisir k éléments parmi n"""
    return factorial(n) // (factorial(k) * factorial(n - k))

# Exemple d'utilisation
if __name__ == "__main__":
    n = 5
    k = 3
    print("C(5,3) =", trivial_comb(n, k))
    # combinations.py

def fact_iterative(n):
    """Calcul du factoriel de façon itérative"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def comb_iterative(n, k):
    """Calcul des combinaisons C(n,k) en utilisant fact_iterative"""
    return fact_iterative(n) // (fact_iterative(k) * fact_iterative(n - k))

# Exemple d'utilisation
if __name__ == "__main__":
    n = 5
    k = 3
    print("C(5,3) avec factorial itératif =", comb_iterative(n, k))
    # combinations.py

def fact_recursive(n):
    """Calcul du factoriel de façon récursive"""
    if n <= 1:
        return 1
    return n * fact_recursive(n - 1)

def comb_recursive(n, k):
    """Calcul des combinaisons C(n,k) en utilisant fact_recursive"""
    return fact_recursive(n) // (fact_recursive(k) * fact_recursive(n - k))

# Exemple d'utilisation
if __name__ == "__main__":
    n = 5
    k = 3
    print("C(5,3) avec factorial récursif =", comb_recursive(n, k))



