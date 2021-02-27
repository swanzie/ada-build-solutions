# your code goes here
import random

names = ['ROSIE MARTINEZ', 'JOE LIU', 'SALLY SUE', 'BOB JOHNSON', 'DELIA AGHO']
id_nums = []
emails = []
last_names = []

#find index for first letter of last name
def get_index_last(name):
  for i in range(len(name)):
    if name[i] == " ":
      # print(i, name)
      return i+1

#get the last name
def get_last_name(fullname):
  for fullname in names:
    index = get_index_last(fullname)
    # print(index, fullname)
    return fullname[index:]

#create list of last names
for i in range(len(names)):
  last_names.append(get_last_name(names[i]))

#create list of id numbers
for i in range(len(names)):
  id_nums.append(random.randint(111111,999999))
print(id_nums)

#create list of emails
for i in range(len(names)):
  str_idnum = str(id_nums[i])
  print(names[i][0])
  print(last_names[i])
  print(str(id_nums[i]))
  email = names[i][0] + last_names[i] + str_idnum[-3] + str_idnum[-2] + str_idnum[-1] + "@example.org"
  emails.append(email)

print(names)
print(last_names)
print(id_nums)
print(emails)

for i in range(len(names)):
  print(f"name: {names[i]}")
  print(f"id: {id_nums[i]}")
  print(f"email: {emails[i]}\n")




