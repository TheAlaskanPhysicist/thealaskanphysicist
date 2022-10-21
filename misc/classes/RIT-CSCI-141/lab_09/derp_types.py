"""
Data Types for Derp the Interpreter

The Derp interpreter parses and evaluates prefix integer expressions 
containing basic arithmetic operators (*,//,-,+). It performs arithmetic with
integer operands that are either literals or variables (read from a 
symbol table).  It dumps the symbol table, prints the infix expression with 
parentheses to denote order of operation, and evaluates the expression to
print the result.

Author: CS@RIT.EDU
"""

from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True)
class LiteralNode:
    """Represents an operand node
    """

    val: int


@dataclass(frozen=True)
class VariableNode:
    """Represents a variable node
    """

    name: str
    

@dataclass(frozen=True)
class MathNode:
    """Represents a mathematical operation
    left:  reference to a LiteralNode, a VariableNode, or another MathNode
    operator: string in the set { '+', '-', '*', '//' }
    right: reference to a LiteralNode, a VariableNode, or another MathNode
    """

    left: Union['MathNode', LiteralNode, VariableNode]
    operator: str
    right: Union['MathNode', LiteralNode, VariableNode]

