from quantum_code_builder import QuantumCodeBuilder
from src.core.input.problem_statement import ProblemStatement
from src.core.optimization.variational_parameters import VariationalParameters
from src.core.quantum_code.quantum_code import QuantumCode
from src.core.quantum_code.quantum_code_basis import QuantumCodeBasis


class QAOAAnsatzBuilder(QuantumCodeBuilder):
    """
    The quantum code assembly module for the original QAOA algorithm ansatz developed by Farhi in 2014.

    Attributes
    ----------
    code_template:
        A quantum circuit template that will be used for compilation to avoid multiple code builds.
    """

    def __init__(self, code_template: str):
        super().__init__(code_template)

    def build(
            self,
            basis: QuantumCodeBasis,
            parameters: VariationalParameters,
            objective: ProblemStatement
    ) -> QuantumCode: ...
