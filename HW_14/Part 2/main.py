from university_pacage import Student, Group, FullGroup

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 28, 'John', 'Doe', 'AN146')
st4 = Student('Female', 22, 'Anna', 'Smith', 'AN147')
st5 = Student('Male', 35, 'Mark', 'Twain', 'AN148')
st6 = Student('Female', 27, 'Sophia', 'Brown', 'AN149')
st7 = Student('Male', 32, 'David', 'Johnson', 'AN150')
st8 = Student('Female', 24, 'Emma', 'Davis', 'AN151')
st9 = Student('Male', 29, 'James', 'Wilson', 'AN152')
st10 = Student('Female', 26, 'Olivia', 'Taylor', 'AN153')
st11 = Student('Male', 31, 'Michael', 'Scott', 'AN154')

gr = Group('PD1')

try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)  # [Error] Група PD1 переповнена. Неможливо додати студента.
except FullGroup as error:
    print(f"[Error] {error}")

print(f"\n{gr}\n")

assert gr.find_student('Jobs') == st1, 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

gr.delete_student('Taylor')
gr.delete_student('Doe')
gr.delete_student('Johnson')
print(gr)  # 7 students

gr.delete_student('Taylor')  # No error!
