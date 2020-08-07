# Sparkify <img src='https://s3.amazonaws.com/video.udacity-data.com/topher/2018/May/5b06cfa8_3-4-p-query-a-digital-music-store-database1/3-4-p-query-a-digital-music-store-database1.jpg' align="right" height="140" />

This is the first project of Udacitys Data Engineering Nanodegree. In this project, a database for storing music and artist records is created.

Here are other **Sparkify** projects built on different database:

[Data Warehouse: AWS Redshift]() 

## Overview

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

In this project,

- data modeling is implemented with Postgres.
- an ETL pipeline is built using Python which will transform data from JSON files to dimension and fact tables using "star" schema.

### Dimension Tables

- users: users in the music app.
- songs: songs in the database.
- artists: artists in the database.
- time: timestamp of records in `songplays` broken down into specific units.

### Fact Table

- songplays: records in the log data associated with song plays.

### ETL Pipeline

- transfers data from two local directories (data/song_data, data/log_data) into the tables using SQL and Python.

## Getting Started

### Prerequisites

These are the Python libraries involved in this project:

```console
pandas==0.23.3
psycopg2==2.8.5
```

You can install the depedency by running the following command in the terminal.

```console
foo@bar:~$ pip3 install requirement.txt
```

### Set up the database

Create a fresh instance of the `sparkifydb` with empty tables by running

```console
foo@bar:~$ python create_table.py
```

Then execute the pipeline to read data from data files and transfer to respective tables.

```console
foo@bar:~$ python etl.py
```

## Usage

### Python

``` Python
import psycopg2
conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
cur = conn.cursor()
cur.execute("Some SQL query")
conn.commit()
```

### SQL query in Jupyter Notebook

```Python
%load_ext sql
%sql postgresql://student:student@127.0.0.1/sparkifydb
%sql "...Some SQL queries here..."
```

| :exclamation:  Note  |
|----------------------|
|Remember to restart the notebook to close the connection to your database. Otherwise, you won't be able to run your code in `create_tables.py`, `etl.py`, or `etl.ipynb` files since you can't make multiple connections to `sparkifydb`|