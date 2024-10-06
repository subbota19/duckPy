from ..wrapper.database import DuckWrapper

DB_NAME = "university"

insert_query = """
INSERT INTO students (id, name, age, major) VALUES
    (1, 'Alice', 20, 'Computer Science'),
    (2, 'Bob', 22, 'Mathematics'),
    (3, 'Charlie', 19, 'Physics')
ON CONFLICT (id) DO NOTHING
"""

DuckWrapper(db_name=DB_NAME).execute(query=insert_query)
