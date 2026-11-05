
"""
Student Manager — DevOps Lab 5
Module: Main Application
"""

from student import Student


def add_student(students: list, student_id: str, name: str, age: int, grade: str) -> list:
    """Thêm sinh viên mới vào danh sách."""

    # Kiểm tra mã sinh viên đã tồn tại chưa
    for s in students:
        if s.student_id == student_id:
            print(f"Ma sinh vien {student_id} da ton tai!")
            return students

    # Tạo sinh viên mới
    new_student = Student(student_id, name, age, grade)

    # Thêm vào danh sách
    students.append(new_student)

    print(f"Da them sinh vien: {new_student}")

    return students


def main():
    """Hàm chính của ứng dụng."""

    print("=" * 50)
    print("STUDENT MANAGER — DevOps Lab 5")
    print("=" * 50)

    students = [
        Student("SV001", "Nguyen Van A", 20, "K20"),
        Student("SV002", "Tran Thi B", 21, "K20"),
        Student("SV003", "Le Van C", 19, "K21"),
    ]

    # Gọi hàm thêm sinh viên
    students = add_student(students, "SV004", "Pham Thi D", 22, "K19")

    # Hiển thị danh sách sinh viên
    for student in students:
        print(f"  {student}")

    print(f"\nTotal: {len(students)} students")


if __name__ == "__main__":
    main()
