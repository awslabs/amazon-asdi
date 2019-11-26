Section 2: 
2.5:
    CREATE DATABASE ghcn

2.7:
    CREATE EXTERNAL TABLE ghcntable(
    id string, 
    year_date string, 
    element string, 
    data_value string, 
    m_flag string, 
    q_flag string, 
    s_flag string, 
    obs_time string)
    ROW FORMAT DELIMITED 
    FIELDS TERMINATED BY ',' 
    STORED AS INPUTFORMAT 
    'org.apache.hadoop.mapred.TextInputFormat' 
    OUTPUTFORMAT 
    'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
    LOCATION
    's3://noaa-ghcn-pds/csv'
    TBLPROPERTIES (
    'has_encrypted_data'='false',
    'transient_lastDdlTime'='1572285230')

2.18:
    SELECT city, station_id,element, data_value
    FROM stadium
    INNER JOIN ghcntable
    ON stadium.station_id = ghcntable.id
    WHERE ghcntable.year_date >= '20191029'
    AND (
    ghcntable.element = 'TMIN' OR ghcntable.element = 'TMAX')


