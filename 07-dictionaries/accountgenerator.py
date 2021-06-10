#account generator using a list of dictionaries (student accounts that have keys: name, ID, email)

import random

#ask user for name
def get_full_name():
  student_name = input("full name: ")
  return student_name

#create list with user inputted names
names = []
def get_list_names():
  more_names = True
  choice = ""

  #ask user for unlimited number of names
  while more_names:
    names.append(get_full_name())
    choice = input("more names? y/n: ")
    if choice == "y":
      more_names = True
    else: 
      more_names = False
  print("\n")

#invoke user to input list of names
get_list_names()

#step 5 - populate list with dictionaries of student account that each as a name, ID, and email with a single loop
student_accounts = []
for i in range(len(names)):

  emails = []
  j = 0
  id = random.randint(111111, 999999)
  for name in names:
    [first,last] = name.split(" ")
    emails.append(first[0]+last+str(id)[3:]+"@example.org")
    j += 1  
  student_accounts.append(
      {"name": names[i],
       "id": id,
       "email": emails[i]}
    )

# print student name, ID, and email
for account in student_accounts:
  print(f'name: {account["name"]}')
  print(f"id: {account['id']}")
  print(f"email: {account['email']}\n")
