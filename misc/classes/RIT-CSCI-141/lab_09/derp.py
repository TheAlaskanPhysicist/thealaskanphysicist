"""
141 Tree Lab - Derp the Interpreter

The Derp interpreter parses and evaluates prefix integer expressions 
containing basic arithmetic operators (*,//,-,+). It performs arithmetic with
integer operands that are either literals or variables (read from a 
symbol table).  It dumps the symbol table, prints the infix expression with 
parentheses to denote order of operation, and evaluates the expression to
print the result.

Author: CS@RIT.EDU

Author: Stanley Goodwin
"""

from derp_types import *        # dataclasses for the Derp interpreter


##############################################################################
# parse
############################################################################## 
    
def parse(tokens):
    """parse: list(String) -> Node
    From a prefix stream of tokens, construct and return the tree,
    as a collection of Nodes, that represent the expression.
    precondition: tokens is a non-empty list of strings
    """
    if not tokens:
        raise IndexError

    char = tokens.pop(0)
    if char.isdigit():
        return LiteralNode(int(char))
    elif char.isidentifier():
        return VariableNode(char)
    elif char in {"+", "-", "*", "//"}:
        left = parse(tokens)
        right = parse(tokens)
        return MathNode(left, char, right)
    else:
        raise ValueError

            
##############################################################################
# infix
##############################################################################
        
def infix(node):
    """infix: Node -> String 
    Perform an inorder traversal of the node and return a string that
    represents the infix expression.
    precondition: node is a valid derp tree node
    """
    if isinstance(node, LiteralNode):
        return str(node.val)
    elif isinstance(node, VariableNode):
        return node.name
    elif isinstance(node, MathNode):
        operator = node.operator
        left = node.left
        right = node.right
        return f"({infix(left)} {operator} {infix(right)})"
 
##############################################################################
# evaluate
##############################################################################    
      
def evaluate(node, sym_tbl):
    """evaluate: Node * dict(key=String, value=int) -> int 
    Return the result of evaluating the expression represented by node.
    Precondition: all variable names must exist in sym_tbl
    precondition: node is a valid derp tree node
    """
    if isinstance(node, LiteralNode):
        return node.val
    elif isinstance(node, VariableNode):
        return sym_tbl[node.name]
    elif isinstance(node, MathNode):
        operator = node.operator
        left_val = evaluate(node.left, sym_tbl)
        right_val = evaluate(node.right, sym_tbl)
        if operator == "+":
            return left_val + right_val
        elif operator == "-":
            return left_val - right_val
        elif operator == "*":
            return left_val * right_val
        elif operator == "//":
            return left_val // right_val
        else:
            raise ValueError

##############################################################################
# read_file
##############################################################################

def read_file(filename: str) -> dict:
    """read_file: filename -> dict
    Return the dictionary of variables -> values.
    Precondition: File name must be valid file.
    """
    symbol_table = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if line != "\n":
                temp = line.strip().split()
                symbol_table[temp[0]] = int(temp[1])
    return symbol_table

##############################################################################
# main
##############################################################################
                     
def main():
    """main: None -> None
    The main program prompts for the symbol table file, and a prefix 
    expression.  It produces the infix expression, and the integer result of
    evaluating the expression"""
    
    print("Hello Herp, welcome to Derp v1.0 :)")
    
    in_file = input("Herp, enter symbol table file: ")
    
    # CONSTRUCT AND DISPLAY THE SYMBOL TABLE HERE
    print("\nDerping the symbol table (variable name => integer value)...")
    value_dict = read_file(in_file)
    for var, val in value_dict.items():
        print(f"{var} => {val}")
    
    print("\nHerp, enter prefix expressions, e.g.: + 10 20 (ENTER to quit)...")
    
    # input loop prompts for prefix expressions and produces infix version
    # along with its evaluation
    while True:
        prefix_exp = input("derp> ")
        if prefix_exp == "":
            break
            
        # STUDENT: GENERATE A LIST OF TOKENS FROM THE PREFIX EXPRESSION
        tokens = prefix_exp.strip().split()
        
        # STUDENT: CALL parse WITH THE LIST OF TOKENS AND SAVE THE ROOT OF
        tree_expression = parse(tokens)
            
        # STUDENT: GENERATE THE INFIX EXPRESSION BY CALLING infix AND SAVING
        infix_expression = infix(tree_expression)

        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.
        print(f"Derping the infix expression: {infix_expression}")
        
        # STUDENT: EVALUTE THE PARSE TREE BY CALLING evaluate AND SAVING THE
        evaluation_val = evaluate(tree_expression, value_dict)

        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.
        print(f"Derping the evaluation: {evaluation_val}")
         
    print("Goodbye Herp :(")


if __name__ == "__main__":
    main()
