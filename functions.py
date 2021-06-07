def add(* numbers):
  whole = 0
  for i in numbers:
    whole += i
  return whole
  
def subtract(* numbers):
  whole = numbers[0]
  for i in range(1, len(numbers)):
    whole -= numbers[i]
  return whole
  
def multi(* numbers):
  whole = 1
  for i in numbers:
    whole *= i
  return whole
  
def div(* numbers):
  whole = numbers[0]
  for i in range(1, len(numbers)):
    whole /= numbers[i]
  return whole

def power(* numbers):
  whole = numbers[0]
  for i in range(1, len(numbers)):
    whole **= numbers[i]
  return whole

def mod(* numbers):
  whole = numbers[0]
  for i in range(1, len(numbers)):
    whole %= numbers[i]
  return whole

def checkPrime(number):
  factors = []
  if number == 1 or number == 0:
    return "None"
  elif number == 2:
    return "Prime"
  else:
    i = 2
    while i < number:
      if number % i == 0:
        factors.append(i)
        return "Composite"
        break
      i += 1
    if len(factors) == 0:
      return "Prime"

def gcf(num1, num2):
  numbers = []
  for i in range(num1 + 1):
    if i == 0:
      continue
    if num1 % i == 0 and num2 % i == 0:
      numbers.append(i)
  numbers.sort()
  return numbers[len(numbers) - 1]
  
def lcm(num1, num2):
  numbers = []
  for i in range(num1 * num2 + 1):
    if i == 0:
      continue
    if i % num1 == 0 and i % num2 == 0:
      numbers.append(i)
  numbers.sort()
  return numbers[0]

def fib(last):
  numbers = list(range(last))
  for i in range(2, last):
    numbers[i] = numbers[i - 1] + numbers[i - 2]
  return numbers[len(numbers) - 1] 

def fibArray(length):
  numbers = list(range(length))
  for i in range(2, length):
    numbers[i] = numbers[i - 1] + numbers[i - 2]
  return numbers

def tribo(last):
  numbers = list(range(last))
  for i in range(3, last):
    numbers[i] = numbers[i - 1] + numbers[i - 2] + numbers[i - 3]
  return numbers[len(numbers) - 1]

def triboArray(length):
  numbers = list(range(length))
  for i in range(3, length):
    numbers[i] = numbers[i - 1] + numbers[i - 2] + numbers[i - 3]
  return numbers