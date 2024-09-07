# extract.py

from sqlalchemy import create_engine, text
import psycopg2
import pandas as pd

# PostgreSQL connection details
DB_URI = "postgresql+psycopg2://username:password@localhost/dummy_postgres"

def inefficient_query_1():
    """Inefficient query for table1."""
    query = """
        SELECT t1.*, t2.*
        FROM table1 t1
        LEFT JOIN table2 t2 ON t1.id = t2.id
        WHERE t1.col1 IN (
            SELECT col1 FROM table1 WHERE col1 LIKE '%dummy%' OR col1 = ''
        )
        AND t1.id IN (
            SELECT DISTINCT id FROM table2 WHERE col2 IS NOT NULL
        );
    """
    return query

def inefficient_query_2():
    """Inefficient query for table2."""
    query = """
        SELECT t2.*, t3.*
        FROM table2 t2
        LEFT JOIN table3 t3 ON t2.id = t3.id
        WHERE t2.id IN (
            SELECT id FROM table1 WHERE col3 LIKE '%%%temp%%'
        )
        AND EXISTS (
            SELECT 1 FROM table3 WHERE col4 = t3.col4 AND t3.col4 = t2.col5
        );
    """
    return query

def inefficient_query_3():
    """Inefficient query for table3."""
    query = """
        SELECT *
        FROM table3
        WHERE id IN (
            SELECT id FROM table2 WHERE col6 IN (SELECT col7 FROM table1)
        )
        AND col6 NOT IN (
            SELECT col6 FROM table2 WHERE col6 IS NULL
        )
        AND col8 = (
            SELECT MAX(col8) FROM table3
        );
    """
    return query

def extract_data(query):
    """Executes a query using SQLAlchemy and returns data as pandas DataFrame."""
    engine = create_engine(DB_URI)
    
    with engine.connect() as connection:
        result = connection.execute(text(query))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
    return df

# Helper functions to extract data with inefficient queries
def extract_from_table1():
    query = inefficient_query_1()
    return extract_data(query)

def extract_from_table2():
    query = inefficient_query_2()
    return extract_data(query)

def extract_from_table3():
    query = inefficient_query_3()
    return extract_data(query)
