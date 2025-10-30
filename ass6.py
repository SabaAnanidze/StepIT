# # 1. შექმენი ლექსიკონი classroom, სადაც ინახება სტუდენტების ინფორმაცია:
# # {
# # "student1": {"name": "ანა", "age": 20, "grade": 9},
# # "student2": {"name": "ნიკო", "age": 22, "grade": 8},
# # "student3": {"name": "მარიამ", "age": 21, "grade": 10}
# # }
# # ა) დაბეჭდე თითოეული სტუდენტის სახელი და ქულა
# # ბ) იპოვე სტუდენტი, ვისაც ყველაზე მაღალი ქულა აქვს
# # გ) დაამატე ახალი სტუდენტი "student4" შენი მონაცემებით

mydict = {
    "student1": {"name": "ანა", "age": 20, "grade": 9},
    "student2": {"name": "ნიკო", "age": 22, "grade": 8},
    "student3": {"name": "მარიამ", "age": 21, "grade": 10}
    }
#a

print("================ 1 davaleba ==================\n")
print("================ a ==================") #eseni rom martivad iyos gasarchevi
for i in mydict:
    for j in mydict[i]:
        if j == "name" or j == "grade":
            print(mydict[i][j])

print("=====================================")
#b

print("================ b ==================")
max_grade = 0
top_student = ""
for i in mydict:
    if mydict[i]["grade"] > max_grade:
        max_grade = mydict[i]["grade"]
        top_student = mydict[i]["name"]
print(f"Top student is {top_student} with grade {max_grade}")

print("=====================================")
#c

print("================ c ==================")

mydict["student4"] = {"name": "საბა", "age": 19, "grade": 10}
print(mydict)

print("=====================================")


# # 2. დაწერე პროგრამა, რომელიც ითვლის რამდენჯერ ჩნდება თითოეული სიტყვა მოცემულ ტექსტში:
# # მაგალითად: text = "python is great and python is easy"

print("\n\n\n================ 2 davaleba ==================")
text = "python is great and python is easy"
word_count = {} 
words = text.split()
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

print("==============================================")