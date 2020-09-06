import psycopg2
def todo():
    create_db = (
        """CREATE TABLE tasks (task_id SERIAL PRIMARY KEY,task VARCHAR(255) NOT NULL)"""
    )
    postgres_insert = (
        """INSERT INTO tasks (task) VALUES(%s)""")
    connection = None
    try:
        connection = psycopg2.connect(user = 'postgres',
                                      password = 'password',
                                      host = '127.0.0.1',
                                      port='5432',
                                      database = 'postgres')
        cursor = connection.cursor()
        cursor.execute(create_db)

        exit = False
        print("Please input a task. Be sure to input done when you're through")
        while not exit:
            user_task = input()
            if user_task == 'done':
                exit = True
            else:
                cursor.execute(postgres_insert,[user_task])
        connection.commit()
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if connection is not None:
            connection.close()

print(todo())

