#Запускается селект который считает кол-во записей по условию, если их больше 0, то он их затирает нужными данными
import psycopg2 #подключение к Postgre
import logging #для логирования
logging.basicConfig(level=logging.INFO, filename="/sambashare/share/dev/py3/py.log",filemode="w",format="%(asctime)s %(levelname)s %(message)s") #Каждое выполнение затирает файл, пофиксить
logging.debug("A DEBUG Message")

try:
    #Попытка подключения к БД
    conn=psycopg2.connect(dbname='postgres', user='mrv_pg', password='dolbyshot1', host='127.0.0.1')
    logging.info(f"Подключение к БД успешно")
    print("Connected done")
except: 
   logging.error("Подключение к БД не успешно",exc_info=True)
   print("error to connect")
# получение объекта курсора
cursor = conn.cursor()

sql_select_query = """ select count (*) from client c where f_name = 'Роман' """
cursor.execute(sql_select_query)
all_clients = cursor.fetchall()
null_clients = """ select count (*) from client c where f_name = 'БЛАБЛА' """
cursor.execute(null_clients)
all_clients_0 = cursor.fetchall()
#print (all_clients)

if all_clients > all_clients_0 :
   print ("Найдено : ", all_clients) 
   sql_update_query = """ update client set f_name = 'Иван' where f_name = 'Роман' """
   cursor.execute(sql_update_query)
   sql_after_update = cursor.rowcount
   conn.commit()
   #sql_after_update = cursor.fetchall()
   print("Обновлено строк: ", sql_after_update)
else:
    print("Строки не найдены")

cursor.close() # закрываем курсор
conn.close() # закрываем соединение