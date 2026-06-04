Total_students = 30
Attendence_count = 1
Presrent_student =0
Absent_student=0
while(Attendence_count<=Total_students):
    print("Student :",Attendence_count)
#input 
    status = input("Attendence :")
#input Checker
    if status == "present":
        Presrent_student+=1
    elif status == "absent":
        Absent_student+=1
    else:
        print("Invalid input")
        Attendence_count-=1
        #Attendence Counter
    Attendence_count+=1
print("Present Student Count:",Presrent_student)
print("Absent Student Count:",Absent_student)
