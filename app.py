#!/usr/bin/python3
from flask import Flask, render_template, url_for, jsonify
from flask_mysqldb import MySQL
# from flask_assets import Environment, Bundle
import datetime


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'database-3.c8nb4zcoufs1.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'lovetumolabs'
app.config['MYSQL_DB'] = 'ClimateNet'
mysql = MySQL(app)


@app.route('/home')
@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/data/<data_type>', methods=['GET'])
def get_data(data_type):
    cursor = mysql.connection.cursor()
    sql = "SELECT " + str(data_type) + ", data_and_time FROM Data"
    cursor.execute(sql)
    rows = cursor.fetchall()
    date_and_time = [ i[1] for i in rows]
    data = [i[0] for i in rows]
    datetime_strings = [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in date_and_time]
    return render_template('show_data.html', js_dates=datetime_strings, data=data, data_type=data_type)
    # return jsonify(data_and_time, data)

@app.route('/about_us')
def show_about():
    return render_template('about.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')


if __name__ == "__main__":
    app.run(debug=True)

