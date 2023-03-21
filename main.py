# class Celsius:
#     def __init__(self,temperature):
#         self.__temperature =temperature
#     def get_temperature(self):
#         return self.__temperature
#     def set_temperature(self,temperature_1):
#         self.__temperature = temperature_1
#     def del_temperature(self):
#       del self.__temperature
#     temperature_property = property(get_temperature , set_temperature ,del_temperature)
# temparatura1=Celsius(15)
# temperatura2=Celsius(40)
# print(temperatura2.temperature_property)
# print (temparatura1.temperature_property)
#davaleba2
# class Bank_account:
#     def __init__(self,account_name , balance=0):
#         self.__account_name= account_name
#         self.__balance = balance
#     def get_accountname(self):
#         return self.__account_name
#     def set_acountname(self,accountname):
#         self.__account_name=accountname
#     def __str__ (self):
#         return f"gamarjoba:{self.__account_name},tqven angarishze gaqvt:{self.__balance}lari"
#     def deposit(self, amount):
#         self.__balance +=  amount
#         print(f"tamxis shetana shesrulda.amzhamad tqven angarishze gaqvt:{self.__balance}lari")
#     def withdraw(self,amount):
#         self.__balance -= amount
#         print(f"tanxis gamotana shesrulebulia maghamad tqven angarishze gaqvt angaishze :{self.__balance}lari")
# c1=Bank_account("gela","kvaratskhelia",)
# c1.deposit(input())
# c1.withdraw(input())
# print(c1)
#davaleba 3
class Point:
    def __init__(self,x , y):
        self.x = x
        self.y = y
p=Point(3,5)
p1=Point(6,9)
print(p)
print(p1)