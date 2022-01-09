from sqlalchemy import text
from sqlalchemy.engine import create_engine 
import configparser

def setupConfig(database,property):
    
    config = configparser.ConfigParser()
    config.read('./conf/rfam.conf')
    
    try:
        result = config.get(database,property)
        return result
    except configparser.NoSectionError:
        print('Property {} for connecntion not received'.format(property))
        exit()
    
    return result

def stringConnectDatabase():

    _user = setupConfig("mysql",'user')
    _host = setupConfig('mysql','host')
    _port = setupConfig('mysql','port')
    _database = setupConfig('mysql','database')

    _stringConnect = 'mysql+pymysql://{}@{}:{}/{}'.format(_user,_host,_port,_database)
    _stringConnect = _stringConnect.replace("'","")

    return _stringConnect

def queryDatabase():
    with open('./query/query1.txt') as query:
        strQuery = query.read()
    return strQuery

if __name__ == '__main__':

    stringConnect = stringConnectDatabase()
    stringQuery = queryDatabase()
    connectDatabase = create_engine(stringConnect)

    with connectDatabase.connect() as conn:
        query = text(stringQuery)
        result = conn.execute(query)

        print(result.fetchall())
