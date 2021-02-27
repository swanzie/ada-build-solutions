# your code goes here
import random

names = ['ROSIE MARTINEZ', 'JOE LIU', 'SALLY SUE', 'BOB JOHNSON', 'DELIA AGHO']
id_nums = []
emails = []
last_names = []

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
  id_nums.append(random.randint(111111,999999))

  #list of emails
  str_idnum = str(id_nums[i])
  print(names[i][0])
  print(last_names[i])
  print(str(id_nums[i]))
  email = names[i][0] + last_names[i] + str_idnum[3:] + "@example.org"
  emails.append(email)


print(names)
print(last_names)
print(id_nums)
print(emails)

for i in range(len(names)):
  print(f"name: {names[i]}")
  print(f"id: {id_nums[i]}")
  print(f"email: {emails[i]}\n")




