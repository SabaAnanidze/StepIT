# შექმენით ბიბლიოთეკის მართვის ფუნქცია(ები)

# თქვენ უნდა შექმნათ ფუნქცია ან ფუნცქიები რომლის საშუალებითაც
# მომხმარებელი შეძლებს წიგნების დამატებას წაშლას პითონის პროგრამის შექმნა წიგნების პატარა ბიბლიოთეკის სამართავად.
#  პროგრამამ უნდა მისცეს მომხმარებლებს შემდეგი მოქმედებების შესრულება:
# 1. წიგნის დამატება,
# 2. წიგნის მოძებნა ავტორის მიხედვით
# 3. წიგნის მოძებნა სათაურის მიხედვით 
# ამისთვის აუცილებელია გამოიყენოთ ლექსიკონები

libr = {
    'harry_potter': 'jk_rowling',
    'the_hobbit': 'jrr_tolkien',
    'pride_and_prejudice': 'jane_austen',
}
#1 wignis damateba
def add_book(library, title, author):
    library[title] = author

def remove_book(library, title):
    if title in library:
        del library[title] #barem washlac gavuwerot

#2 wignis modzebna avtoris mixedvit
def find_by_author(library, author):
    result = []
    for title, writer in library.items(): 
        if writer == author:
            result.append(title)

    return result

#3 wignis modzebna satauris mixedvit
def find_by_title(library, title):
    return library.get(title, "Book not found") #defaulti ikneba "Book not found"

print(libr)

add_book(libr, 'to_kill_a_mockingbird', 'harper_lee')
print(libr)

remove_book(libr, 'the_hobbit')
print(libr)

print(find_by_author(libr, 'jk_rowling'))
print(find_by_title(libr, 'pride_and_prejudice'))
#mushaobs