# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of 
# pizza toppings until they enter a 'quit' value. As they enter each topping, 
# print a message saying you’ll add that topping to their pizza.



active = True
pizza = ''

print("Please Enter What Toppings That You Would Like On YOur Pizza: (Type 'quit' To Finish Order) \n")
while(active):
    pizza_toppings = input("What Topping Would You Like To Add(Type quit to Finish Order): ")
    
    if(pizza_toppings.lower() == 'quit'):
        active = False
    else:
        print("I Have Added " + pizza_toppings.title() + " To You Pizza!\n")
        pizza += pizza_toppings
        pizza += " "
print("Your Pizza Order Is Finished! Your Pizza With The Toppings: " + pizza + " Has Been Sent To Our Store!")