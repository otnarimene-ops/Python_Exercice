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

