from CYK_Parsing_Algorithm import CYK

def main():
   """Main"""
   # Driver Code
   print("\nGiven our Context Free Language L = { a^n b^n | n >= 1}\n")
   print("\nGiven our CFG G: \n S   -->  CB | AB \n A  -->  a \n B  -->  b \n C -->  AS ")

   # Given string
   w = "a a b b".split()
   
   # Function Call
   CYK(w)

   # Given string
   w = "a a a a b b b b".split()
   
   # Function Call
   CYK(w)

   # Given string
   w = "a b".split()
   
   # Function Call
   CYK(w)

if(__name__=='__main__'):
   main()