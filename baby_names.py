import re, psycopg2

def save_baby_names(html_file):
    name_list = []
    with open(html_file, 'r') as NameFile:
        file_content = NameFile.readlines()
        for name in file_content:
            baby_name = re.findall(r"<li>(.*)</li>", name)
            if baby_name:
                name_list.append(baby_name[0])

    baby_names = name_list
    create_db = (
        """CREATE TABLE baby_names (name VARCHAR(255) NOT NULL)"""
    )
    try:
        connection = psycopg2.connect(user='postgres',
                                      password='password',
                                      host='127.0.0.1',
                                      port='5432',
                                      database='postgres')
        cursor = connection.cursor()
        cursor.execute(create_db)

        for b_name in baby_names:
            insert_query = """INSERT INTO baby_names(name) VALUES(%s) """
            cursor.execute(insert_query, [b_name])
            connection.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)



save_baby_names('baby_names.html')
