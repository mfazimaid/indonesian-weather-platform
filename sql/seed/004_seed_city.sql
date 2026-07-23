/* ===========================================================
Seed : 004_seed_city.sql
Generated Automatically
Do not edit manually.
=========================================================== */

BEGIN;

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
    'Jakarta',
    'DKI Jakarta',
    -6.2088,
    106.8456,
    'Asia/Jakarta'
)
ON CONFLICT (city_name)
DO NOTHING;

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
    'Bandung',
    'Jawa Barat',
    -6.9175,
    107.6191,
    'Asia/Jakarta'
)
ON CONFLICT (city_name)
DO NOTHING;

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
    'Bekasi',
    'Jawa Barat',
    -6.2383,
    106.9756,
    'Asia/Jakarta'
)
ON CONFLICT (city_name)
DO NOTHING;

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
    'Bogor',
    'Jawa Barat',
    -6.595,
    106.8166,
    'Asia/Jakarta'
)
ON CONFLICT (city_name)
DO NOTHING;

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
    'Semarang',
    'Jawa Tengah',
    -6.9667,
    110.4167,
    'Asia/Jakarta'
)
ON CONFLICT (city_name)
DO NOTHING;

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
    'Yogyakarta',
    'DI Yogyakarta',
    -7.7956,
    110.3695,
    'Asia/Jakarta'
)
ON CONFLICT (city_name)
DO NOTHING;

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
    'Surabaya',
    'Jawa Timur',
    -7.2575,
    112.7521,
    'Asia/Jakarta'
)
ON CONFLICT (city_name)
DO NOTHING;

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
    'Malang',
    'Jawa Timur',
    -7.9819,
    112.6265,
    'Asia/Jakarta'
)
ON CONFLICT (city_name)
DO NOTHING;

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
    'Denpasar',
    'Bali',
    -8.6705,
    115.2126,
    'Asia/Makassar'
)
ON CONFLICT (city_name)
DO NOTHING;

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
    'Makassar',
    'Sulawesi Selatan',
    -5.1477,
    119.4327,
    'Asia/Makassar'
)
ON CONFLICT (city_name)
DO NOTHING;
COMMIT;
