'''
1. დაწერეთ პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. 
შექმენით საწყისი ცვლადი total_sum =0, შეამოწმეთ რიცხვი თუ დადებითია, 
მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს.
 ესპროცესი გაგრძელდეს იქამდე სანამმომხმარებელი
 არ შეიყვანს 'sum' ტექსტს, რის შემდეგაც დაიბეჭდება
   შეყვანილი დადებითი რიცხვების ჯამი.'''


total_sum = 0
while True: 
    user_input = input("Enter a number (or 'sum' to finish): ") 
    if user_input == "sum":
     print("Total sum:", total_sum)
     break    
    elif int(user_input) >= 0:
     total_sum += int(user_input)
    
    else: 
     print("Invalid input, please enter a number or 'sum'.")
     continue


#2. გამოთვალეთ რიცხვების ჯამი, სანამ მომხმარებელი არ შეიყვანს 0-ს


# total_sum = 0
# while True: 
#     user_input = input("Enter a number (or '0' to finish): ") 
#     if int(user_input) == 0:
#      print("Total sum:", total_sum)
#      break    
#     elif int(user_input) > 0:
#      total_sum += int(user_input)
    
#     else: 
#      print("Invalid input, please enter a number or '0'.")
#      continue    



# # 3. რომელიც გამოიმუშავებს შემთხვევით რიცხვს 
# # 1-დან 10-მდე და სთხოვს მომხმარებელს გამოიცნოს რიცხვი.
# # პროგრამამ უნდა გამოიყენოს while loop, რათა გააგრძელოს 
# # მომხმარებლის ჩაფიქრებული რიცხვი,
# #  სანამ ისინი სწორად არ გამოიცნობენ რიცხვს. მიაწოდეთ უკუკავშირი მომხმარებელს,
# #  თუ მათი გამოცნობა ძალიან მაღალია ან ძალიან დაბალი.

import random

selected_int = random.randint(1,10)

while True: 
    user_input = int(input("Guess a number between 1 and 10: "))
    if (user_input)==selected_int:
        print("Nice, you are correct! ")
        break
    else:
        step = abs(user_input - selected_int) #modulistvis gamoviyene math librarydan es funkcia
        if step <=2:
            print("Hot!")
        elif step <=4:
            print("Warm!")
        elif step <=6:
            print("Cold!")
        else:
            print("Very Cold!")
    continue



