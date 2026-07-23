from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

csv_file = BASE_DIR / "data/reference/cities.csv"
output_file = BASE_DIR / "sql/seed/004_seed_city.sql"

df = pd.read_csv(csv_file)

with open(output_file, "w", encoding="utf-8") as f:
    f.write("""/* ===========================================================
Seed : 004_seed_city.sql
Generated Automatically
Do not edit manually.
=========================================================== */

BEGIN;
""")

    for _, row in df.iterrows():
        city = str(row["city_name"]).replace("'", "''")
        province = row["province"].replace("'", "''")

        f.write(f"""
INSERT INTO weather.dim_city
(
    city_name,
    province,
    latitude,
    longitude,
    timezone
)
VALUES
(
    '{city}',
    '{province}',
    {row.latitude},
    {row.longitude},
    '{row.timezone}'
)
ON CONFLICT (city_name)
DO NOTHING;
""")

    f.write("COMMIT;\n")

# print("Seed SQL generated successfully.")
print("=" * 60)
print("Generate Seed City")
print("=" * 60)

print(f"CSV File : {csv_file}")
print(f"Output File : {output_file}")

print()
print("Reading CSV...")

# df = pd.read_csv(csv_file)

print(f"{len(df)} rows loaded")
