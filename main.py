# main.py

import logging
from extract import extract_from_table1, extract_from_table2, extract_from_table3

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting data extraction process...")
    
    # Extract data from table1
    try:
        logging.info("Extracting data from table1...")
        df1 = extract_from_table1()
        logging.info(f"Data from table1 extracted successfully. Rows: {len(df1)}")
    except Exception as e:
        logging.error(f"Error extracting data from table1: {str(e)}")

    # Extract data from table2
    try:
        logging.info("Extracting data from table2...")
        df2 = extract_from_table2()
        logging.info(f"Data from table2 extracted successfully. Rows: {len(df2)}")
    except Exception as e:
        logging.error(f"Error extracting data from table2: {str(e)}")

    # Extract data from table3
    try:
        logging.info("Extracting data from table3...")
        df3 = extract_from_table3()
        logging.info(f"Data from table3 extracted successfully. Rows: {len(df3)}")
    except Exception as e:
        logging.error(f"Error extracting data from table3: {str(e)}")

    logging.info("Data extraction process completed.")

if __name__ == "__main__":
    main()
