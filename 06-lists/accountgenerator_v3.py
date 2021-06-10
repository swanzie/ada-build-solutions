# optional enhancements to account generator prompting user for names and ensuring no id duplicates
import random

names = []
id_nums = []
emails = []
last_names = []

def get_full_name():
  student_name = input("full name: ")
  return student_name

#create list with user inputted names
def get_list_names():
  more_names = True
  choice = ""

  while more_names:
    names.append(get_full_name())
    choice = input("more names? y/n: ")
    if choice == "y":
      more_names = True
    else: 
      more_names = False
# 
# get_list_names()

names = ["bob loblaw"] * 100

#return the last name
def get_last_name(name):
  for i in range(len(name)):
    if name[i] == " ":
      # print(i, name)
      return name[i+1:]

#create list of last names, list of id numbers, list of emails
for i in range(len(names)):
  #last names
  last_names.append(get_last_name(names[i]))

  #id numbers
  new_id = random.randint(111111, 999999)
  #checking for duplicates
  while new_id in id_nums:
    print("created a duplicate~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    new_id = random.randint(111111, 999999)
  id_nums.append(new_id)
   

  #list of emails
  str_idnum = str(id_nums[i])
  # print(names[i][0])
  # print(last_names[i])
  # print(str(id_nums[i]))
  email = names[i][0] + last_names[i] + str_idnum[3:] + "@example.org"
  emails.append(email)


# print(names)
# print(last_names)
# print(id_nums)
# print(emails)

for i in range(len(names)):
  print(f"name: {names[i]}")
  print(f"id: {id_nums[i]}")
  print(f"email: {emails[i]}\n")

def has_dupes(arr):
  for elem in arr:
    if arr.count(elem) > 1:
      return True
  # else    
  return False    

assert has_dupes(id_nums) == False, "Found a duplicate"
