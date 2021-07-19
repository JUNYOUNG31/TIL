class Student :
    def __init__(self, name, gender, height) :
        self.__name = name
        self.__gender = gender
        self.__height = height

    @property
    def name(self) :
        return self.__name

    @property
    def gender(self) :
        return self.__gender
    
    @property
    def height(self) :
        return self.__height

    @height.setter
    def height(self, height) :
        self.__height = height

    def __repr__(self) :
        return "{0}(name: {1}, gender : {2}, height : {3})"\
            .format(self.__class__.__name__, self.name, self.gender, self.height)

Students = [
    Student("홍길동", "남",170.3),
    Student("박남길", "남",180.6),
    Student("나우주", "남",167.3),
    Student("조광문", "남",190.4)
]

for student in Students :
    print(student)


print("name 으로 오름차순 정렬 후 ===>")    
for student in sorted(Students, key=lambda x :x.name, reverse= False) :
    print(student)

print("name 으로 내림차순 정렬 후 ===>")    
for student in sorted(Students, key=lambda x :x.name, reverse= True) :
    print(student)

print("height 으로 오름차순 정렬 후 ===>")    
for student in sorted(Students, key=lambda x :x.height) :
    print(student)

print("height 으로 내림차순 정렬 후 ===>")    
for student in sorted(Students, key=lambda x :x.height, reverse= True) :
    print(student)