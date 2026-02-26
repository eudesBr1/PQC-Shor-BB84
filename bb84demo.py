import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from numpy.random import randint

def simulation_complete_5_qubits(interception=True):
    n = 5
    # On crée un circuit avec 5 qubits et 5 bits classiques pour Bob
    qc = QuantumCircuit(n, n)
    
    # 1. Alice génère ses choix
    alice_bits = randint(2, size=n)
    alice_bases = randint(2, size=n) # 0=Z, 1=X
    
    # 2. Alice prépare les qubits
    for i in range(n):
        if alice_bits[i] == 1:
            qc.x(i)  # Porte X pour le bit 1
        if alice_bases[i] == 1:
            qc.h(i)  # Porte H pour la base X
    qc.barrier(label="ALICE")

    # 3. Eve intercepte (si activé)
    if interception:
        eve_bases = randint(2, size=n)
        for i in range(n):
            if eve_bases[i] == 1: qc.h(i)
            # Eve mesure mais on ne peut pas "lire" le résultat ici sans casser le circuit
            # On simule sa mesure par une barrière
            qc.barrier(i) 
            if eve_bases[i] == 1: qc.h(i)
        qc.barrier(label="EVE")

    # 4. Bob mesure
    bob_bases = randint(2, size=n)
    for i in range(n):
        if bob_bases[i] == 1:
            qc.h(i)
    qc.measure(range(n), range(n))

    # --- EXÉCUTION DE LA SIMULATION ---
    backend = Aer.get_backend('qasm_simulator')
    job = backend.run(transpile(qc, backend), shots=1, memory=True)
    resultat_brut = job.result().get_memory()[0] # Résultat sous forme '10101'
    bob_results = [int(b) for b in reversed(resultat_brut)] # On remet dans l'ordre q0, q1...

    # --- SIFTING (Comparaison des bases) ---
    indices_communs = [i for i in range(n) if alice_bases[i] == bob_bases[i]]
    cle_alice = [alice_bits[i] for i in indices_communs]
    cle_bob = [bob_results[i] for i in indices_communs]

    # --- AFFICHAGE DES RÉSULTATS ---
    print("--- RÉSULTATS DE LA SIMULATION ---")
    print(f"Bits d'Alice : {alice_bits}")
    print(f"Bases Alice  : {['Z' if b==0 else 'X' for b in alice_bases]}")
    print(f"Bases Bob    : {['Z' if b==0 else 'X' for b in bob_bases]}")
    print(f"Bits de Bob  : {np.array(bob_results)}")
    print(f"\nClé finale Alice : {cle_alice}")
    print(f"Clé finale Bob   : {cle_bob}")
    
    # Calcul d'erreur sur ces 5 qubits
    erreurs = sum(1 for a, b in zip(cle_alice, cle_bob) if a != b)
    print(f"Erreurs détectées : {erreurs}")

    # --- GÉNÉRATION DU SCHÉMA ---
    qc.draw(output='mpl', filename='bb84_5qubits_complet.png')
    print("\n✅ Schéma 'bb84_5qubits_complet.png' généré.")

if __name__ == "__main__":
    simulation_complete_5_qubits(interception=True)