Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = input("Name of the student: ")
Name of the student: DIVYA
>>> subject1 = float(input("Enter the subject1 score: "))
Enter the subject1 score: 67.9
>>> if subject1 < 40:
...     print("Fail")
... else:
...     print("Pass")
... 
...     
Pass
>>> subject2 = float(input("Enter the subject2 score: "))
Enter the subject2 score: 49.5
>>> if subject2 < 40:
...     print("Fail")
... else:
...     print("Pass")
... 
Pass
>>> subject3 = float(input("Enter the subject3 score: "))
Enter the subject3 score: 45.9
>>> if subject3 < 40:
...     print("Fail")
... else:
...     print("Pass")
... 
Pass
>>> subject4 = float(input("Enter the subject4 score: "))
... 
Enter the subject4 score: 89.9
>>> if subject4 < 40:
...     print("Fail")
... else:
...     print("Pass")
... 
Pass
>>> subject5 = float(input("Enter the subject5 score: "))
... 
Enter the subject5 score: 78.9
>>> if subject5 < 40:
    print("Fail")
else:
    print("Pass")

Pass
subject6 = float(input("Enter the subject6 score: "))
Enter the subject6 score: 89.7
if subject6 < 40:
    print("Fail")
else:
    print("Pass")

Pass
result = subject1 + subject2 + subject3 + subject4 + subject5 + subject6
print("Sum of the subjects:", result)
Sum of the subjects: 421.8
if result > 240 and result <= 600:
    if result > 600:
        print("Congrats for O+ grade")
    elif result > 580:
        print("Congrats for O grade")
    elif result > 570:
        print("Congrats for D++ grade")
    elif result > 560:
        print("Congrats for D+ grade")
    elif result > 550:
        print("Congrats for D grade")
    elif result > 530:
        print("Congrats for A+ grade")
    elif result > 500:
        print("Congrats for A grade")
    elif result > 400:
        print("Congrats for B grade")
else:
    if result > 200:
        print("Keep studying")
    else:
        print("Work hard - Overall Fail")


Congrats for B grade
