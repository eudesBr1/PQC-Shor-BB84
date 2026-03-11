import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from numpy.random import randint

# Création du dossier results
output_dir = "results"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def simulate_bb84(n, interception=False):
    alice_bits = randint(2, size=n)
    alice_bases = randint(2, size=n)
    bob_bases = randint(2, size=n)
    errors = 0
    common_bases = 0
    for i in range(n):
        if alice_bases[i] == bob_bases[i]:
            common_bases += 1
            if interception:
                # Eve crée statistiquement 25% d'erreurs sur les bases communes
                if randint(0, 100) < 25: errors += 1
    return (errors / common_bases * 100) if common_bases > 0 else 0

print("Lancement du Mega Benchmark BB84...")
n_tests = [10, 20, 40, 50]
final_results = []

plt.figure(figsize=(10, 6))

for n in n_tests:
    # On lance 100 fois pour chaque n
    sans_eve = [simulate_bb84(n, False) for _ in range(1000)]
    avec_eve = [simulate_bb84(n, True) for _ in range(1000)]
    
    # On ajoute au tableau CSV
    final_results.append(["BB84", f"{n} Qubits", "Moyenne (Sans Eve)", np.mean(sans_eve), "%"])
    final_results.append(["BB84", f"{n} Qubits", "Moyenne (Avec Eve)", np.mean(avec_eve), "%"])
    final_results.append(["BB84", f"{n} Qubits", "Max (Avec Eve)", np.max(avec_eve), "%"])

    # On prépare le graphique
    plt.scatter([n]*1000, avec_eve, color='red', alpha=0.3, label='Interception' if n==20 else "")
    plt.scatter([n]*1000, sans_eve, color='green', alpha=0.3, label='Sûr' if n==20 else "")

# Sauvegarde CSV
df = pd.DataFrame(final_results, columns=["Algo", "Config", "Metric", "Value", "Unit"])
df.to_csv("results/results_bb84_complet.csv", index=False)

# Finition graphique
plt.axhline(y=15, color='orange', linestyle='--', label='Seuil Alerte')
plt.title("Évolution du Taux d'Erreur selon le nombre de Qubits")
plt.xlabel("Nombre de Qubits envoyés")
plt.ylabel("Taux d'erreur (%)")
plt.legend(loc='upper right')
plt.grid(True, linestyle=':', alpha=0.6)
plt.savefig("results/graphique_bb84_mega.png")

print("Benchmark fini !  'results_bb84_complet.csv' et 'graphique_bb84_mega.png' dans le dossier 'results'.")

# legende anglais + variance

#faire autre algo qui fait le temps en fonction taille matrice