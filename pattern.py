class Pattern():
  def __init__(self, patterntype):
    self.patterntype = patterntype
  
  def pattern(self, start, jump, length):
    array = []
    if self.patterntype == "add":
      for i in range(length):
        array.append(start)
        start += jump
    elif self.patterntype == "subtract":
      for i in range(length):
        array.append(start)
        start -= jump
    elif self.patterntype == "multiply":
      for i in range(length):
        array.append(start)
        start *= jump
    elif self.patterntype == "divide":
      for i in range(length):
        array.append(start)
        start /= jump    
    elif self.patterntype == "exponent":
      for i in range(length):
        array.append(start)
        start **= jump
    return array