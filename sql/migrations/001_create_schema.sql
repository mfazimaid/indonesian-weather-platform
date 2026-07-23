/* ======================================= 
Migration: 001_create_schema.sql
Porject: Indonesian Weather Platform

Description:
Initial Database Schema

This migration creates:
 - Weather Schema
 - Dimension Tables
 - Fact Table
 - Constraints
 - Comments

Author: Muhammad Fauzan Azima
Version: 1.0
=======================================*/

BEGIN;

-- =======================================
-- Create Schema
-- =======================================

CREATE SCHEMA IF NOT EXISTS weather;

-- =======================================
-- Dimension: City
-- 
-- Bussiness Rules
-- 1. 1 baris merepresentasikan 1 kota.
-- 2. kota harus unik.
-- 3. Lintang (Latitude) mengikuti standar WGS84 (rentang antara -90 sampai 90 derajat).
-- 4. Bujur (Longitude) mengikuti standar WGS84 (rentang antara -180 sampai 180 derajat).
-- 5. Zona waktu mengikuti Database Zona Waktu IANA (contoh formatnya seperti Asia/Jakarta, Asia/Makassar, atau Asia/Jayapura).
-- =======================================

CREATE TABLE IF NOT EXISTS weather.dim_city(

    city_id BIGINT
        GENERATED ALWAYS AS IDENTITY,

    city_name VARCHAR(100)
        NOT NULL,

    province VARCHAR(100)
        NOT NULL,

    latitude NUMERIC(9,6)
        NOT NULL,

    longitude NUMERIC(9,6)
        NOT NULL,

    timezone VARCHAR(50)
        NOT NULL,
    
    created_at TIMESTAMP
        NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP
        NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_dim_city
        PRIMARY KEY (city_id),

    CONSTRAINT uq_dim_city_name
        UNIQUE (city_name),

    CONSTRAINT chk_latitude
        CHECK (latitude BETWEEN -90 AND 90),

    CONSTRAINT chk_longitude
        CHECK (longitude BETWEEN -180 AND 180)
);

COMMENT ON TABLE weather.dim_city
IS 'Master table containing Indonesian cities';

COMMENT ON COLUMN weather.dim_city.city_name
IS 'Official city name';

COMMENT ON COLUMN weather.dim_city.latitude
IS 'latitude using WGS84';

COMMENT ON COLUMN weather.diim_city.longitude
IS 'longitude using WGS84';

COMMENT ON COLUMN weather.dim_city.timezone
IS 'Timezone based on IANA database';

-- =======================================
-- Dimension: Date
-- =======================================

CREATE TABLE IF NOT EXISTS weather.dim_date(
    
    date_id INTEGER,

    full_date DATE
        NOT NULL,

    day INTEGER
        NOT NULL,

    month INTEGER
        NOT NULL,

    year INTEGER
        NOT NULL,

    week INTEGER
        NOT NULL,

    weekday VARCHAR(20)
        NOT NULL,

    quarter INTEGER
        NOT NULL,

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_dim_date
        PRIMARY KEY (date_id),

    CONSTRAINT uq_dim_date
        UNIQUE (full_date)
);

COMMENT ON TABLE weather.dim_date
IS 'Calendar dimension';

-- =======================================
-- Fact: Weather
--
-- Grain:
-- 1 Row = 1 Kota + 1 Tanggal
-- =======================================

CREATE TABLE IF NOT EXISTS weather.fact_weather (
    
    weather_id BIGINT
        GENERATED ALWAYS AS IDENTITY,

    city_id BIGINT
        NOT NULL,

    date_id INTEGER
        NOT NULL,

    temperature NUMERIC(5,2),

    humidity NUMERIC(5,2),

    wind_speed NUMERIC(6,2),

    wind_direction NUMERIC(6,2),

    pressure NUMERIC(7,2),

    precipitation NUMERIC(6,2),

    cloud_cover NUMERIC(5,2),

    weather_code INTEGER,

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_fact_weather
        PRIMARY KEY (weather_id),

    CONSTRAINT fk_fact_weather_city
        FOREIGN KEY (city_id)
        REFERENCES weather.dim_city(city_id),

    CONSTRAINT fk_fact_weather_date 
        FOREIGN KEY (date_id)
        REFERENCES weather.dim_date(date_id),

    CONSTRAINT chk_temperature
        CHECK (temperature BETWEEN -50 AND 60),

    CONSTRAINT chk_humidity
        CHECK (humidiity BETWEEN 0 AND 100),

    CONSTRAINT chk_wind_direction
        CHECK (wind_direction BETWEEN 0 AND 100),
);

COMMENT ON TABLE weather.fact_weather
IS 'Daily weather observation fact table';

COMMENT ON COLUMN weather.fact_weather.temperature
IS 'Average temperature in Celcius';

COMMENT ON COLUMN weather.fact_weather.humidity
IS 'Relative humidity percentage';

COMMENT ON COLUMN weather.fact_weather.wind_speed
IS 'wind speed in km/h';

COMMENT ON COLUMN weather.fact_weather.wind_direction
IS ON 'Open meteo weather code';

COMMIT;

