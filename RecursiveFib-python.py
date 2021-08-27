import time as t
start = t.time

# Recursive Fibonacci calculator -> PYTHON

# Input should be an integer
def fibFunc(x):
  if( x==0 or x==1 ):
    return x
  return fibFunc(x-1)+fibFunc(x-2)
end = t.time

total = start-end
if( total<0 ):
  total = total*-1
  
# Outputting run-time performance for comparison(s) with other files in repo
print('This specific run-time performance is ', total)
  






