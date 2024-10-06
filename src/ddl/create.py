from ..wrapper.database import DuckWrapper

DB_NAME = "university"

create_student_table_query = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    age INTEGER,
    major VARCHAR
)
"""

DuckWrapper(db_name=DB_NAME).execute(query=create_student_table_query)
