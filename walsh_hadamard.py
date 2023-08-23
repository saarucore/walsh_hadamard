from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
import numpy as np

backend = Aer.get_backend('qasm_simulator')

shots = 1024

qc = QuantumCircuit()

q = QuantumRegister(1, 'q')
c = ClassicalRegister(2, 'c')

qc.add_register(q)
qc.add_register(c)

qc.h(q[0])
qc.id(q[0])
qc.measure(q[0], c[0])

job = execute(qc, backend=backend, shots=shots)
job_result = job.result()
print(job_result.get_counts(qc))
