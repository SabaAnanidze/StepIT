'''
დაწერეთ პროგრამა, რომელიც მიიღებს მოსწავლის ქულებს,
 როგორც შეყვანის სახით და 
დაბეჭდავს მათ შესაბამის შეფასებას (A, B, C და ა.შ.) 
if-elif-else ოპერატორების გამოყენებით.
'''

a = float(input("type your score: "))

if a > 90 and a <= 100:
    print("A")
elif a > 80 and a <= 90:
    print("B")
elif a > 70 and a <= 80:
    print("C") 
elif a > 60 and a <= 70:
    print("D")
elif a > 50 and a <= 60:
    print("E")
else:
    print("You failed the the subject")


'''
დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი 
რიცხვის ლუწობასა და კენტობას. 
თუ რიცხვი ლუწია გამოიტანეთ ტექსტი
 ‘even ’თუ კენტია ‘odd’ 
'''

a = int(input("type your number: "))
if a == 0:
    print("zero")
elif a % 2 == 0:
    print("even")
else:
    print("odd")

# # '''
# # დაწერეთ პროგრამა
# #  რომელიც მომხმარებლის მიერ შეყვანილ ტექსტში მოძებნის სიტყვებს 
# #  “small”, “tall”, “middle”


# # a. თუ ტექსტში აღმოჩნდება რომელიმე მათგანი,
# #  დაბეჭდეთ პირველივე სიტყვა რაც აღმოჩნდება ტექსტში

# # b. თუ ტექსტში არცერთი სიტყვა მოიძებნა დაბეჭდეთ,
# #  რომ ტექსტში ეს სამი სიტყვა არ მოიძებნა
# # '''


text = input("Enter text: ")

if "small" in text:
    print("First found word: small")
elif "tall" in text:
    print("First found word: tall")
elif "middle" in text:
    print("First found word: middle")
else:
    print("No words 'small', 'tall', or 'middle' were found.")

