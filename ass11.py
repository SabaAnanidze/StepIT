# დაწერეთ პითონის პროგრამა ფაილში სიის შინაარსის ჩასაწერად

lst = ['red', 'Green', 'white', 'Black', 'Pink', 'Yellow']

with open('colors.txt', 'w') as file:

    for color in lst:
        file.write(color + '\n')


with open('colors.txt', 'r') as f:
    list1 = f.readlines()
    uppercase = 0 
    for i in list1:
        if i[0].isupper() == True:
            uppercase += 1

print(f"Uppercase letters: {uppercase}")
