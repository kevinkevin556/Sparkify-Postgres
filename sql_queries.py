# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users "
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id     SERIAL     PRIMARY KEY,
        timestamp       varchar,
        user_id         int        REFERENCES users (user_id),
        level           varchar,
        song_id         varchar    REFERENCES songs (song_id),
        artist_id       varchar    REFERENCES artists (artist_id),
        session_id      int        NOT NULL,
        user_location   varchar,
        user_agent      varchar
    )
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id       int       PRIMARY KEY,
        first_name    varchar   NOT NULL,
        last_name     varchar   NOT NULL,
        gender        varchar, 
        level         varchar
    )
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id     varchar    PRIMARY KEY, 
        title       varchar    NOT NULL, 
        artist_id   varchar    NOT NULL,
        year        int, 
        duration    numeric
    )
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id           varchar    PRIMARY KEY,
        artist_name         varchar    NOT NULL,
        artist_location     varchar, 
        artist_latitude     numeric,
        artist_longitude    numeric
    )
""") 

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        timestamp       varchar  NOT NULL, 
        hour            int      NOT NULL, 
        day             int      NOT NULL,
        week_of_year    int      NOT NULL,
        month           int      NOT NULL,
        year            int      NOT NULL,
        weekday         int      NOT NULL
    )
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (timestamp, user_id, level, song_id, artist_id, session_id, user_location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id)
    DO UPDATE 
        SET first_name = EXCLUDED.first_name,
            last_name  = EXCLUDED.last_name,
            gender     = EXCLUDED.gender,
            level      = EXCLUDED.level
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id)
    DO UPDATE
        SET title     = EXCLUDED.title,
            artist_id = EXCLUDED.artist_id,
            year      = EXCLUDED.year,
            duration  = EXCLUDED.duration
""")


artist_table_insert = ("""
    INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id)
    DO UPDATE 
        SET artist_name      = EXCLUDED.artist_name,
            artist_location  = EXCLUDED.artist_location,
            artist_latitude  = EXCLUDED.artist_latitude,
            artist_longitude = EXCLUDED.artist_longitude
""")


time_table_insert = ("""
    INSERT INTO time
    VALUES (%s, %s ,%s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
    SELECT song.song_id, song.artist_id 
    FROM (
        SELECT * 
        FROM songs
        WHERE songs.title = %s) AS song 
    JOIN (
        SELECT * 
        FROM artists
        WHERE artist_name = %s) AS artist
    ON song.artist_id = artist.artist_id
    WHERE song.duration = %s
""")

# QUERY LISTS

create_table_queries = [artist_table_create, user_table_create, song_table_create, songplay_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]