/* ==========================================
 Migration: 002_create_index.sql
 Description: Create Indexes
 ========================================== */

 -- ============================================================================
-- Dimension Index
-- ============================================================================

CREATE INDEX idx_dim_city_city_name
ON weather.dim_city(city_name);

CREATE INDEX idx_dim_date_full_date
ON weather.dim_city(full_date);

-- ============================================================================
-- Fact Index
-- ============================================================================

CREATE INDEX idx_fact_weather_city
ON weather.fact_weather(city_id);

CREATE INDEX idx_fact_weather_date
ON weather.fact_weather(date_id);

CREATE INDEX idx_fact_weather_weather_code
ON weather.fact_weather(weather_code);
