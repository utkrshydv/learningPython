student = {
    'name': 'utkarsh',
    'age': 21,
    'courses': ['Maths', 'Science'],
    'grade': 100
}


print(student['name'])
# get is better -> returns none instead of throwing an error
print(student.get('age'))

student['email'] = 'abc@example.com'
print(student)

del student['age']
grade = student.pop('grade')
print(grade)
print(student)

for key in student:
    print(key, ' : ', student[key])

for key, value in student.items():
    print(key, ' : ', value)
