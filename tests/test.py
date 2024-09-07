import sqlite3
import pandas as pd
import pytest

# queries to test - chages are
q1 = """
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
q2 = """
        SELECT t1.*, t2.*
        FROM table1 t1
        LEFT JOIN table2 t2 ON t1.id = t2.id
        WHERE (t1.col1 LIKE '%dummy%' OR t1.col1 = '')
        AND EXISTS (
            SELECT 1 FROM table2 t3
            WHERE t3.id = t1.id
            AND t3.col2 IS NOT NULL
        );
        """

# Function to establish a connection to the database
def create_connection(db_name='sqlite_mock.db'):
    return sqlite3.connect(db_name)

# Function to execute the query and return the results as a pandas DataFrame
def execute_query(connection, query):
    return pd.read_sql_query(query, connection)

# Function to compare two query results
def compare_query_results(connection, query1, query2):
    # Execute both queries
    result1 = execute_query(connection, query1)
    result2 = execute_query(connection, query2)
    
    # Compare the results using pandas (ignoring column order)
    pd.testing.assert_frame_equal(result1, result2, check_like=True)

# A pytest test function that compares two SQL queries
@pytest.mark.parametrize("query1, query2", [(q1, q2)])
def test_compare_query_results(query1, query2):
    # Create a database connection
    connection = create_connection()

    # Call the function to compare query results
    compare_query_results(connection, query1, query2)

    # Close the connection after the test
    connection.close()
    
# usage pytest test.py

