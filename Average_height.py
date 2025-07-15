# student_height= input("Enter a list of student height ").split()
# for n in range(0, len(student_height)):
#     student_height[n]=int(student_height[n])
# print(student_height)    

# total_height=0
# number=0
# for height in student_height:
#     total_height+=height
#     number+=1
# print(total_height)   
# avg_height= total_height/number
# print(round(avg_height))
 

students_heights= input("Enter the height of the students: ")  # give space after imput(eg: 12 14 16)
height=students_heights.split()      #creating a list of heights
sum=0
num=0
for i in height:
    sum=sum+int(i)
    num+=1
avg_height= sum/num
print(f"The average height of the student is {avg_height}")   
