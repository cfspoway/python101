# Homework #08
# Calculator

while True:
   print("\nPlease select an operation:")
   print("1.Add")
   print("2.Subtract")
   print("3.Multiply")
   print("4.Divide")
   print("5.Quit")

   choice = input("Enter your choice(1/2/3/4/5):")

   if choice != '1' and choice != '2' and choice != '3' and choice != '4':
       print('Thank you, see you next time')
       break
       
   else:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))

      if choice == '1':
         print(num1,"+",num2,"=", str(num1+num2))

      elif choice == '2':
          print(num1,"-",num2,"=", str(num1-num2))

      elif choice == '3':
          print(num1,"*",num2,"=", str(num1*num2))

      else:
          while num2 == 0:
             num2 = float(input('Denumerator must be non-zero, please input again: '))
          print(num1,"/",num2,"=", str(num1/num2))

