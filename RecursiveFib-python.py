# Recursive Fibonacci calculator -> PYTHON

# Input should be an integer
def fibFunc(x):
  if( x==0 or x==1 ):
    return x
  return fibFunc(x-1)+fibFunc(x-2)
  






