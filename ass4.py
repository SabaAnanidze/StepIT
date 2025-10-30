# 1. დაწერეთ პროგრამა, რომელიც იღებს სტრიქონს, 
# როგორც შეყვანას და აბრუნებს True-ს, თუ ის პალინდრომია
# (პალინდრომი არის ისეთი ტექსტი, რომელიც მარცხნიდანაც და მარჯვნიდანაც ერთნაირად იკითხება),
# თუ არა მაშინ False. მაგალითად, თუ შევიყვანთ "level", ფუნქციამ უნდა დააბრუნოს True.

text = str(input("Enter a string: ")).lower().replace(" ", "") #tavs vizgvevt Level, Level  , shemtxvevebisgan
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text

while True :
    if text == reversed_text:
        print("True")
        break
    else:
        print("False")
        break
# es sheidzleboda ufro mokledac...

# 2. დაწერეთ პროგრამა, რომელიც მომხმარებელს სთხოვს შეიყვანოს ტექსტი,
# ტექსტის სიმბოლოები გადაყავს
# შესაბამის ASCII სტანდარტში და გვიბეჭდავს ამ რიცხვების თანმიმდევრობას


text = input("Enter a text: ")
for char in text:
    print(ord(char), end=" ")

# 3.დაწერეთ სკრიპტი, რომელიც მომხმარებელს მოსთხოვს შეიყვანოს სიტყვა,
# შემდეგ კი შეყვანილ სიტყვას ბოლოში დაუმატებ ing-ს.
# თუკი მომხმარებლის მიერ შეყვანილი სიტყვა ისედაც მთავრდება ing-ზე - მაშინ დაუმატებს ly-ს. 
# მაგალითად: თუკი მომხარებელმა შეიყვანტა სიტყვა test;
# - უნდა დაიბეჭდოს testing; თუკი შეიყვანა string; - უნდა დაიბეჭდოს stringly
# ჩაწერეთ ეს while loop-ში და იყოს გაშვებული მანამ სანამ მომხმარებელი არ ჩაწერს stop-ს

while True:
    word = input("Enter a word (or type 'stop' to end): ")
    if word.lower() == "stop":
        break  # stop the loop
    if word.endswith("ing"):
        print(word + "ly")
    else:
        print(word + "ing")
    

