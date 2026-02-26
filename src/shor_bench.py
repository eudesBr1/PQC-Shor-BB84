import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Création du dossier results
output_dir = "results"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Tailles de clés standards (en bits)
tailles_cles = np.array([512, 1024, 2048, 3072, 4096])

# Fonctions de complexité (simplifiées pour la démo)
# Classique : Croissance exponentielle (GNFS)
temps_classique = 10**(-3) * np.exp(0.02 * tailles_cles) 
# Quantique (Shor) : Croissance polynomiale (n^3)
temps_shor = 10**(-1) * (tailles_cles / 1024)**3 

print("Lancement du Benchmark Prédictif Shor")

# --- GÉNÉRATION DU TABLEAU DE RÉSULTATS ---
final_results = []
for i in range(len(tailles_cles)):
    cle = tailles_cles[i]
    t_c = temps_classique[i]
    t_s = temps_shor[i]
    
    # On convertit en unités lisibles (Secondes, Jours, Années...)
    status = "VULNÉRABLE" if t_c < 10**5 else "SÉCURISÉ"
    
    final_results.append(["Shor", f"RSA-{cle}", "Temps Classique (est.)", f"{t_c:.2e}", "sec"])
    final_results.append(["Shor", f"RSA-{cle}", "Temps Shor (théorique)", f"{t_s:.2e}", "sec"])
    final_results.append(["Shor", f"RSA-{cle}", "Statut Classique", status, "N/A"])

# Sauvegarde CSV
df = pd.DataFrame(final_results, columns=["Algo", "Config", "Metric", "Value", "Unit"])
df.to_csv("results/results_shor_complet.csv", index=False)

# generatuion du graphique
plt.figure(figsize=(10, 6))
plt.plot(tailles_cles, temps_classique, label="Ordinateur Classique (RSA)", color="red", linewidth=2, marker='o')
plt.plot(tailles_cles, temps_shor, label="Ordinateur Quantique (Shor)", color="green", linewidth=2, marker='s')

# On ajoute une ligne pour la "limite de l'âge de l'univers" ou du temps humainement acceptable
plt.axhline(y=3.15e7, color='black', linestyle='--', alpha=0.5) # 1 an en secondes
plt.text(500, 1e8, "Limite de sécurité (1 an)", color='black', alpha=0.7)

plt.yscale('log') # Indispensable pour voir la différence
plt.xlabel("Taille de la clé RSA (bits)")
plt.ylabel("Temps de calcul estimé (secondes / log)")
plt.title("Benchmark Shor : Pourquoi le Quantique brise RSA")
plt.grid(True, which="both", ls="-", alpha=0.3)
plt.legend()
plt.savefig("results/graphique_shor_benchmark.png")

print("Terminé ! Les fichiers 'results_shor_complet.csv' et 'graphique_shor_benchmark.png' sont disponibles dans le dossier 'results'.")