#our calculator

a = input("Enter first number")
b = input("Enter second number")

a= int(a)
b= int(b)

print("-----------Press keys for the operator( + , - , * , / , %)-----------------")

opt= input("Enter The operator:")

if opt =="+":
    print(a+b)

elif opt =="-":
     print(b-a)

elif opt =="*":
     print(b*a)

elif opt =="/":
     print(b/a)

elif opt =="%":
     print(a%b)

else:
     print("Invalod Operation")