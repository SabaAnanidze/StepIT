import json

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    @classmethod #viyenebt classmethod dekorators imitom rom dicts jsoni ighebs rogorc obiekts
    def read_json(cls, filep):
        with open(filep, "r") as file:
            data = json.load(file)

        students = []
        for i in data["students"]:
            student = Student(i["name"], i["age"], i["grades"])
            students.append(student)
        return students

    def calculate_average(self): #es unda iyos instance method imitom rom initidan unda amoighos
        # instance variablebi romlebzec unda moaxdinos zemokmedeba
        return round(sum(self.grades) / len(self.grades), 2)

    @classmethod
    def write_json(cls, students, output_file):
        result = {}
        for student in students:
            result[student.name] = student.calculate_average()

        with open(output_file, "w") as file:
            json.dump(result, file, indent=4)
        return result

