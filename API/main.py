from fastapi import FastAPI
import requests, json, psycopg2

#conexão banco de dados
host = 'localhost'
dbname = 'desafio_cross'
user = 'postgres'
password = 'postgres'
conn_string = 'host={0} dbname={1} user={2} password={3}'.format(host, dbname, user, password)
conn = psycopg2.connect(conn_string)
sql = conn.cursor()

app = FastAPI()
sql.execute("SELECT numbers FROM cross_commerce")
numbers = sql.fetchall()

@app.get("/")
async def root():
    return numbers


