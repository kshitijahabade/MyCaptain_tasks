import csv
def write_into_csv(info_list):
    with open('student_info.csv','a',newline='')as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
           writer.writerow(["Name","Age","Contact","Email_ID"])
        writer.writerow(info_list)

if __name__=='__main__':
    condition=True
    student_num=1
    while(condition):
        student_info=input("Enter student information for student #{} in the following format (Name Age Contact Email_ID ):".format(student_num))
        student_info_list=student_info.split(' ')
        print("\nEntererd information is: \nName: {}\nAge: {}\nContact: {}\nEmail: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check=input("Is the entered innformation correct?(y/n)")
        if choice_check=='y':
            write_into_csv(student_info_list)
            condition_check=input("Do you want to enter information for another student?(y/n)")
            if condition_check=='y':
                student_num+=1
                condition=True
            elif condition_check=='n':
                condition=False
        elif choice_check=='n':
            print("Plz re-enter the values!")
