import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from numpy.random import randint

# --- FONCTION DE SIMULATION (ton code optimisé pour les stats) ---
def run_bb84_stats(n_qubits=20, interception=False):
    alice_bits = randint(2, size=n_qubits)
    alice_bases = randint(2, size=n_qubits)
    qubits = []
    for i in range(n_qubits):
        qc = QuantumCircuit(1, 1)
        if alice_bits[i] == 1: qc.x(0)
        if alice_bases[i] == 1: qc.h(0) # Base X
        qubits.append(qc)

    if interception:
        eve_bases = randint(2, size=n_qubits)
        for i in range(n_qubits):
            if eve_bases[i] == 1: qubits[i].h(0)
            qubits[i].measure(0, 0)
            if eve_bases[i] == 1: qubits[i].h(0)

    bob_bases = randint(2, size=n_qubits)
    bob_results = []
    backend = Aer.get_backend('qasm_simulator')
    for i in range(n_qubits):
        qc = qubits[i]
        if bob_bases[i] == 1: qc.h(0)
        qc.measure(0, 0)
        job = backend.run(transpile(qc, backend), shots=1, memory=True)
        bob_results.append(int(job.result().get_memory()[0]))

    # Sifting
    final_alice = [alice_bits[i] for i in range(n_qubits) if alice_bases[i] == bob_bases[i]]
    final_bob = [bob_results[i] for i in range(n_qubits) if alice_bases[i] == bob_bases[i]]
    
    # Calcul du taux d'erreur
    if len(final_alice) == 0: return 0
    err = sum(1 for a, b in zip(final_alice, final_bob) if a != b)
    return (err / len(final_alice)) * 100

# --- 1. GENERER LES GRAPHES DE MESURES ---
print("Calcul des statistiques en cours...")
nb_tests = 50
stats_sain = [run_bb84_stats(40, False) for _ in range(nb_tests)]
stats_espion = [run_bb84_stats(40, True) for _ in range(nb_tests)]

plt.figure(figsize=(10, 6))
plt.plot(stats_sain, label='Sans Espion (Sain)', color='green', marker='o', linestyle='')
plt.plot(stats_espion, label='Avec Espion (Eve)', color='red', marker='x', linestyle='')
plt.axhline(y=15, color='orange', linestyle='--', label='Seuil de détection')
plt.title("Comparaison des taux d'erreur BB84")
plt.xlabel("Numéro du test")
plt.ylabel("Taux d'erreur (%)")
plt.legend()
plt.savefig("graphique_bb84_stats.png")
print("✅ Graphique 'graphique_bb84_stats.png' généré.")

# --- 2. MONTRER LES PORTES (Les Bases) ---
# On crée un schéma qui montre comment on code un 0 et un 1 dans les deux bases
def dessiner_bases():
    # Base Z (Rectiligne)
    qc_z = QuantumCircuit(1, name="Base Z")
    qc_z.x(0) # Pour faire un '1'
    qc_z.draw(output='mpl', filename='porte_base_Z.png')
    
    # Base X (Diagonale)
    qc_x = QuantumCircuit(1, name="Base X")
    qc_x.x(0) # Pour faire un '1'
    qc_x.h(0) # LA PORTE HADAMARD : Change la base
    qc_x.draw(output='mpl', filename='porte_base_X.png')

dessiner_bases()
print("✅ Schémas des portes générés.")