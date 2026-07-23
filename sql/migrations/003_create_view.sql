/* =============================================================================
Migration: 003_create_view.sql
Project: Indonesian Weather Platform

Description: 
Create reporting views for Business Intelligence dashboard.

Author: Muhammad Fauzan Azima
Version: 2.0
============================================================================= */

BEGIN
-- =============================================================================
-- View: Daily Weather
--
-- Purpose
-- One row represents one city on one day.
-- 
-- Consumer
-- - Power BI
-- - Dashboard
-- - Analyst
-- =============================================================================

CREATE OR REPLACE VIEW weather.vw_daily_weather AS

SELECT
    -- Date
    d.full_date,
    d.day,
    d.month,
    d.year,
    d.week,
    d.weekday,
    d.quarter,

    -- City
    c.city_id,
    c.city_name,
    c.province,
    c.latitude,
    c.longitude,
    c.timezone,

    -- Weather
    f.temperature,
    f.humidity,
    f.wind_speed,
    f.wind_direction,
    f.pressure,
    f.precipitation,
    f.cloud_cover,
    f.weather_code,
    f.created_at

FROM weather.fact_weather f
INNER JOIN weather.dim_city c
    ON f.city_id = c.city_id

INNER JOIN weather.dim_date d
    ON f.date_id = d.date_id;

COMMENT ON VIEW weather.vw_daily_weather
IS 'Daily weather reporting view for dashboard';

COMMIT;
