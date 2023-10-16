
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


    def add_new_task ( self , title , discription , date , time , periority) :
        try :
            query = f"INSERT INTO tasks(title, discription, date, time, priority, state)\
                  VALUES ('{title}', '{discription}', '{date}', '{time}', {periority}, 0)"
            self.cur.execute (query)
            self.con.commit ()
            return True
        
        except :
            return False


    def delete_task ( self , id ) :
        try :
            text = "0"
            query = f"DELETE FROM tasks WHERE id = {id}"
            text += "1"
            self.cur.execute (query)
            text += "2"
            self.con.commit ()
            text += "3"
            return True
        
        except :
            return (text)


    def update_task ( self , id , mode ) :
        query = f"UPDATE tasks SET state = {mode} WHERE id = {id}"
        self.cur.execute (query)
        self.con.commit ()