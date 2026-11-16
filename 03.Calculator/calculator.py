i = 0
multi = 1

while True:
  number = int(input("Type number: "))
  store = []
  fun = input()
 
  if fun == "+": 
      i = i + number
      store.append(i)
      print(store)
  elif fun == "-":
      i = number - i
      store.append(i)
      print(store)
  elif fun == "*":
      multi = multi * number
      store.append(multi)
      print(store)

  elif fun == "/":
      yes = int(input("Enter number: "))
      ohhk = number / yes
      store.append(ohhk)
      print(store)
  else:
      break
