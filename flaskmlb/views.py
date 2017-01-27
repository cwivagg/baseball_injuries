from flask import render_template
from flaskmlb import app
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2
from flask import request
from a_Model import ModelIt

user = 'cwivagg' #add your username here (same as previous postgreSQL)            
host = 'localhost'
dbname = 'mlb_db'
db = create_engine('postgres://%s%s/%s'%(user,host,dbname))
con = None
con = psycopg2.connect(database = dbname, user = user)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
       title = 'Home', user = { 'nickname': 'Miguel' },
       )

@app.route('/db')
def pitcher_page():
    sql_query = """                                                             
                SELECT * FROM mlb_data_table WHERE "Name"='wakefti01'\
;                                                                               
                """
    query_results = pd.read_sql_query(sql_query,con)
    iPitched = ""
    print query_results[:10]
    for i in range(0,10):
        iPitched += str(query_results.iloc[i]['IP'])
        iPitched += "<br>"
    return iPitched

@app.route('/db_fancy')
def pitcher_page_fancy():
    sql_query = """
               SELECT "index", "GameDate", "IP" FROM mlb_data_table WHERE "Name"='wakefti01';
                """
    query_results=pd.read_sql_query(sql_query,con)
    iPitched = []
    for i in range(0,query_results.shape[0]):
        iPitched.append(dict(index=query_results.iloc[i]['index'], GameDate=query_results.iloc[i]["GameDate"], IP=query_results.iloc[i]["IP"]))
    return render_template('innings_pitched.html',iPitched=iPitched)

@app.route('/input')
def primpredict_input():
    return render_template("input.html")

@app.route('/output')
def primpredict_output():
  #pull 'birth_month' from input field and store it
  ip = request.args.get('IP')
  era = request.args.get('ERA')
  age = request.args.get('ages')
  ip = float(ip.decode('utf-8'))
  era = float(era.decode('utf-8'))
  age = float(age.decode('utf-8'))
    #just select the Cesareans  from the birth dtabase for the month that the user inputs
  query = """
          SELECT "index", "Name", "GameDate", "targets" FROM mlb_data_table WHERE \
          "IP"='%f' AND "ERA"='%f' AND "ages"<'%d' AND "ages">'%d'
          """ % (ip, era, int(365.25*(age+1)),int(365.25*(age-1)))
  print query
  query_results=pd.read_sql_query(query,con)
  print query_results
  the_result = ModelIt(ip,era,age)
  return render_template("output.html", the_result = the_result)