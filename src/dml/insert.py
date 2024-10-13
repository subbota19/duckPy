from ..wrapper.database import DuckWrapper

DB_NAME = "sales.duckdb"
DUCKDB_PATH = "/home/yauheni/main/codeDomain/dbtAstro/db"

insert_query_raw_customers = """
INSERT OR IGNORE INTO raw.customers (customer_id, first_name, last_name, signup_date) VALUES
    (1001, 'John', 'Doe', '2023-01-15'),
    (1002, 'Jane', 'Smith', '2023-02-20'),
    (1003, 'Alice', 'Johnson', '2023-03-05'),
    (1004, 'Bob', 'Brown', '2023-04-10'),
    (1005, 'Carol', 'Davis', '2023-05-25');
"""
insert_query_raw_marketing_campaigns = """
INSERT OR IGNORE INTO raw.marketing_campaigns (campaign_id, campaign_name, channel, start_date, budget) VALUES
    (2001, 'Spring Sale', 'Email', '2023-03-01', 5000.00),
    (2002, 'Summer Launch', 'Social Media', '2023-06-15', 8000.00),
    (2003, 'Holiday Deals', 'PPC', '2023-11-20', 10000.00),
    (2004, 'Winter Clearance', 'Email', '2023-12-01', 7000.00),
    (2005, 'New Year Promo', 'Social Media', '2024-01-05', 6000.00);
"""
insert_query_raw_sales = """
INSERT OR IGNORE INTO raw.sales (sale_id, product_id, customer_id, amount, date) VALUES
    (3001, 101, 1001, 250.00, '2023-01-15'),
    (3002, 102, 1002, 150.00, '2023-02-20'),
    (3003, 103, 1003, 300.00, '2023-03-05'),
    (3004, 104, 1004, 450.00, '2023-04-10'),
    (3005, 105, 1005, 500.00, '2023-05-25'),
    (3006, 106, 1001, 200.00, '2023-06-15'),
    (3007, 107, 1002, 350.00, '2023-07-20'),
    (3008, 108, 1003, 400.00, '2023-08-05'),
    (3009, 109, 1004, 550.00, '2023-09-10'),
    (3010, 110, 1005, 600.00, '2023-10-25');
"""
insert_template_query = """
INSERT OR IGNORE INTO raw.marketing_campaigns (campaign_id, campaign_name, channel, start_date, budget) VALUES
 (?,?,?,?,?);
"""

duck_wrapper = DuckWrapper(db_name=DB_NAME, path=DUCKDB_PATH)

duck_wrapper.execute_fetchall(query=insert_query_raw_sales)
duck_wrapper.execute_fetchall(query=insert_query_raw_customers)
duck_wrapper.execute_fetchall(query=insert_query_raw_marketing_campaigns)
