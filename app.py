#!/usr/bin/env python3

import psycopg2

try:
    conn = psycopg2.connect("dbname=news")

    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()

    # What are the most popular three articles of all time?
    cursor.execute("""
        SELECT a.title, COUNT(log.id) AS views
        FROM articles AS a
        JOIN log ON (log.path = CONCAT('/article/', a.slug))
        GROUP BY a.id
        ORDER BY views DESC
        Limit 3
    """)


    print ('1- What are the most popular three articles of all time?')
    rows = cursor.fetchall()
    for x in rows:
        print(' - ', x[0], ' - ', x[1], ' views')


    # Who are the most popular article authors of all time?
    cursor.execute("""
        SELECT a.name, COUNT(log.id) AS views
            FROM authors AS a
            JOIN articles AS b ON (a.id = b.author)
            JOIN log ON (log.path = CONCAT('/article/', b.slug))
            GROUP BY a.id
            ORDER BY views DESC
    """)
    print ('\n')
    print ('2- Who are the most popular article authors of all time?')

    rows = cursor.fetchall()
    for x in rows:
        print(' - ', x[0], ' — ', x[1], ' views')


    # On which days did more than 1% of requests lead to errors?
    cursor.execute("""
        SELECT
            logs.day,
            ROUND(error_logs.views * 100.0 / logs.views, 2) AS error
            FROM (
                SELECT DATE(time) AS day, COUNT(id) AS views
                FROM log
                GROUP BY day
            ) AS logs
            INNER JOIN (
                SELECT DATE(time) AS day, COUNT(id) AS views
                FROM log
                WHERE status != '200 OK'
                GROUP BY day
            ) AS error_logs ON logs.day = error_logs.day
            WHERE ROUND(error_logs.views * 100.0 / logs.views, 2) > 1.00
            ORDER BY error DESC
    """)
    print ('\n')
    print ('3. On which days did more than 1% of requests lead to errors?')

    rows = cursor.fetchall()
    for x in rows:
        print(' - ', x[0], ' — ', x[1], ' views')

except:
    print ("Unable to connect to the database")
