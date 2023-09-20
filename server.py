from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MySQL_HOST'] = 'localhost'
app.config['MySQL_USER'] = 'root'
app.config['MySQL_PASSWORD'] = ''
app.config['MySQL_DB'] = 'end_db'
mysql = MySQL(app)

@app.route('/Create', methods=['POST'])
def dataset():
    cur = mysql.connection.cursor()
    cur.execute(f"""CREATE DATABASE `end_db`""")
    mysql.connection.commit
    return("Database Created")

@app.route('/Create/Table', methods=["POST"])
def tableset():
    thy = mysql.connection.cursor()
    thy.execute(f"""USE `end_db`""")
    thy.execute("""CREATE TABLE IF NOT EXISTS `Create_note`(
                `id` INT PRIMARY KEY AUTO_INCREMENT,
                `Note_Title` VARCHAR(100) NOT NULL,
                `Note_Content` LONGTEXT NOT NULL,
                `Author` VARCHAR(50) NOT NULL,
                `Created_At` timestamp DEFAULT current_time); 
                """)
    mysql.connection.commit
    return("Table Created")

@app.route('/Create/modify/table', methods=["POST", "GET", "PUT", "DELETE"])
def create_note():
    Insert = mysql.connection.cursor()
    Insert.execute(f"""USE `end_db`""")
    if request.method == 'POST':
        id = request.json['id']
        note_title = request.json['note_title']
        note_content = request.json['note_content']
        author = request.json['author']
        created_at = request.json['created_at']
        Insert.execute(f"""INSERT INTO `Create_note` VALUES (%s, %s, %s, %s, %s)""",
                    (id, note_title, note_content, author, created_at))
        mysql.connection.commit()
        return jsonify(id, note_title, note_content, author, created_at)   
    elif request.method == 'GET':
        id = request.json['id']
        Insert.execute(f"""SELECT * FROM `Create_note` WHERE id = %s""",(id))
        feedback = Insert.fetchall()
        mysql.connection.commit()
        return jsonify(feedback)
    elif request.method == 'PUT':
        id = request.json['id']
        note_title = request.json['note_title']    
        Insert.execute(f"""UPDATE `Create_note` SET Note_Title = %s WHERE id = %s """,(note_title, id))
        mysql.connection.commit()
        return jsonify(id, note_title)
    elif request.method == 'DELETE':
        id = request.json['id']
        Insert.execute(f"""DELETE FROM `Create_note` WHERE id = %s""",(id))
        mysql.connection.commit()
        return "Successful"
    else:
        return "Syntax malfunction"    
if(__name__=='__main__'):
    app.run(debug=True)