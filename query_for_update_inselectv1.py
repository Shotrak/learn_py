import psycopg2

try:
    #Попытка подключения к БД
    conn=psycopg2.connect(dbname='postgres', user='mrv_pg', password='dolbyshot1', host='127.0.0.1')
    print("Connected done")
except: 
    print("error to connect")
# получение объекта курсора
cursor = conn.cursor()

#SELECT
cursor.execute('SELECT * FROM client')
all_clients = cursor.fetchall()
print (all_clients)
#UPDATE
sql_update_query = """ update client set f_name = 'Иван' where f_name = 'Роман' """
cursor.execute(sql_update_query)
conn.commit()
res = cursor.rowcount
print (res, "Записей успешно обновлено")
#SELECT AFTER UPDATE
print ("таблица после обновления")
sql_select_query = """ select * from client """
cursor.execute(sql_select_query)
clients_au = cursor.fetchall()
print (clients_au)


cursor.close() # закрываем курсор
conn.close() # закрываем соединение
#Hello world