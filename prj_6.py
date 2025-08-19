#Đề bài: Tính tổng của các số từ 1 đến N

num = int(input("Enter a number: "))
sum = 0

for i in range(num):
    sum = sum + i

print("The sum is ", sum)