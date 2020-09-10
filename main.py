# Author: Khalil Stroman kzs5955@psu.edu
def getGradePoint(gp1):
  if gp1 == "A":
    return 4.0
  elif gp1 == "A-":
    return 3.67
  elif gp1 == "B+":
    return 3.33
  elif gp1 == "B":
    return 3.0
  elif gp1 == "B-":
    return 2.67
  elif gp1 == "C+":
    return 2.33
  elif gp1 == "C":
    return 2.0
  elif gp1 == "D":
    return 1.0
  else :
    return 0.0
def run():
  gp1 = input("Enter your course 1 letter grade: ")
  first = getGradePoint(gp1)
  credit1 = input("Enter your course 1 credit: ")
  credit1 = float(credit1)
  print(f"Grade point for course 1 is: {first}")
  gp2 = input("Enter your course 2 letter grade: ")
  second = getGradePoint(gp2)
  credit2 = input("Enter your course 2 credit: ")
  credit2 = float(credit2)
  print(f"Grade point for course 2 is: {second}")
  gp3 = input("Enter your course 3 letter grade: ")
  third = getGradePoint(gp3)
  credit3 = input("Enter your course 3 credit: ")
  credit3 = float(credit3)
  print(f"Grade point for course 3 is: {third}")
  GPA = ((first * credit1)+(second * credit2)+(third * credit3))/(credit1 + credit2 + credit3)
  print(f"Your GPA is: {GPA}")
if __name__ == "__main__":
    run()