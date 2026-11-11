users =  {
    45561 : {
        "username" : "amit",
        "password" : 4586,
        "balance"  : 50000
    },
    894562:{
        "username" : "rakshi",
        "password" : 8463,
        "balance"  : 896140
    },
    789412: {
      "username": "jhon",
      "password": 1248,
      "balance" : 550160
    }
}




found = False
try:
  acc = int(input("Enter yout account number:"))

  for i in users:
    if i == acc:
      found = True
      print(f"hello  \"{users[acc]['username']}\"")
      x = int(input("what service you wanted\n1.cheack balance\n2.withdrawl amount\nselect the number: "))
      if x == 1 :
        pin = int(input("Please Enter Your pin:"))
        if pin == users[acc]['password']:
           print(f"your balance is : {users[acc]['balance']}")
      elif x == 2:
           pin = int(input("Please Enter Your pin:"))
           if pin == users[acc]['password']:
             withdrawl = int(input("Enter the amount you want to withdrawl:"))
             if withdrawl > 0:
              print("yout withdrawl amount",withdrawl,"is in process")
              yy =  users[acc]['balance'] = users[acc]['balance'] - withdrawl
              print("your current balance is:",yy)
             else:
               print("number should be greater than 0")
           else:
            print("incorrect password")
            break
  if found == False:
      print("invalid account number")

except ValueError:
  print("please select only numbers")
