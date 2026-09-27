print("\n\t"+ "="*21 +"  Collection Manipulator  " + "="*21)

#welcome message for user
print("\nWelcome to the Student Data Organizer!")

students = []


while True:
    print("\n Select Option .......")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display subjects Offered")
    print("6. Exit")

    choice=int(input("Enter Your Choice : "))

    
    #-------------------------  TO ADD STUDENT--------------------------


    if choice == 1:
       print("\n\t=== Enter student details ===")
   
       stud_id =(int(input("\nStudent ID :")),)
       name = input("Name : ")
       age = int(input("Age : "))
       grade = input("Grade : ")
       dob = (input("Date of Birth (YYYY-MM-DD) : "),)
       subjects = set(input("Subjects (comma-separated) : ").split(","))

                   
       student = {
        "id" : stud_id,
        "name" : name,
        "age" : age,
        "grade" : grade,
        "dob" : dob,
        "subjects" :set([i.strip() for i in subjects ])
            }
       students.append(student)
        
       print("\n\t===== Student added successfully. =====")
       


   #----------------------------DISPLAY STUDENT DETAILS-----------------------------     


    elif choice == 2:
        print("\n\t=== Display  All student  ===")
        if not students:
            print("\nNo students found.")
        else:
            for student in students:
                print("\nStudent ID : ", student["id"][0])
                print("Student Name : ", student["name"])
                print("Student Age : ", student["age"])
                print("Student Grade : ", student["grade"])
                print("Student DOB : ", student["dob"][0])
                print("Student Subjects : ", student["subjects"])



#------------------------------UPDATE INFORMATION--------------------------


    elif choice == 3:
        print("\n\t=== Update Student Information ===")

        search_id = int(input("Enter Student ID to update : "))

        found = False

        for student in students:

            if student["id"][0] == search_id:
                found = True

                print("\nEnter New Student Details : ")
                print("(Press Enter to keep old value)")

                # Update name
                new_name = input("New Name : ")
                if new_name == "":
                    new_name = student["name"]

                #Update age
                new_age = input("New Age : ")
                if new_age == "":
                    new_age = student["age"]
                else:
                    new_age = int(new_age)

                # Update grade
                new_grade = input("New Grade : ")
                if new_grade == "":
                    new_grade = student["grade"]

                # Update subjects
                new_subject = input("New Subjects (comma-separated) : ")
                if new_subject == "":
                    new_subject = student["subjects"]
                else:
                    new_subject = set(
                        i.strip() for i in new_subject.split(",")
                    )

                # Update values
                student["name"] = new_name
                student["age"] = new_age
                student["grade"] = new_grade
                student["subjects"] = new_subject

                print("\n===== Student information updated successfully. =====")
                break

        if found == False:
            print("\nStudent ID not found.")
        

            
#--------------------DELETE STUDENT----------------------------------            


    elif choice == 4:
        print("\n\t=== Delete Student ===")

        delete_id = int(input("Enter Student ID to delete : "))

        found = False

        for i in range(len(students)):

            if students[i]["id"][0] == delete_id:
                del students[i]
                found = True

                print("\n===== Student deleted successfully. =====")
                break

        if found == False:
            print("\nStudent ID not found.")


#--------------------------DISPLAY SUBJECTS--------------------


    elif choice == 5:
        print("\n\t=== Display Student Subjects ===")

        search_id = int(input("Enter Student ID : "))

        found = False

        for student in students:

            if student["id"][0] == search_id:
                found = True

                print("\nStudent ID : ", student["id"][0])
                print("Student Name : ", student["name"])
                print("Subjects : ", student["subjects"])

                break

        if found == False:
            print("\nStudent ID not found.")

    elif choice == 6:
        print("Thank you for using the Student Data Organizer.")
        print("Goodbye! See you again.")
        break
            
    else :
        print("Invalid choice... Enter the choice between 1 to 6")
        continue
 
