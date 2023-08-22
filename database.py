"""
Records
"""
import sqlite3

bd = sqlite3.connect("2048.sqlite")
cur = bd.cursor()
cur.execute(
    """
create table if not exists Records (
    name text,
    score integer
)"""
)


def insert_result(name, score):
    cur.execute(
        """
        insert into Records values(?,?)
        """,
        (name, score),
    )
    bd.commit()


def get_best():
    cur.execute(
        """
    SELECT name, max(score) as score FROM Records
    GROUP BY 1
    ORDER BY 2 DESC
    """
    )
    return cur.fetchall()
