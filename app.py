from flask import Flask, jsonify, request
from sqlalchemy import create_engine
import pandas as pd
import os

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    if request.method == 'GET':
        host=os.getenv('MYSQL_HOST')
        user=os.getenv('MYSQL_USER')
        password=os.getenv('MYSQL_PASSWORD')
        database ="dataengine_adminpanel"
        sql_query = "select * from Taxonomy_v6 limit 1000;"
        mysql_engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
        data = pd.read_sql_query(sql_query, con=mysql_engine)
    return jsonify({"record_count": len(data)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=9025)
