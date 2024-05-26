import pandas as pd
import mysql.connector

# Establish a connection to the database
conn = mysql.connector.connect(
    host="your_host",
    user="your_user",
    password="your_password",
    database="sakila"
)

# Retrieve the data for May
may_query = "SELECT customer_id, COUNT(*) AS may_rentals FROM rentals_may GROUP BY customer_id;"
df_may = pd.read_sql(may_query, conn)

# Retrieve the data for June
june_query = "SELECT customer_id, COUNT(*) AS june_rentals FROM rentals_june GROUP BY customer_id;"
df_june = pd.read_sql(june_query, conn)

# Merge the two dataframes on customer_id
merged_df = pd.merge(df_may, df_june, on='customer_id', how='inner')

# Define a function to compare rentals
def compare_rentals(row):
    if row['may_rentals'] < row['june_rentals']:
        return 'More in June'
    elif row['may_rentals'] > row['june_rentals']:
        return 'More in May'
    else:
        return 'Equal'

# Apply the function to the dataframe
merged_df['comparison'] = merged_df.apply(compare_rentals, axis=1)

# Display the results
print(merged_df)