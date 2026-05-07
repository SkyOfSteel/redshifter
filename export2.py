# redshift-env\Scripts\activate

import redshift_connector
import pandas as pd

# Connection detailsHOST = 'your_host'DATABASE = 'your_db'PORT = 5439USER = 'your_user'PASSWORD = 'your_password'TABLE_NAME = 'your_table'COLUMN_NAME = 'your_column'try:

    # Establish connectionconn = redshift_connector.connect(

        host=HOST,

        database=DATABASE,

        port=PORT,

        user=USER,

        password=PASSWORD

    )

    print("Connection successful")


    # Create a cursor objectcursor = conn.cursor()

column_list = result_df['column_name'].tolist()

print(column_list)

    # Execute the SQL query to select the columnsql_query = f"SELECT {COLUMN_NAME} FROM {TABLE_NAME}"    cursor.execute(sql_query)


    # Fetch all results# fetchall() retrieves all rows of a query result setresult_rows = cursor.fetchall()


    # Process the results into a Python listcolumn_data = [row[0] for row in result_rows]


    print(f"Captured {len(column_data)} rows of data.")

    print("Sample data:", column_data[:10]) # Print first 10 items# Optional: Load directly into a pandas DataFrame# data_frame = pd.read_sql(sql_query, conn)# print("DataFrame shape:", data_frame.shape)except Exception as e:

    print(f"An error occurred: {e}")

finally:

    # Close the cursor and connectionif cursor:

        cursor.close()

    if conn:

        conn.close()