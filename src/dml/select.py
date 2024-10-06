from ..wrapper.database import DuckWrapper

DB_NAME = "university"

select_all_students = """
SELECT * FROM students
"""
try:
    duck_wrapper = DuckWrapper(db_name=DB_NAME)
    students = duck_wrapper.execute(query=select_all_students)
    for student in students:
        print(student)
except Exception as e:
    print(f"Error querying all students: {e}")
