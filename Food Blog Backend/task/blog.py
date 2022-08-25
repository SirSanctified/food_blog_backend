import sqlite3
from sqlite3 import Error


def create_connection(db_file: str) -> sqlite3.Connection:
    """
    create a data connection with the specified database, if it doesn't exist it will be created
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_table(connection, create_table_query):
    """
    create a table using the provided query
    :param connection: connection object
    :param create_table_query: sqlite query
    :return:
    """
    try:
        c = connection.cursor()
        c.execute(create_table_query)
    except Error as e:
        print(e)


def main():
    data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
            "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
            "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}

    meals_table_query = '''CREATE TABLE IF NOT EXISTS meals(
    meal_id int PRIMARY KEY,
    meal_name text NOT NULL UNIQUE
    );'''
    ingredients_table_query = '''CREATE TABLE IF NOT EXISTS ingredients(
    ingredient_id int PRIMARY KEY,
    ingredient_name text NOT NULL UNIQUE
    );'''
    measures_table_query = '''CREATE TABLE IF NOT EXISTS measures(
    measure_id int PRIMARY KEY,
    measure_name text UNIQUE
    );'''
    meals_insert_query = '''INSERT INTO meals (meal_name)
VALUES(?)'''
    ingredients_insert_query = '''INSERT INTO ingredients (ingredient_name)
    VALUES(?)'''
    measures_insert_query = '''INSERT INTO measures (measure_name)
    VALUES(?)'''

    conn = create_connection('food_blog.db')
    create_table(conn, meals_table_query)
    create_table(conn, ingredients_table_query)
    create_table(conn, measures_table_query)

    cursor = conn.cursor()

    for meal in data['meals']:
        cursor.execute(meals_insert_query, (meal,))

    for ingredient in data['ingredients']:
        cursor.execute(ingredients_insert_query, (ingredient,))

    for measure in data['measures']:
        cursor.execute(measures_insert_query, (measure,))

    conn.commit()


if __name__ == '__main__':
    main()
