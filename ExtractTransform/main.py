import requests, json, psycopg2

#conexão banco de dados
host = 'localhost'
dbname = 'desafio_cross'
user = 'postgres'
password = 'postgres'
conn_string = 'host={0} dbname={1} user={2} password={3}'.format(host, dbname, user, password)
conn = psycopg2.connect(conn_string)
sql = conn.cursor()

pageint = 1
numbers = []
while True:
    try:
        pagestr = str(pageint)
        url = 'http://challenge.dienekes.com.br/api/numbers?page=' + pagestr
        response = requests.get(url)
        results = response.json()
        if not results['numbers']:
            break
        pageint = pageint + 1
        numbers += results['numbers']
    except:
        print('tratativa erro simulado!')

n = len(numbers)
for num in range(n - 1, 0, -1):
    for contador in range(num):
        if numbers[contador] > numbers[contador + 1]:
            numbers[contador], numbers[contador + 1] = numbers[contador + 1], numbers[contador]
for number in numbers:
    numberstr = str(number)
    sql.execute("INSERT INTO cross_commerce (numbers) VALUES("+ numberstr +");" )
conn.commit()
sql.close()
conn.close()