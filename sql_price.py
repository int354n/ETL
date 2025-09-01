import pandas as pd

df = pd.read_csv("C:/Users/user/Downloads/laptops.csv")
print(df.head())

import sqlite3

conn = sqlite3.connect("C:/Users/user/Downloads/laptops.db")  
df.to_sql("laptops", conn, if_exists="replace", index=False)


query = """		
SELECT		
 Screen_Size,		
 AVG(CAST(REPLACE(Price, ',', '.') AS REAL)) AS Avg_Price		
FROM		
 laptops		
WHERE		
 Price != '' AND Screen_Size != ''		
GROUP BY		
 Screen_Size		
ORDER BY		
 CAST(REPLACE(Screen_Size, ',', '.') AS REAL);		
"""		


result_df = pd.read_sql_query(query, conn)

print(result_df)


result_df.to_csv("C:/Users/user/Downloads/avg_price_result.csv", index=False, encoding='utf-8')


conn.close()