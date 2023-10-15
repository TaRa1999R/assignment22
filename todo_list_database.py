
import sqlite3

class Database () :

    def __init__ ( self ) :
        self.con = sqlite3.connect ("todo_list.db")
        self.cur = self.con.cursor ()

    def get_tasks ( self ) :
        query = f"SELECT * FROM tasks"
        result = self.cur.execute (query)
        tasks = result.fetchall ()
        print (tasks)

    def add_new_task ( self ) :
        ...

    def delete_task ( self ) :
        ...

    def update_task ( self ) :
        ...