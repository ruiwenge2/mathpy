import math

class Array:
  def __init__(self, array):
    self.array = array
  
  def add(self):
    whole = 0
    for i in self.array:
      whole += int(i)
    return whole

  def subtract(self):
    whole = self.array[0]
    for i in range(1, len(self.array)):
      whole -= int(self.array[i])
    return whole

  def multi(self):
    whole = 1
    for i in self.array:
      whole *= int(i)
    return whole

  def mod(self):
    whole = self.array[0]
    for i in range(1, len(self.array)):
      whole %= int(self.array[i])
    return whole
  
  def elemsqrt(self):
    root = lambda x: x ** 0.5
    newArr = map(root, self.array)
    return list(newArr)
    
  def elemcbrt(self):
    root = lambda x: x ** (1 / 3)
    newArr = map(root, self.array)
    return list(newArr)

  def elemroot(self, number):
    root = lambda x: x ** (1 / number)
    newArr = map(root, self.array)
    return list(newArr)

  def elemsq(self): 
    square = lambda x: x ** 2
    newArr = map(square, self.array)
    return list(newArr)
    
  def elemcb(self):
    cube = lambda x: x ** 3
    newArr = map(cube, self.array)
    return list(newArr)
    
  def elempow(self, number):
    power = lambda x: x ** number
    newArr = map(power, self.array)
    return list(newArr)
    
  def elemadd(self, number):
    add = lambda x: x + number
    newArr = map(add, self.array)
    return list(newArr)
    
  def elemmin(self, number):
    minus = lambda x: x - number
    newArr = map(minus, self.array)
    return list(newArr)
    
  def elemmulti(self, number):
    multiply = lambda x: x * number
    newArr = map(multiply, self.array)
    return list(newArr)
    
  def elemdiv(self, number):
    divide = lambda x: x / number
    newArr = map(divide, self.array)
    return list(newArr)
    
  def elemround(self):
    newArr = map(round, self.array)
    return list(newArr)
    
  def elemabs(self):
    newArr = map(abs, self.array)
    return list(newArr)
    
  def elemfloor(self):
    newArr = map(math.floor, self.array)
    return list(newArr)
    
  def elemceil(self):
    newArr = map(math.ceil, self.array)
    return list(newArr)