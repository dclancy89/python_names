students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }



def printNames(arr):
	for x in arr:
		print x["first_name"] + " " + x["last_name"]

def printUsers(users):
	for key, data in users.items():
		print key
		count = 1
		for value in data:
			print str(count) + " - " + value["first_name"].upper() + " " + value["last_name"].upper() + " - " + str(len(value["first_name"]) + len(value["last_name"]))

printNames(students)
print ""
print ""
print ""
printUsers(users)