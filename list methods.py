marks=["english", 95, "chemistrty", 98]
marks.append("physics")

marks.append(97)
print(marks)

marks.insert(0,"math")
marks.insert(1,99)
print(marks)


print("math" in marks)
print(len(marks)/2)
marks.clear()
print(marks)

i=0
while i<len(marks):
    print(marks[i])
    print(marks[i+1])
    i=i+2 