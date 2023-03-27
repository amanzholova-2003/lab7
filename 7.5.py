students = {}
students.setdefault('Anna', {'age': 20, 'major': 'Biologist'})
students.setdefault('Tom', {'age': 18, 'major': 'Math'})
students.update({'Anna': {'age': 21, 'major': 'Math'}})
anna_major = students.get('Anna', {}).get('major')
print(f'Anna: спец - {anna_major}')

removed_student = students.pop('Tom')
print(f'pop: {removed_student}')

clear_student_dict = students.clear()
print(clear_student_dict)