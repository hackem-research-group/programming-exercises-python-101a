# Create a program to convert numeric grades according to the following table:
#  GRADE | Numbers
#    A   |   19,20
#    B   |   16,17,18
#    C   |   13,14,15
#    D   |   10,11,12
#    E   |   1 to 9

def getGrade(noteInNumber):
    grade = int(noteInNumber)
    if (grade <= 20 and grade >= 19):
        return "A"
    elif (grade < 19 and grade >= 16):
        return "B"
    elif (grade < 16 and grade >= 13):
        return "C"
    elif (grade < 13 and grade >= 10):
        return "D"
    elif (grade < 10 and grade >= 1):
        return "E"
    else:
        return "-"

gradeInNumber = raw_input("Ingrese la nota:")
print getGrade(gradeInNumber)
