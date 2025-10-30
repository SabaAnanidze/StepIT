# 1. შექმენით list რომელიც შედგება თქვენთვის სასურველი ნებისმიერი ხუთი ელემენტისგან.
# # ამოარჩიეთ random-ულად რომელიმე ელემენტი და შეინახეთ ცვლადში. 
# # დაბეჭდეთ ყველა ელემენტი და მიეცით მომხმარებელს საშუალება 
# # გამოიცნოს შემთხვევითობის პრინციპით ამორჩეული ცვლადი.
# # გამოცნობის/ვერ გამოცნობის შემთხვევაში დაუბეჭდეთ შესაბამისი შეტყობინება



import random

names = ["saba", "giorgi", "nika", "luka", "dato"]
random_name = random.choice(names) # choice ighebs ert elements sequence-dan

while True: 
    user_input = input(f"{names}, Guess which name I chose: ").lower()
    if (user_input)==random_name:
        print("Nice, you are correct! ")
        break
    else:
        print("Incorrect, try again! ")


# # 2. დაწერეთ პითონის პროგრამა, 
# # რომელიც შექმნის ლისტს my_llist = [43, '22', 12, 66, 210, ["hi"]],
# # და შეასრულებს შემდეგ ნაბიჯებს:
# # a. დაბეჭდავს 210-ის ინდექს, თუ მერამდენე ინდექსზეა
# # b. დაამატებს ბოლო ელემენტში ტექსტს "hello" 
# # c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს ლისტს 
# # d. შექმენით ახალი ლისტი my_llist_2





my_list = [43, '22', 12, 66, 210, ["hi"]]
print(my_list.index(210)) # a

my_list[5].append("hello") # b 

my_list.pop(2)
print(my_list) # c
import copy
my_list_2 = copy.deepcopy(my_list)






# # 3. დაწერეთ პროგრამა რომელიც გააკეთებს კვადრატული 3x3 მატრიცის ტრანსპონირებას,
# # ტრანსპონირება ნიშნავს ინდექსების შებრუნებას, მაგ.
# # თუ გვაქვს ერთ-ერთი ჩანაწერი ინდექსით list[1][2], 
# # ტრანსპონირების შემდეგ მისი ინდექსი უნდა გახდეს list[2][1],
# # ასე ხდება ყველა ჩანაწერზე

# """
#  [1(0,0), 2(0,1), 3(0,2)],


#  [4(1,0), 5(1,1), 6(1,2)], 


#  [7(2,0), 8(2,1), 9(2,2)],

# """

matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]
result_matrix = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]
]

for i in range(len(matrix)):
    for j in range(len(matrix)):
        result_matrix[i][j] = matrix[j][i]

print(result_matrix)



