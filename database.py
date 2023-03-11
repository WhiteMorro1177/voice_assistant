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
    OPTION_ID = "id"
    OPTION_NAME = "name"
    OPTION_TAG = "option_tag"
    OPTION_CMD_TAG = "command_tag"

    APPLICATIONS_TABLE_NAME = "Applications"
    APP_ID = "id"
    APP_NAME = "name"
    APP_TAG = "tag"

    def __init__(self) -> None:
        files = os.listdir()
        if (self.DB_PATH in files): return
        else: self.init_db()
    
    def get_cursor(self) -> sql.Cursor:
        return sql.connect(self.DB_PATH).cursor()

    def init_db(self):
        with self.get_cursor() as cursor:
            cursor.execute(f"create database ?", self.DB_NAME)
            cursor.execute(f"""create table if not exist ? (
                ? int primary key identity(1, 1),
                ? text not null,
                ? text not null,
                ? text not null);""", 
                (self.OPTIONS_TABLE_NAME, self.OPTION_ID, self.OPTION_NAME, self.OPTION_TAG, self.OPTION_CMD_TAG))

    # "Options" table
    def select_option(self, tag: str):
        with self.get_cursor() as cursor:
            cursor.execute(f"select * from {self.OPTIONS_TABLE_NAME} where {self.OPTION_TAG} = '{tag}'")
            return cursor.fetchall()

    def select_all_options(self):
        pass

    def insert_option(self, record: tuple):
        pass

    def delete_option(self, id: int):
        pass

    def delete_option(self, name: str):
        pass

    def update_option(self, id: int):
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