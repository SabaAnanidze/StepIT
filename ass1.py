'''
დაწერეთ პროგრამა რომელიც 
კითხულობს სამ მთელ რიცხვს 
და ეკრანზე(ტერმინალში) გამოაქვს მათი ჯამი.
'''
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))

numsum = num1 + num2 + num3
print("The sum of the three numbers is:", numsum)




'''
დაწერეთ პროგრამა, რომელიც გარდაქმნის ტემპერატურას ცელსიუსიდან ფარენჰეიტში.
გამოიყენეთ ცვლადი ცელსიუსის ტემპერატურის შესანახად,
შეასრულეთ კონვერტაცია ფორმულის გამოყენებით
(ცელსიუსი * 9/5) + 32 და დაბეჭდეთ შედეგი.
'''

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
print("It will be", fahrenheit, "degrees Fahrenheit.")






'''
დაწერეთ პითონის პროგრამა, რომელიც იღებს 
მომხმარებლისგან კუბის 
გვერდის სიგრძეს და ითვლის კუბის 
ზედაპირის ფართობსაც და მოცულობასაც და შემდეგ 
ამობეჭდავს ფართობსაც და მოცულობასაც.
'''
a = float(input("Enter the length of a side of your cube: "))

sur = 6 * (a ** 2)
vol = a ** 3

print("The surface area of the cube is:", sur)
print("The volume of the cube is:", vol)

