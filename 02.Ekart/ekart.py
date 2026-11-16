products = {
    "laptop":{
        "brand":"asus",
        "price":56000,
        "quantity": 9
    },
    "face wash":{
        "brand":"cetaphil",
        "price":789,
        "quantity":15
    },
    "bag":{
        "brand":"gear",
        "price":1500,
        "quantity":40
    },
    "shoe":{
        "brand":"nike",
        "price":3560,
        "quantity":10
    }

}
while True :
 available = input("Enter yout product name: ")
 if available in products:
  print(f"product:{available} is available in our site\nthe price is: {products[available]['price']:>10}\nbrand name: {products[available]['brand']:>12}\navailable quantity:{products[available]['quantity']:>3}")

 else:
  print(f"this product not available in our site")

 try:
   x = int(input("Enter the quantity:"))
   if x <= 0:
     print("please Enter at least one item")

   elif x <= products[available]['quantity']  :
     print(f"\nYour product {available} is added with quantity {x}")
     buy = input("can you confirm you purchase  yes/No : ")
     if buy == "yes":
      products[available]['quantity'] = products[available]['quantity'] - x
      print("the avaliable quantity is now:",products[available]['quantity'])
      total= x * (products[available]['price'])
      print(f"your bill is : {total:,}")
      more = input("Do you want to buy other prodcuts:")
      if more == "yes":
         print("ok here we go ")

      else:
       break

     else:
      print("thank you for cheacking out")

   else:
     print("this much qunatity is not available now")

 except ValueError:
  print("please enter value in number")
 finally:
  print("\n\"!!!!!you always welcome to our E - cart!!!!!\"")