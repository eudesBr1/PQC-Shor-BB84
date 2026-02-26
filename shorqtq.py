import matplotlib.pyplot as plt
from qiskit import QuantumCircuit

def generer_schema_oral():
    qc = QuantumCircuit(5, 3)
    
    # 1. LANCER TOUTES LES POSSIBILITES
    for i in range(3):
        qc.h(i) 
    qc.x(4) 
    qc.barrier() 
    
    # 2. CALCULER LA CLE
    oracle_instructions = QuantumCircuit(2, name=" CALCUL RSA ")
    oracle_instructions.cx(0, 1) 
    oracle_gate = oracle_instructions.to_gate()
    qc.append(oracle_gate, [3, 4])
    qc.barrier()
    
    # 3. TRIER LES RESULTATS
    qc.h(0)
    qc.cp(1.57, 0, 1)
    qc.h(1)
    qc.barrier()
    
    # 4. LIRE LA REPONSE
    qc.measure([0, 1, 2], [0, 1, 2])

    qc.draw(output='mpl', filename='schema_shor_simple.png')
    print("Le schéma 'schema_shor.png' est prêt.")

if __name__ == "__main__":
    generer_schema_oral()