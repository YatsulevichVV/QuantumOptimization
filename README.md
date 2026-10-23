# QuantumOptimization

## Description

Framework is presented as a platform in a no-code format.
This means that users of this application will not need to write code to implement the
quantum optimization algorithm.
The fundamental operation scheme of the framework is as follows. The program
receives a QUBO matrix for a certain problem as input. Then, based on the QUBO
matrix and certain values of the variational parameters, a quantum code is constructed
in the QASM language. This code is sent to a quantum computing emulator or
to a physical quantum processor. As a result of the emulation or direct quantum
computing, the average energy value is determined. The found energy value and the
variational parameters are passed to a certain optimizer.

## Launch

```commandline
$ pip install .
$ python main.py
quant-optimizer> config data/config.json
quant-optimizer> input data/matrix.json
quant-optimizer> optimize
quant-optimizer> run
```

## Developers

- [Yatsulevich Vladimir](https://t.me/modern_qc) — Junior researcher, Quantum Computation Laboratory, Moscow Independent Research Institute of Artificial Intelligence
(MIRAI).

- [Ksel Anna](...) — ML engineer, Laboratory of Quantum Computing, Innopolis University, Innopolis.