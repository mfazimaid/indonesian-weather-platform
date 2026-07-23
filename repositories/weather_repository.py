from etl.utils.database import get_connection


class WeatherService:
    def get_all_cities(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
			SELECT
				city_name,
				province,
				latitude,
				longitude
			FROM dim_city
			ORDER BY city_name;
		""")

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows
