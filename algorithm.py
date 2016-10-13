def search(a,b,array):
  for x in array:
    if((a!=b) & (a > 0) & (b > 0) & (x > a) & (x < b)):
      return True
  return False
