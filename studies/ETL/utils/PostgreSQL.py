import logging
import psycopg2
import configparser
import os

class PostgresDB:
    def __init__(self, logger=None, **kwargs):
        self.logger = logger
        if logger is None:
            self.logger = logging.getLogger(__name__)
        self.config_file = kwargs.get('config_file','')
        self.selection = kwargs.get('selection','')
        self.conn_type = kwargs.get('conn_type','')
        self.POSTGRESRDS_URL= kwargs.get('POSTGRES_RDS')
        self.port = kwargs.get('port','')

        if self.conf_file !="":
            self.read_config(self.config_file,self.selection)
        
        if self.conn_type == 'Postgres':
            if  self.POSTGRESRDS_URL !='':
                self.host_url = self.POSTGRESRDS_URL
                self.conn = self.get_connection()
        
        else:
            print("ERROR")
    
    def get_connection(self):

        try:
            conn =  psycopg2.connect(self.host_url)
            conn.autocommit = True
        except Exception as e:
            conn =  None
            self.logger.error("get_connection: " +  str(e))
    
    def check_connection(self, cursor):
        flag = False
        try:
            if cursor:
                cursor.execute("SELECT VERSION()")
                results = cursor.fetchone()
                if results:
                    flag = True

        except psycopg2.DatabaseError as e:
            self.logger.error("check_connection" +  str(e))
            conn = None
        
        except Exception as e:
            conn = None 
            self.logger.error("check_connection" +  str(e))
        
        return flag
    
    def get_cursor(self):
        cur = None
        try:
            if not self.conn:
                self.conn  = self.get_connection()
            
            if self.conn:
                cur =  self.conn.cursor()
        except psycopg2.DatabaseError as e:
            self.conn =  self.get_connection()
            self.logger.error("check_connection" +  str(e))
            conn = None
        
        except Exception as e:
            conn = None 
            self.logger.error("get_cursor" +  str(e))
        
        return conn, cur
    
    def close_connection(self,conn,cur):
        try:
            cur.close()
            conn.close()
        except psycopg2.DatabaseError as e:
            self.logger.error("close_connection" + str(e))
        return
    
    def read_config(self,config_file,section):
        config = configparser.ConfigParser()
        config.read(config_file)
        self.port =  1521
        self.POSTGRESRDS_URL = config.get("POSTGRESDB",'POSTGRES_HOST_URL')
    
    def get_data(self,query,values):
        cur = None
        status = -1
        resultset = []
        try:
            cur =  self.get_cursor()
            if True:
                cur.arraysize = 50000
                cur.execute(query,values)
                resultset = cur.fetchall()
                status = 0
        except psycopg2.DatabaseError as e:
            self.conn =  self.get_connection()
            self.logger.error("check_connection" +  str(e))
            conn = None
        
        except Exception as e:
            conn = None 
            self.logger.error("get_cursor" +  str(e))
        
        return status, resultset
    

    def set_data(self,query,values):
        cur = None
        status = -1
        resultset = []
        try:
            cur =  self.get_cursor()
            cur.execute(query,values)
            cur.commit()
            status = 0

        except psycopg2.DatabaseError as e:
            self.logger.error("check_connection" +  str(e))
            status = 1
            resultset = e
            cur.close()
            return status,resultset
        
        except Exception as e:
            conn = None 
            self.logger.error("set_data" +  str(e))
        
        return status, resultset
    
    def add_data(self,query,values):
        cur = None
        status = -1
        resultset = []
        try:
            cur =  self.get_cursor()
            cur.execute(query,values)
            cur.commit()
            status = 0

        except psycopg2.DatabaseError as e:
            self.logger.error("check_connection" +  str(e))
            status = 1
            resultset = e
            cur.close()
            return status,resultset
        
        except Exception as e:
            self.logger.error("add_data" +  str(e))
            resultset = e
        
        return status, resultset
    
    def delete_data(self,query,values):
        cur = None
        status = -1
        resultset = []
        try:
            cur =  self.get_cursor()
            cur.execute(query,values)
            cur.commit()
            status = 0

        except psycopg2.DatabaseError as e:
            self.logger.error("check_connection" +  str(e))
            status = 1
            resultset = e
            cur.close()
            return status,resultset
        
        except Exception as e:
            self.logger.error("delete_data" +  str(e))
            resultset = e
        
        return status, resultset
    
    def get_tbl_cols(self,query,values):
        cur = None
        status = -1
        resultset = []
        try:
            cur = self.getcursor()
            if True:
                cur.arraysize = 1
                cur.execute(query,values)
                col_names = []
                for i in range(0,len(cur.description)):
                    col_names.append(cur.description[i][0])
                    resultset = col_names
                    status = 0
        except psycopg2.DatabaseError as e:
            self.logger.error("check_connection" +  str(e))
            status = 1
            resultset = e
            cur.close()
            return status,resultset
        
        except Exception as e:
            self.logger.error("delete_data" +  str(e))
            resultset = e
        
        return status, resultset
    
    def get_tbl_clm_dtypes(self,query,values):
        cur = None
        status = -1
        resultset = []
        try:
            cur = self.getcursor()
            if True:
                cur.arraysize = 1
                cur.execute(query,values)
                col_name_dtypes = []
                for row in [row[1] for row in cur.description]:
                    row = str(row)
                    row = row.replace('class','')
                    row = row.replace('psycopg2','')
                    row = row.replace('DbType DB_TYPE_','')
                    row = row.replace('<','')
                    row = row.replace('>','')
                    row = row.replace("'",'')
                    col_name_dtypes.append(row)
                    resultset = col_name_dtypes
                    status = 0
        except psycopg2.DatabaseError as e:
            self.logger.error("clm_tbl_dtp" +  str(e))
            status = 1
            resultset = e
            cur.close()
            return status,resultset
        
        except Exception as e:
            self.logger.error("clm_tbl_dataype" +  str(e))
            resultset = e
        
        return status, resultset
    
    def get_audit_log_key(self,audit_log_func_name,job_cd):
        cur =  None
        status = -1
        resultset = []
        try:
            cur = self.get_cursor()
            if True:
                cur.arraysize = 1
                aud_log_key = cur.callproc(audit_log_func_name, int, [job_cd])
        except psycopg2.DatabaseError as e:
            self.logger.error("clm_tbl_dtp" +  str(e))
            status = 1
            resultset = e
            cur.close()
            return status,resultset
        
        except Exception as e:
            self.logger.error("clm_tbl_dataype" +  str(e))
            resultset = e
        
        return status, aud_log_key
    
    def get_cur_user(self,cret_usr_id):
        cur =  None
        status = -1
        resultset = []
        try:
            cur = self.get_cursor()
            if True:
                cur.arraysize = 1
                aud_log_key = cur.callproc(cret_usr_id, str)
                status = 0
        except psycopg2.DatabaseError as e:
            self.logger.error("clm_tbl_dtp" +  str(e))
            status = 1
            resultset = e
            cur.close()
            return status,resultset
        
        except Exception as e:
            self.logger.error("clm_tbl_dataype" +  str(e))
            resultset = e
        
        return status, aud_log_key
    
    
    
        
