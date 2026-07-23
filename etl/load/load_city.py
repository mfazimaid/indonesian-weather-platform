import pandas as pd

from etl.utils.database import get_connection

df = pd.read_csv("data/reference/cities.csv")

conn = get_connection()
cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute(
        """
		INSERT INTO dim_city
		(city_name,province,latitude,longitude)
		VALUES(%s,%s,%s,%s)
		ON CONFLICT(city_name)
		DO NOTHING;
	""",
        (row.city_name, row.province, row.latitude, row.longitude),
    )

conn.commit()
cursor.close()
conn.close()

print("city loaded.")
