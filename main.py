print("Q1")
print("")
print("hello user")
name=input("enter your name")
age=input("enter your age")
address=input("enter your address")
if type(name)is str and age.isdigit() :
 print("Hello Mr/Ms ",name," age ",age," located in ",address,".\nthanks for beening one of our community,    Enjoy")
else:
    print("error occured")
    exit()