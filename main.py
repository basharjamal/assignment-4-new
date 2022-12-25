print("Q2 ")
from math import ceil, floor
import math

first_number=(input("enter a number"))
if first_number.isdigit():
    operation=(input("choose one of this operations\n1- +\n2- -\n3- *\n4- /\n5- ^\n6- %"))
    if operation == "+"or operation == "1":
      second_number = (input("enter a second number"))
      if second_number.isdigit():
          result=int(first_number)+int(second_number)
          choice = input("choose one of these line\n1- normal round\n2- ceiling\n3- floor\n4- integer\n5- exit")
          if choice == "1":
              result = round(result)
              print("result= ", result)
          elif choice == "2":
              result = ceil(result)
              print("result= ", result)
          elif choice == "3":
              result = floor(result)
              print("result= ", result)
          elif choice == "4":
              result = int(result)
              print("result= ", result)
          elif choice == "5":
              exit()
      else:
          print("you must enter a number only")
    elif operation == "-"or operation == "2":
      second_number = (input("enter a second number"))
      if second_number.isdigit():
          result=int(first_number)-int(second_number)
          choice = input("choose one of these line\n1- normal round\n2- ceiling\n3- floor\n4- integer\n5- exit")
          if choice == "1":
              result = round(result)
              print("result= ", result)
          elif choice == "2":
              result = ceil(result)
              print("result= ", result)
          elif choice == "3":
              result = floor(result)
              print("result= ", result)
          elif choice == "4":
              result = int(result)
              print("result= ", result)
          elif choice == "5":
              exit()
      else:
          print("you must enter a number only")
    elif operation == "*"or operation == "3":
      second_number = (input("enter a second number"))
      if second_number.isdigit():
          result=int(first_number)*int(second_number)
          choice = input("choose one of these line\n1- normal round\n2- ceiling\n3- floor\n4- integer\n5- exit")
          if choice == "1":
              result = round(result)
              print("result= ", result)
          elif choice == "2":
              result = ceil(result)
              print("result= ", result)
          elif choice == "3":
              result = floor(result)
              print("result= ", result)
          elif choice == "4":
              result = int(result)
              print("result= ", result)
          elif choice == "5":
              exit()
      else:
          print("you must enter a number only")
    elif operation == "/"or operation == "4":
      second_number = (input("enter a second number"))
      if second_number.isdigit():
          result=int(first_number)/int(second_number)
          choice=input("choose one of these line\n1- normal round\n2- ceiling\n3- floor\n4- integer\n5- exit")
          if choice == "1":
             result=round(result)
             print ("result= ",result)
          elif choice == "2":
              result = ceil(result)
              print("result= ", result)
          elif choice == "3":
              result = floor(result)
              print("result= ", result)
          elif choice == "4":
              result = int(result)
              print("result= ", result)
          elif choice == "5":
              exit()
      else:
          print("you must enter a number only")
    elif operation == "^"or operation == "5":
      second_number = (input("enter a second number"))
      if second_number.isdigit():
          result=int(first_number)**int(second_number)
          choice = input("choose one of these line\n1- normal round\n2- ceiling\n3- floor\n4- integer\n5- exit")
          if choice == "1":
              result = round(result)
              print("result= ", result)
          elif choice == "2":
              result = ceil(result)
              print("result= ", result)
          elif choice == "3":
              result = floor(result)
              print("result= ", result)
          elif choice == "4":
              result = int(result)
              print("result= ", result)
          elif choice == "5":
              exit()
      else:
          print("you must enter a number only")
    elif operation == "%"or operation == "6":
      second_number = (input("enter a second number"))
      if second_number.isdigit():
          result=int(first_number)%int(second_number)
          choice = input("choose one of these line\n1- normal round\n2- ceiling\n3- floor\n4- integer\n5- exit")
          if choice == "1":
              result = round(result)
              print("result= ", result)
          elif choice == "2":
              result = ceil(result)
              print("result= ", result)
          elif choice == "3":
              result = floor(result)
              print("result= ", result)
          elif choice == "4":
              result = int(result)
              print("result= ", result)
          elif choice == "5":
              exit()
      else:
          print("you must enter a number only")
    else:
        print("enter one of these operations (+ - * / ^ %)")
else:
    print("you must enter a number only")