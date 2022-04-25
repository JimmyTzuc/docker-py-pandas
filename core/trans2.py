import psycopg2


ID = 1 
# transaction int, 
# Month VARCHAR (255), 
# Day int, 
# Credit_Type varchar (255)
con = psycopg2.connect(
     database="postgres",
     user='postgres',
     password='postgres',
     host='postgres',
     port='5432'
)
cur = con.cursor()

cur.execute("INSERT INTO TRANSACTIONS (ID,transaction, Month, Day, Credit_Type) VALUES (2, 3420, 'month', 4, 'ICT')");

con.commit()
print("Record inserted successfully")
con.close()
print("Database opened successfully")
