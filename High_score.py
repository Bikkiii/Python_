Scores=input("Enter the marks of the students: ")
List=Scores.split()
max=int(List[0])
for i in List:
    if max<int(i):
        max=int(i)
print(f"The max1imum value is {max}") 


# student_scores= input("Enter marks of student  ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n]=int(student_scores[n])
# print(student_scores)

# max=student_scores[0]
# for i in student_scores:
#     if max<i:
#         max=i
        
# print(f"The maximum socre is {max}")        
    