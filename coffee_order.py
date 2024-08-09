#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SHARJEEL
#
# Created:     04/02/2024
# Copyright:   (c) SHARJEEL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------


drinks={
 "latte":{
  "items":{
  "water":100, "coffee":50, "milk": 120},
  "cost":50
  },

  "black coffee":{
   "items":{
    "water":120, "coffee":100, "milk":200},
    "cost":100
    },

    "ice coffee":{
    "items":{
     "water":150, "coffee":250, "milk":250},
     "cost":100
    }


}

resourses={
"water":100,
"coffee":500,
"milk":500,
}

profit=0

def menu():
    print("1. LATTE -- Rs 50 only")
    print("2. BLACK COFFEE -- Rs 120 only")
    print("3. ICE COFFEE -- Rs 100 only")


def check_resource(choice):
    value=True
    for i in choice:
        if choice[i] > resourses[i] :
            value=False
    return value



def order(choice):
    for i in choice:
        resourses[i] -= choice[i]

    print("ENJOY YOUR COFFEE....")

def payment(pay,real_price):
    pay=int(pay)
    if pay==real_price:
        return True
    elif pay>real_price:
        print(f"YOUR CHANGE {pay-real_price}")
        return True
    else:
        return False




print("ENTER '1' TO ORDER")
print("ENTER '2' TO CHECK RESOUSES AVABILITY")
print("ENTER '3' TO CHECK PROFIT")
enter=input("ENTER CHOICE: ")
enter.lower()
while enter=='1' or enter=='2' or enter=='3':

    if enter=='1':
        print("+++++++++++++++++++++++++++++++++++++")
        menu()
        print("+++++++++++++++++++++++++++++++++++++\n")
        choice=input("ENTER COFFEE NAME: ")
        choice.lower()
        print(choice)
        if choice=="latte" or choice=="black coffee" or choice=="ice coffee":
            coffee_type=drinks[choice]
            return_value=check_resource(coffee_type["items"])

            if return_value==True:
                #-------------
                pay=input("ENTER PAYMENT: ")
                payment_value=payment(pay,drinks[choice]["cost"])
                if(payment_value)==True:
                   print("COFFEE IN MAKINK PLEASE WAIT....")
                   order(coffee_type["items"])
                   profit += drinks[choice]["cost"]
                else:
                    print("INSUFFICIENT BALANCE")

            else:
                print("NOT POSSIBLE RESOURSES NOT AVALIABLE....")
        else:
            print("ENTER RIGHT OPTION....")

    if enter=='2':
        print("+++++++++++++++++++++++++++++++++++++")
        for key,val in resourses.items():
            print(key, ':', val)

    if enter=='3':
        print("+++++++++++++++++++++++++++++++++++++")
        print(f"YOU MAKE PROFIT {profit}")

    print("+++++++++++++++++++++++++++++++++++++++++++\n")
    print("ENTER '1' TO ORDER")
    print("ENTER '2' TO CHECK RESOUSES AVABILITY")
    print("ENTER '3' TO CHECK PROFIT")
    print("+++++++++++++++++++++++++++++++++++++++++++")
    enter=input("ENTER IF YOU WANT MORE: ")




