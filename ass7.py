# 1. დაწერეთ პითონის პროგრამა, რომელიც ცვლის tuple-ის ბოლო მნიშვნელობას სიაში.
# ნიმუშების ასი: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# data = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# result = []

# for i in data:
#     temp = []
#     index = 0
#     for j in i:
#         temp.append(j)
#         index += 1
#     temp[index - 1] = 100  
#     result.append(temp)

# print(result)



# # 2.max და min ფუნქციის გარეშე იპოვეთ სეტში არსებული უმცირესი და უდიდესი მონაცემი.


set1 = {10, 20, 4, 45, 99}
max = 0
min = 0

def main():
    print("Maximum number is:", maxval(set1))
    print("Minimum number is:", minval(set1))

def maxval(set):
    global max
    for x in set:
        if x > max:
            max = x 
    
    return max

def minval(set):
    global max
    global min
    min = max

    for y in set:
        if y < min:
            min = y
    return min

main()

# #ახალ დაწერილი მაქვს, კვირა ამერია და მეგონა დეფინიციით უნდა დაგვეწერა, 
# #მაგრამ მუშაობს იდეალურად.

# # 3.დაწერეთ პითონის პროგრამა, რათა გამოვთვალოთ რიცხვების საშუალო მნიშვნელობა მოცემულ ტოპებში.
# input = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# output = [30.5, 34.25, 27.0, 23.25]

# nums = ((10, 10, 10, 12),
#         (30, 45, 56, 45),
#         (81, 80, 39, 32),
#         (1, 2, 3, 4))


# averages = []

# num_columns = 0
# for _ in nums[0]:
#     num_columns += 1

# for i in range(num_columns):
#     total = 0
#     count = 0
#     for row in nums:
#         total += row[i]
#         count += 1
#     average = total / count
#     averages.append(average)

# print(averages)








