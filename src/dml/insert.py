from ..wrapper.database import DuckWrapper

DB_NAME = "university"

insert_query = """
INSERT INTO students (id, name, age, major) VALUES
    (1, 'Alice', 20, 'Computer Science'),
    (2, 'Bob', 22, 'Mathematics'),
    (3, 'Charlie', 19, 'Physics'),
    (4, 'Max', 19, 'Physics')
ON CONFLICT (id) DO NOTHING;
"""

insert_template_query = """
INSERT OR IGNORE INTO students (id, name, age, major) VALUES (?,?,?,?);
"""

duck_wrapper = DuckWrapper(db_name=DB_NAME)

duck_wrapper.execute_fetchall(query=insert_query)
duck_wrapper.execute_commit(
    query=insert_template_query,
    args=(5, 'Yauheni', 19, 'Biology')
)
