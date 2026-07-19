from abc import ABC, abstractmethod
from quantum_code_basis import QuantumCodeBasis
from src.core.optimization.variational_parameters import VariationalParameters
from src.core.input.problem_statement import ProblemStatement
from quantum_code import QuantumCode


class QuantumCodeBuilder(ABC):
    """
    A module that collects a quantum code based on the input data,
    i.e., the value of the variational parameters and the initial optimization problem,
    depending on the established basis.

    Attributes
    ----------
    code_template:
        A quantum circuit template that will be used for compilation to avoid multiple code builds.
    """

    # TODO: code_template is the template for compiling.
    def __init__(self, code_template: str):
        ...

    @abstractmethod
    def build(
            self,
            basis: QuantumCodeBasis,
            parameters: VariationalParameters,
            objective: ProblemStatement
    ) -> QuantumCode: ...