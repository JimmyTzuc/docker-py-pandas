import pandas
import psycopg2

def trans():
    df = pandas.read_csv("txns.csv")
    df['dt'] = pandas.to_datetime(df['Date'], format = '%m/%d')
    df['Month'] = df['dt'].dt.strftime('%B')
    df['Day'] = df['dt'].dt.strftime('%d')
    df['Credit_Type'] = df['Transaction'].apply(lambda x: 'Credit' if float(x) > 0 else 'Debit')

    print(df)
# def dbtrans(df):  
    # connection establishment
    conn = psycopg2.connect(
        database="postgres",
        user='postgres',
        password='postgres',
        host='postgres',
        port='5432'
    )
    conn.autocommit = True
    
    conn.autocommit = True
    cursor = conn.cursor()

    sql = '''CREATE TABLE IF NOT EXISTS TRANSACTIONS(ID int NOT NULL,\
    transaction int, Month VARCHAR (255), Day varchar (255), Credit_Type varchar (255));'''
    
    cursor.execute(sql)

    for i in range(len(df)): 
        id = (df.iloc[i,0])
        trans = (df.iloc[i,2])
        month = (df.iloc[i,4])
        day = (df.iloc[i,5])
        ctype = (df.iloc[i,6])
        datos=(id,trans,month,day,ctype)
        print(datos)
    #Creating queries
    # SQL query to execute
        query = "INSERT INTO transactions (ID,transaction, Month, Day, Credit_Type) VALUES(%s,%s,%s,%s,%s)" 
        cursor.execute(query, datos)
trans()