#account generator using a list of dictionaries (student accounts that have keys: name, ID, email)

import random

#step 2 - list of student names
student_names = ["ROSIE MARTINEZ", "JOE LIU", "SALLY SUE", "BOB JOHNSON", "DELIA AGHO"]

#step 3 - loop generator to randomly assign student ID numbers from 111111 - 999999 and store in student ID
ids = []
for i in range(len(student_names)):
  ids.append(random.randint(111111, 999999))

#step 4 - generate student e-mail addresses in format: first initial + last name + last 3 digits of ID @ example.org
emails = []
i = 0
for name in student_names:
  [first,last] = name.split(" ")
  emails.append(first[0]+last+str(ids[i])[3:]+"@example.org")
  i += 1

#step 5 - create list of dictionaries
student_accounts = []
for i in range(len(student_names)):
  student_accounts.append(
      {"name": student_names[i],
       "ID": ids[i],
       "emails": emails[i]}
    )

# print student name, ID, and email
for account in student_accounts:
  print(f'name: {account["name"]}')
  print(f"ID: {account['ID']}")
  print(f"email: {account['emails']}\n")
