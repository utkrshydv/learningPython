student = {
    'name': 'utkarsh',
    'age': 21,
    'courses': ['Math', 'physics', 'CompSc']
}

print(student.get('name'), student.get('courses'))

student['grade'] = 85
student['age'] = 23

print(student)

age = student.pop('age')

address = student.pop('address', "Not found")
print(address, age)

for keys in student.keys():
    print(keys)

for values in student.values():
    print(values)

for key, value in student.items():
    print(f"{key} : {value}")


classroom = {
    'utkarsh': {'age': 21, 'grade': 90},
    'disha': {'age': 32, 'grade': 100}
}

print(f'utkarsh\'s grade: {classroom['utkarsh']['grade']}')

print(f'disha\'s grade: {classroom['disha']['grade']}')

for key in classroom.keys():
    print(f'{key}\'s grade : {classroom[key]['grade']}')
