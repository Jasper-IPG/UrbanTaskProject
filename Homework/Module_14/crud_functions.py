"""Продуктовая база; Регистрация покупателей"""
import sqlite3

connection = sqlite3.connect('Vits.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
);
''')

connection.commit()
connection.close()

connection = sqlite3.connect('Users.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER NOT NULL,
balance INTEGER NOT NULL
);
''')

connection.commit()
connection.close()


def add_user(username, email, age):
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)',
                   (username, email, age, 1000))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    user_check = True
    check = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    if check.fetchone() is None:
        user_check = False
    connection.close()
    return user_check


def initiate_db():
    connection = sqlite3.connect('Vits.db')
    cursor = connection.cursor()
    for number in range(1, 5):
        check_product = cursor.execute("SELECT * FROM Products WHERE id=?", (number,))
        if check_product.fetchone() is None:
            cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                           (f'Продукт {number}', f'Описание {number}', f'Цена {number * 100}'))
        else:
            pass
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('Vits.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products


initiate_db()
