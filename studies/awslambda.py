import json 
import boto3
import sys
import logging
import pymysql

class rds_config:

    db_username = "username"
    db_password = "password"
    db_name = "ExampleDB" 

s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('planets')
def lambda_handler(event, context):
    bucketlist = []

    for bucket in s3.buckets.all():
        bucketlist.append(bucket.name)
        print(bucket.name)
    
    return {
        'statusCode':200,
        'body':bucketlist
    }

def lambda_handler2(event,context):
    response = table.get_item(
        key = {
            'id':'mercury'
        }
    )
    print(response)

    return{
        'statusCode' : 200,
        'body' : response
    }

def lambda_handler3(event,contect):
    table.put_item(
        Item = {
            'id': 'neptune',
            'temp':'super cold'
        }
    )
    response = "item added"
    return {
        'statusCode' : 200,
        'body': response
    } 

#rds settings
rds_host  = "rds-instance-endpoint"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

def handler(event, context):
    """
    This function fetches content from MySQL RDS instance
    """

    item_count = 0

    with conn.cursor() as cur:
        cur.execute("create table Employee ( EmpID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))")
        cur.execute('insert into Employee (EmpID, Name) values(1, "Joe")')
        cur.execute('insert into Employee (EmpID, Name) values(2, "Bob")')
        cur.execute('insert into Employee (EmpID, Name) values(3, "Mary")')
        conn.commit()
        cur.execute("select * from Employee")
        for row in cur:
            item_count += 1
            logger.info(row)
            #print(row)
    conn.commit()

    return "Added %d items from RDS MySQL table" %(item_count)