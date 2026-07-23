from etl.utils.database import get_connection
from models.city import City


class CityRepository:
    def get_lookup(self) -> dict:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
                SELECT
                    city_id,
                    city_name
                FROM weather.dim_city
            """)

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return {row[1]: row[0] for row in rows}

    def get_all(self) -> list[City]:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT
                        city_id,
                        city_name,
                        province,
                        latitude,
                        longitude,
                        timezone
                    FROM weather.dim_city
                    ORDER BY city_name;
                """)

                rows = cursor.fetchall()

        return [City(*row) for row in rows]
