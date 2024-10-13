from ..wrapper.database import DuckWrapper

DB_NAME = "sales.duckdb"
DUCKDB_PATH = "/home/yauheni/main/codeDomain/dbtAstro/db"

create_schema_raw = """
CREATE SCHEMA IF NOT EXISTS raw;
"""

create_table_raw_customers = """
CREATE TABLE IF NOT EXISTS raw.customers (
    customer_id INTEGER PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    signup_date DATE
);
"""

create_table_raw_marketing_campaigns = """
CREATE TABLE IF NOT EXISTS raw.marketing_campaigns (
    campaign_id INTEGER PRIMARY KEY,
    campaign_name VARCHAR,
    channel VARCHAR,
    start_date DATE,
    budget DOUBLE
);
"""

create_table_raw_sales = """
CREATE TABLE IF NOT EXISTS raw.sales (
    sale_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    customer_id INTEGER,
    amount DOUBLE,
    date DATE
);
"""

duckdb_wrapper = DuckWrapper(db_name=DB_NAME, path=DUCKDB_PATH)

duckdb_wrapper.execute_commit(query=create_schema_raw)

duckdb_wrapper.execute_commit(query=create_table_raw_sales)
duckdb_wrapper.execute_commit(query=create_table_raw_customers)
duckdb_wrapper.execute_commit(query=create_table_raw_marketing_campaigns)
