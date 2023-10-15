from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_mail import Mail, Message
import random


app = Flask(__name__)
mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'restated.immortal@gmail.com'
app.config['MAIL_PASSWORD'] = 'suji@2004'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MySQL_HOST'] = 'localhost'
app.config['MySQL_USER'] = 'root'
app.config['MySQL_PASSWORD'] = ''
app.config['MySQL_DB'] = 'end_db'
mysql = MySQL(app)

@app.route('/emailer/table', methods=['POST'])
def emailer():
    character = "ABCdEfdgIj2350897KLmnhPO"
    verification = []
    for _ in range(5):
        verify = ''.join(random.choice(character))
        verification.append(verify)
    email = request.json['email']
    msg = Message(
          'Verification',
          sender = 'restated.immortal@gmail.com',
          recipients = [email]
        )
    msg.body = verification
    mail.send(msg)
    input_char = request.json['varchar']
    if input_char == verification:
         return 'You have been verified'
    else:
         return 'You have not been verified'

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

@app.route('/Create/table', methods=["POST"])
def create_note():
    Insert = mysql.connection.cursor()
    Insert.execute(f"""USE `end_db`""")
    id = request.json['id']
    note_title = request.json['note_title']
    note_content = request.json['note_content']
    author = request.json['author']
    created_at = request.json['created_at']
    Insert.execute(f"""INSERT INTO `Create_note` VALUES (%s, %s, %s, %s, %s)""",
                (id, note_title, note_content, author, created_at))
    mysql.connection.commit()
    return jsonify(id, note_title, note_content, author, created_at)   

@app.route('/Create/access/table', methods=["GET"])
def access_note():
        Insert = mysql.connection.cursor()
        Insert.execute(f"""USE `end_db`""")
        id = request.json['id']
        Insert.execute(f"""SELECT * FROM `Create_note` WHERE id = %s""",(id))
        feedback = Insert.fetchall()
        mysql.connection.commit()
        return jsonify(feedback)

@app.route('/Create/update/table', methods=["PUT"])   
def update_note():
        Insert = mysql.connection.cursor()
        Insert.execute(f"""USE `end_db`""")
        id = request.json['id']
        note_title = request.json['note_title']    
        Insert.execute(f"""UPDATE `Create_note` SET Note_Title = %s WHERE id = %s """,(note_title, id))
        mysql.connection.commit()
        return jsonify(id, note_title)

@app.route('/Create/delete/table', methods=["DELETE"])
def delete_entry_in_note():
        Insert = mysql.connection.cursor()
        Insert.execute(f"""USE `end_db`""")
        id = request.json['id']
        Insert.execute(f"""DELETE FROM `Create_note` WHERE id = %s""",(id))
        mysql.connection.commit()
        return "Successful"   
if(__name__=='__main__'):
    app.run(debug=True)