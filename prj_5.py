#Đề bài: Xếp loại học sinh dựa trên điểm trung bình

strName = input("Enter your name: ")
nAvgScore = float(input("Enter your average score: "))

print(strName, nAvgScore)

print("Xếp loại: ")
if (9.0 <= nAvgScore <= 10.0):
    print("Xuất sắc")
elif (8.0 <= nAvgScore <= 8.9):
    print("Giỏi")
elif (6.5 <= nAvgScore <= 7.9):
    print("Khá")
elif (5.0 <= nAvgScore <= 6.4):
    print("Trung bình")
elif (nAvgScore < 5.0):
    print("Yếu")

