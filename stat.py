import math
import collections as cl

class Stat():
  def __init__(self, array):
    self.array = array
  
  def average(self):
    length = len(self.array)
    whole = 0
    for i in self.array:
      whole += i
    whole /= length
    return whole

  def mode(self):
    n = len(self.array) 
    data = cl.Counter(self.array) 
    get_mode = dict(data) 
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
    if len(mode) == n: 
      return None
    else:
      return mode

  def median(self):
    self.array.sort()
    length = len(self.array)
    if length % 2 == 1:
      return self.array[math.ceil(length / 2) - 1]
    else:
      part1 = self.array[int(length / 2 - 1)]
      part2 = self.array[int(length / 2)]
      average = (part1 + part2) / 2
      return average

  def range(self):
    self.array.sort()
    length = len(self.array)
    mini = self.array[0]
    maxi = self.array[length - 1]
    return maxi - mini

  def max(self):
    self.array.sort()
    last = len(self.array) - 1
    return self.array[last]

  def min(self):
    self.array.sort()
    return self.array[0]