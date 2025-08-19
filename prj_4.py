#Đề bài: Quản lý thông tin học sinh
strName = input("Enter your name: ")
nAge = int(input("Enter your age: "))
nMathScore = int(input("Enter your Math score: "))
nPhysicScore = int(input("Enter your Physic score: "))
nEngScore = int(input("Enter your English score: "))
nAvgScore = (nMathScore + nPhysicScore + nEngScore) / 3

print(strName, nAge, nMathScore, nPhysicScore, nEngScore, nAvgScore)