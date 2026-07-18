name = input("Enter Student Name")
sub1 = int(input("Enter Marks of Subject 1"))
sub2 = int(input("Enter Marks of Subject 2"))
sub3 = int(input("Enter Marks of Subject 3"))
sub4 = int(input("Enter Marks of Subject 4"))
sub5 = int(input("Enter Marks of Subject 5"))
#calculations
total_possiblemarks = 500
total_marks = sub1+sub2+sub3+sub4+sub5
average = (total_marks) / 5
percentage = (total_marks) / (total_possiblemarks) * 100
print("hi",name)
print("total marks",total_marks)
print("percentage:",percentage)