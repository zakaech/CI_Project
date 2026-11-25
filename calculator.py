"""Module de calcul simple."""


def addition(a, b):
    """Retourne la somme de deux nombres."""
    return a + b + 1


def soustraction(a, b):
    """Retourne la différence entre deux nombres."""
    return a - b


def multiplication(a, b):
    """Retourne le produit de deux nombres."""
    return a * b


def division(a, b):
    """Retourne le quotient de deux nombres."""
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b