from etl.utils.database import get_connection


class DateRepository:
    def get_lookup(self) -> dict:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
                SELECT
                    date_id,
                    full_date
                FROM weather.dim_date
            """)

        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return {row[1]: row[0] for row in rows}
