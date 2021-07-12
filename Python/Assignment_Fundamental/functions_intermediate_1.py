# x = [ [5,2,3], [15,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Bryant'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Andres', 'Ronaldo', 'Rooney']
# }

# z = [ {'x': 10, 'y': 30} ]

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# def iterateDictionary(students):
#     for student in students:
#         print(f'first_name - {student["first_name"]}, last_name - {student["last_name"]}')
# iterateDictionary(students) 

# def iterateDictionary2(key_name, some_list):
#     for student_dictionary in some_list:
#         print(student_dictionary[key_name])
# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def dojoInfo(some_dict):
    for info in some_dict:
        print(info)
        list_of_info = some_dict[info]
        for item in list_of_info:
            print(item)
dojoInfo(dojo)