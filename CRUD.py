import psycopg2

class CRUD:
#######CREATE/INSERT#######
    def create(self):
        create_db = """CREATE TABLE Album(album_id SERIAL PRIMARY KEY,
                        album_name VARCHAR(255) NOT NULL,
                        author VARCHAR(255) NOT NULL)"""
        try:
            connection = psycopg2.connect(user='postgres',
                                          password='password',
                                          host='127.0.0.1',
                                          port='5432',
                                          database='postgres')
            cursor = connection.cursor()
            cursor.execute(create_db)
            create = (
                """INSERT INTO Album (album_name,author) VALUES(%s,%s)""")
            album = [('Guns and Roses', 'KISS'), ('ROTD', 'Dreamville')]
            cursor.executemany(create, album)
            connection.commit()
            print('Records',album[0],'and',album[1],'inserted into table')
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

        #######RETRIEVE######
    def retrieve(self):
        try:
            connection = psycopg2.connect(user='postgres',
                                          password='password',
                                          host='127.0.0.1',
                                          port='5432',
                                          database='postgres')
            cursor = connection.cursor()
            query = ("""SELECT author FROM Album WHERE album_name = %s""")
            cursor.execute(query, ['ROTD'])
            record = cursor.fetchone()
            print('Record',record,'has been retrieved from the database')
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)


    #######UPDATE#######
    def update(self):
        try:
            connection = psycopg2.connect(user='postgres',
                                          password='password',
                                          host='127.0.0.1',
                                          port='5432',
                                          database='postgres')
            cursor = connection.cursor()

            query = ("""UPDATE album set album_name= %s WHERE author = %s""")
            ex = [('Guns and Roses'), ('KISS')]
            cursor.execute(query, ex)
            connection.commit()
            print('Update Done')

        except(Exception, psycopg2.DatabaseError) as error:
            print(error)


    #######DELETE#######
    def delete(self):
        try:
            connection = psycopg2.connect(user='postgres',
                                          password='password',
                                          host='127.0.0.1',
                                          port='5432',
                                          database='postgres')
            cursor = connection.cursor()
            delete_query = ("""DELETE from album WHERE author = %s""")
            cursor.execute(delete_query, ['KISS'])
            connection.commit()
            cursor.close()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)


crud = CRUD()
crud.create()
crud.retrieve()
crud.update()
crud.delete()