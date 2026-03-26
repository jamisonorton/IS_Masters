# week 7 code along 2


class SimpleClass:
    pass


class YesNoBooleanValueConverter:

    def convert(self, val):
        if val:
            return "Yes"
        return "No"

    def convert_back(self, val):

        val = str(val).upper()
        if val == "Y" or val == "YES":
            return True
        return False


class Student:

    first_name = ""
    last_name = ""
    is_graduated = False


student_a = Student()
student_a.first_name = "Jamison"
student_a.last_name = "Orton"
student_a.is_graduated = True

vc = YesNoBooleanValueConverter()
grad_status = vc.convert(student_a.is_graduated)
print(grad_status)

grad_status1 = vc.convert_back("N")
print(
    student_a.first_name,
    student_a.last_name,
    "Is graduated:",
    vc.convert(grad_status1),
)
