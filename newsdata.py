#!/usr/bin/env python3
import psycopg2
import traceback
import sys
DBNAME = "news"

"""Connect to DB"""


def database_connect():
    try:
        db = psycopg2.connect(database=DBNAME)
        return db
    except psycopg2.Error as e:
        print("Unable to connect to the database")
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)

"""Return results in a SQL like table"""


def print_table(crsr, data):
    widths = []
    columns = []
    tavnit = '|'
    separator = '+'
    for cd in crsr.description:
        widths.append(len(cd[0]))
        columns.append(cd[0])

    for w in widths:
        tavnit += " %-"+"%ss |" % (w,)
        separator += '-'*w + '--+'

    print(separator)
    print(tavnit % tuple(columns))
    print(separator)
    for row in data:
        print(tavnit % row)
    print(separator)

"""Return table of all articles and respective view counts"""


def see_article_views(db):
    c = db.cursor()
    sql_select_query = """SELECT articles.title,
        count(log.status) as article_views
        from articles left join log
        on log.path ILIKE '%' || articles.slug
        where log.status = '200 OK'
        group by articles.title order by article_views DESC;"""
    c.execute(sql_select_query)
    result = c.fetchall()
    print_table(c, result)
    return c.fetchall()

"""Return table of authors and their rspective aggregated view count"""


def see_author_views(db):
    c = db.cursor()
    sql_select_query = """SELECT authors.name,
        count(log.status) as author_views
        from articles left join log on log.path ILIKE '%' || articles.slug
        join authors on authors.id = articles.author
        group by authors.name
        order by author_views DESC;"""
    c.execute(sql_select_query)
    result = c.fetchall()
    print_table(c, result)
    return c.fetchall()

"""Return table of all days with >1% 404 Errors"""


def see_error_days(db):
    c = db.cursor()
    sql_select_query = """create view http_requests as
        SELECT time::date as day, count(status) as total_requests,
        sum(case when status  = '404 NOT FOUND' then 1.0 else 0 end)
        as errors from log group by day;
        select day, TRUNC(errors / total_requests, 3) as error_percentage
        from http_requests where TRUNC(errors / total_requests, 3) > 0.01 """
    c.execute(sql_select_query)
    result = c.fetchall()
    print_table(c, result)
    return c.fetchall()

"""Run all three SQL queries in a row"""


def sql_queries():
    db = database_connect()
    see_article_views(db)
    see_author_views(db)
    see_error_days(db)
    db.close()

try:
    sql_queries()
except Exception:
    print(traceback.format_exc())
