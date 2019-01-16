subjects = ["Computer Science", "Business Management", "Film", "English Language & Literature", "Math Standard Level", "Spanish Ab Initio"]
grades = ["D", "B", "A", "B", "C", "C"]

for subject, grade in zip(subjects, grades):
  print(grade + " - " + subject)
  if grade == "A":
    print("Well done!")
  elif grade == "B":
    print("Not bad!")
  else:
    print("Try harder next time.")
