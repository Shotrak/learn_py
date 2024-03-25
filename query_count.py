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
all_clients = cursor.rowcount
print(all_clients)
if all_clients > 0:
    print ("1")
else:
    print("2")

sql_update_query = "update client set f_name = 'Иван' where f_name = 'Роман'"
cursor.execute(sql_update_query)
update_clients = cursor.rowcount
print("updated:",update_clients)

cursor.close() # закрываем курсор
conn.close() # закрываем соединение
if conn.close = True:
    logging.info("Соединение закрыто")