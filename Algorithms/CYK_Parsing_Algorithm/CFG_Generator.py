"""Context Free Grammar G is in Chomsky Normal Form (CNF) if each production within G is of the form:

    A –> BC,        ( with at most two non-terminal symbols on the RHS )
    A –> a,         ( one terminal symbol on the RHS) """

"""Our CFG will look like this:"""
"""S   -->  CB | AB 
   A  -->  a
   B  -->  b
   C -->  AS """

""""Generate and return R, The rules of our CFG in CNF"""
def Generate_CFG_Grammar():
   
   # Rules of the grammar
   R = {
      "S": [["C", "B"], ["A","B"]],
      "A": [["a"]],
      "B": [["b"]],
      "C": [["A", "S"]]
      }
   return R