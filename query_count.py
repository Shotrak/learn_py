import psycopg2 #подключение к Postgre
try:
    #Попытка подключения к БД
    conn=psycopg2.connect(dbname='postgres', user='mrv_pg', password='dolbyshot1', host='127.0.0.1')
    print("Connected done")
except: 
   logging.error("Подключение к БД не успешно",exc_info=True)
   print("error to connect")
# получение объекта курсора
cursor = conn.cursor()

sql_select_query = """ select count (*) from client c where f_name = 'Роман' """
cursor.execute(sql_select_query)
all_clients = cursor.fetchone(1)
print(all_clients)