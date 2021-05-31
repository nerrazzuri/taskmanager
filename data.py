import sqlite3
from datetime import datetime

class Data:
    def __init__(self):
        self._connection = None
        self._cursor = None

    def connect(self):
        self._connection = sqlite3.connect('data.db')
        self._cursor = self._connection.cursor()

    def create_table(self):
        self._cursor.execute('CREATE TABLE task_manager(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, tasks TEXT, start DATE, end DATE, status TEXT)')
        self._connection.commit()

    def add_item(self, task, start_date, end_date, reminder):
        self._cursor.execute('INSERT INTO task_manager (tasks, start, end, status, reminder) VALUES ("{}", "{}", "{}", "{}", "{}")'.format(task, start_date, end_date, 'In Progress', reminder))
        self._connection.commit()

    def update_item(self, task_id, status):
        self._cursor.execute('UPDATE task_manager SET status = "{}" WHERE id = {}'.format(status, task_id))
        self._connection.commit()

    def select_item(self, status='All'):
        if status == 'All':
            cur = self._cursor.execute('SELECT * FROM task_manager')
        else:
            cur = self._cursor.execute('SELECT * FROM task_manager WHERE status = "{}"'.format(status))

        return cur

    def close_connection(self):
        if self._connection:
            self._connection.close()


if __name__ == '__main__':
    data = Data()
    data.connect()
    data.add_item('task A', '13-05-2021', '15-05-2021')