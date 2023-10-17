
import sqlite3

class Database () :

    def __init__ ( self ) :
        self.con = sqlite3.connect ("todo_list.db")
        self.cur = self.con.cursor ()

    def get_tasks ( self ) :
        query = f"SELECT * FROM tasks"
        result = self.cur.execute (query)
        tasks = result.fetchall ()
        return (tasks)


    def add_task ( self , title , description , date , time , periority) :
        try :
            query = f"INSERT INTO tasks(title, description, date, time, priority, state)\
                  VALUES ('{title}', '{description}', '{date}', '{time}', {periority}, 0)"
            self.cur.execute (query)
            self.con.commit ()
            return True
        
        except :
            return False


    def delete_task ( self , id ) :
        try :
            query = f"DELETE FROM tasks WHERE id = {id}"
            self.cur.execute (query)
            self.con.commit ()
            return True
        
        except :
            return False


    def update_task ( self , id , mode ) :
        try :
            t = "0"
            query = f"UPDATE tasks SET state = {mode} WHERE id = {id}"
            t+="1"
            self.cur.execute (query)
            t+="2"
            self.con.commit ()
            t+="3"
            return (t)
        
        except :
            return False