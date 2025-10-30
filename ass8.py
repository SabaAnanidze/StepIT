# 1. დაწერეთ პითონის ფუნქცია რომელიც მიიღებს არგუმენტს, პირობითად num_1 და num_2-ს შემდეგ
# ამის და მიხედვით შექმნის ლისტს და საბოლოოდ დაგვიბრუნებს ლისტში არსებული ყველა ობიექტის კვადრატს
    

def square(*args): # square(1,5,6,7,4,2,3)
    list_result = []
    for number in args:
        list_result.append(number*number)

    return list_result


print(square(1,5,6,7,4,2,3))


