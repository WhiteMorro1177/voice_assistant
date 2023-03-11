import sqlite3 as sql
import os


class Database():

    '''
    DataBase:

        Options:

        id: int pk identity
        name: varchar(40) not null
        option_tag: varchar(20) not null
        command_tag: varchar(20) (if opt_tag == "alias") null

        Apps:

        id: int pk identity
        name: varchar(40) not null
        tag: varchar(20) not null

    '''

    DB_PATH = "storage.db"
    DB_NAME = "VoiceAssistantDB"

    OPTIONS_TABLE_NAME = "Options"
    APPLICATIONS_TABLE_NAME = "Applications"

    def __init__(self) -> None:
        files = os.listdir()
        if (self.DB_PATH in files): return
        else: self.init_db()
    
    def get_cursor(self) -> sql.Cursor:
        return sql.connect(self.DB_PATH).cursor()

    def init_db(self):
        with self.get_cursor() as cursor:
            cursor.execute(f"create database {self.DB_NAME}")
            cursor.execute(f"create table {self.OPTIONS_TABLE_NAME}()")


    # "Options" table
    def select_option(id: int):
        pass

    def select_all_options():
        pass

    def insert_option(name: str, option_tag: str, command_tag: str):
        pass

    def delete_option(id: int):
        pass

    def delete_option(name: str):
        pass

    def update_option(id: int):
        pass


    # "Applications" table
    def select_app(id: int):
        pass

    def select_all_apps():
        pass

    def insert_app(name: str, tag: str):
        pass

    def delete_app(id: int):
        pass

    def delete_app(name: str):
        pass

    def update_app(id: int):
        pass