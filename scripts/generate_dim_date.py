from datetime import datetime, timedelta

from etl.utils.database import get_connection


def generate_date(start_date, end_date):
    conn = get_connection()
    cursor = conn.cursor()

    current = start_date

    while current <= end_date:
        date_id = int(current.strftime("%Y%m%d"))
        full_date = current.strftime("%Y-%m-%d")
        day = current.day
        month = current.month
        year = current.year
        week = current.isocalendar().week
        weekday = current.strftime("%A")
        quarter = (month - 1) // 3 + 1

        cursor.execute(
            """
			INSERT INTO weather.dim_date
			(
				date_id,
				full_date,
				day,
				month,
				year,
				week,
				weekday,
				quarter
			)
			VALUES
			(%s,%s,%s,%s,%s,%s,%s,%s)
			oN CONFLICT (date_id)
			DO NOTHING;
			""",
            (date_id, full_date, day, month, year, week, weekday, quarter),
        )

        current += timedelta(days=1)

    conn.commit()
    cursor.close()
    conn.close()
    print("dim_date berhasil dibuat.")


if __name__ == "__main__":
    start = datetime(2026, 1, 1)
    end = datetime(2030, 12, 31)
    generate_date(start, end)
