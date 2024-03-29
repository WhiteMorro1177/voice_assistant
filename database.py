import sqlite3 as sql

DB_PATH = "data\\voice_assistant.db"



def select_option(tag: str):
    return Database.select_option(Database, tag)

def select_all_options():
    return Database.select_all_options(Database)

def select_app(tag: str):
    return Database.select_app(Database, tag)

def select_all_apps():
    return Database.select_all_apps(Database)
class Database:
    
    OPTIONS_TABLE_NAME = "options"
    OPTION_TAG = "option_tag"

    APPS_TABLE_NAME = "apps"
    APP_TAG = "tag"

    def get_cursor() -> sql.Cursor:
        return sql.connect(DB_PATH).cursor()
    
    def select_option(self, tag: str):  # select one record from "option" table by tag
        cursor = self.get_cursor()
        result_set = cursor.execute(f"select * from {self.OPTIONS_TABLE_NAME} where {self.OPTION_TAG} = '{tag}'").fetchall()
        cursor.close()
        return result_set

    def select_all_options(self):  # select all records from "options"
        cursor = self.get_cursor()
        result_set = cursor.execute(f"select * from {self.OPTIONS_TABLE_NAME}").fetchall()
        cursor.close()
        return result_set

    def select_app(self, tag: str):
        cursor = self.get_cursor()
        result_set = cursor.execute(f"select * from {self.APPS_TABLE_NAME} where {self.APP_TAG} = '{tag}'").fetchall()
        cursor.close()
        return result_set

    def select_all_apps(self):
        cursor = self.get_cursor()
        result_set = cursor.execute(f"select * from {self.APPS_TABLE_NAME}").fetchall()
        cursor.close()
        return result_set

    ''' for configuration mode (if i start working on it)
    
    
    def insert_option(self, record: tuple):
        cursor = self.get_cursor()
        cursor.execute(f"insert into {self.OPTIONS_TABLE_NAME} values (?, ?, ?)", record)
        cursor.close()

    def delete_option(self, id: int):
        cursor = self.get_cursor()
        cursor.execute(f"delete from {self.OPTIONS_TABLE_NAME} where {self.OPTION_ID} = ?", id)
        cursor.close()

    def delete_option(self, name: str):
        cursor = self.get_cursor()
        cursor.execute(f"delete from {self.OPTIONS_TABLE_NAME} where {self.OPTION_NAME} = ?", name)
        cursor.close()

    def update_option(self, id: int):
        pass

   def insert_app(self, name: str, tag: str):
        cursor = self.get_cursor()
        cursor.execute(f"insert into {self.OPTIONS_TABLE_NAME} values (?, ?, ?)", record)
        cursor.close()

    def delete_app(self, id: int):
        cursor = self.get_cursor()
        cursor.execute(f"delete from {self.OPTIONS_TABLE_NAME} where {self.OPTION_ID} = ?", id)
        cursor.close()

    def delete_app(self, name: str):
        cursor = self.get_cursor()
        cursor.execute(f"delete from {self.OPTIONS_TABLE_NAME} where {self.OPTION_ID} = ?", id)
        cursor.close()'''