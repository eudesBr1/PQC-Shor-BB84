import time
import numpy as np
from math import gcd, log2

def comparaison_performance(N):
    a = 2
    print(f"--- ANALYSE DE LA COMPLEXITÉ POUR N = {N} ---")

    # 1. TEMPS CLASSIQUE (Recherche réelle)
    start_classique = time.time()
    # On simule la recherche de période que doit faire un PC
    r_found = 0
    for r in range(1, N):
        if pow(a, r, N) == 1:
            r_found = r
            break
    end_classique = time.time()
    temps_classique = end_classique - start_classique

    # 2. TEMPS QUANTIQUE (Théorique)
    # La formule de Shor dit que le temps quantique est proportionnel à (log2(N))^3
    # On calcule le nombre de "portes" logiques nécessaires
    nb_qubits = int(log2(N))
    operations_quantiques = nb_qubits**3 
    
    # On simule un temps très court car c'est une seule opération de superposition
    temps_quantique_theorique = 0.000001 * operations_quantiques

    print(f"⏱️ Temps Classique (Réel sur ce PC) : {temps_classique:.6f} s")
    print(f"🚀 Temps Quantique (Estimé sur IBM Q) : {temps_quantique_theorique:.6f} s")
    
    speedup = temps_classique / temps_quantique_theorique if temps_quantique_theorique > 0 else 0
    print(f"📊 Facteur d'accélération théorique : x{speedup:.0f}")

# Test avec un nombre "moyen"
comparaison_performance(123456789)