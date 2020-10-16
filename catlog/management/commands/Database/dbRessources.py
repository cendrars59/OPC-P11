# -*- coding: Utf-8 -*
# Package in order to manage
# - the connection to the database
# - the creation of the database and the associated schema

import os

import psycopg2


def connect():
    """Connect to Postgresql database."""
    conn = None
    try:
        conn = psycopg2.connect(user= "dick",
                                password = "rivers",
                                host = "localhost",
                                database = "pure",
                                port= "5432")

        return conn

    except (Exception, psycopg2.Error) as err:

        print(err)
    else:
        conn.close()
