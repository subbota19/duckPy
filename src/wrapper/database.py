from duckdb import connect
from os.path import relpath, dirname, join as path_join
from typing import List, Any

PACKAGE_DIR = relpath(dirname(__file__))
PARENT_DIR = relpath(path_join(PACKAGE_DIR, '..', '..'))
DATA_DIR = path_join(PARENT_DIR, 'db_storage')


class DuckWrapper:
    def __init__(self, db_name: str):
        self.con = connect(database=f"{DATA_DIR}/{db_name}", read_only=False)

    def execute_fetchall(self, query: str) -> List[Any]:
        try:
            return self.con.execute(query).fetchall()
        except Exception as e:
            print(f"Failed to execute DuckDB query: {e}")

    def execute_commit(self, query: str, args: tuple = ()) -> None:
        try:
            self.con.execute(query, args).commit()
        except Exception as e:
            print(f"Failed to execute DuckDB query: {e}")

    def close(self):
        self.con.close()
