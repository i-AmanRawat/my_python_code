##  LIST COMPREHENSION
'''
        SYNTAX:    new_list = [new_item for item in list if test]
'''
# updated_number_list= [n*2 for n in range(1, 5) if n>2]
# print(updated_number_list)

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
# sorted_names= [name.upper() for name in names if len(name)>=5]
# print(sorted_names)

##  DICTIONARY COMPREHENSION
'''
        SYNTAX:    new_dict = { new_key : new_value for item in list if test }
        
        SYNTAX:    new_dict = { new_key : new_value for (key, value) in dict.items() if test }  ##using an exiting dictionary 
        
'''

# dict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(dict.items())

student_score={'aman': 90, "tanvi": 92, "shantnu": 55, "kaira":60, "sage": 20}
passed_student = { student:student_score[student]  for student in student_score if student_score[student]>=60}
print(passed_student)
print()
passed_student= { key:value for (key, value) in student_score.items() if value >=60}
print(passed_student)
