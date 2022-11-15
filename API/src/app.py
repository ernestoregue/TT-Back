from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
from config import config

import hashlib
from hashlib import md5

app = Flask(__name__)
CORS(app, resources={r"/map-api/*": {"origins": "*"}})
db = MySQL(app)


@app.route('/map-api', methods=['GET'])
def index():
    try:
        cur = db.connection.cursor()
        sql = "SELECT * FROM place"
        cur.execute(sql)
        data = cur.fetchall()
        places = []
        for row in data:
            place = {
                'id': row[0],
                'name': row[1],
                'hashtag': row[2],
                'city': row[3],
                'comment': row[4],
                'subjectivity': row[5],
                'polarity': row[6],
                'sentiment': row[7],
                'latitude': row[8],
                'longitude': row[9]
            }
            places.append(place)

        return jsonify({'places': places, 'Mensaje': "Datos obtenidos correctamente"})

    except Exception as e:
        return jsonify({'Mensaje': str(e)})


@app.route('/map-api/<id>', methods=['GET'])
def get_place(id):
    try:
        cur = db.connection.cursor()
        sql = "SELECT * FROM place WHERE place_id = '{0}'".format(id)
        cur.execute(sql)
        data = cur.fetchone()
        if data != None:
            place = {
                'id': data[0],
                'name': data[1],
                'hashtag': data[2],
                'city': data[3],
                'comment': data[4],
                'subjectivity': data[5],
                'polarity': data[6],
                'sentiment': data[7],
                'latitude': data[8],
                'longitude': data[9]
            }
            return jsonify({'place': place, 'Mensaje': "Datos obtenidos correctamente"})
        else:
            return jsonify({'Mensaje': "No se encontró el lugar"})

    except Exception as e:
        return jsonify({'Mensaje': str(e)})


@app.route('/map-api/<id>', methods=['DELETE'])
def delete_place(id):
    try:
        cur = db.connection.cursor()
        sql = "DELETE FROM place WHERE place_id = '{0}'".format(id)
        cur.execute(sql)
        db.connection.commit()
        return jsonify({'Mensaje': "Lugar eliminado correctamente"})

    except Exception as e:
        return jsonify({'Mensaje': str(e)})


@app.route('/map-api/<id>', methods=['PUT'])
def update_place(id):
    try:
        cur = db.connection.cursor()
        sql = "UPDATE place SET place_name = '{0}', place_hashtag = '{1}', place_city = '{2}', place_comment = '{3}', place_subjectivity = '{4}', place_polarity = '{5}', place_sentiment = '{6}', place_latitude = '{7}', place_longitude = '{8}' WHERE place_id = '{9}'".format(
            request.json['name'], request.json['hashtag'], request.json['city'], request.json['comment'], request.json['subjectivity'], request.json['polarity'], request.json['sentiment'], request.json['latitude'], request.json['longitude'], id)
        cur.execute(sql)
        db.connection.commit()
        return jsonify({'Mensaje': "Lugar actualizado correctamente"})

    except Exception as e:
        return jsonify({'Mensaje': str(e)})


@app.route('/map-api', methods=['POST'])
def add_place():
    try:
        cur = db.connection.cursor()
        sql = "INSERT INTO place (place_name, place_hashtag, place_city, place_comment, place_subjectivity, place_polarity, place_sentiment, place_latitude, place_longitude) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}')".format(
            request.json['name'], request.json['hashtag'], request.json['city'], request.json['comment'], request.json['subjectivity'], request.json['polarity'], request.json['sentiment'], request.json['latitude'], request.json['longitude'])
        cur.execute(sql)
        db.connection.commit()
        return jsonify({'Mensaje': "Lugar agregado correctamente"})
    except Exception as e:
        return jsonify({'Mensaje': str(e)})

# get users info


@app.route('/map-api/login', methods=['GET'])
def get_user():
    try:
        cur = db.connection.cursor()
        sql = "SELECT * FROM login_user"
        cur.execute(sql)
        data = cur.fetchall()
        users = []
        for user in data:
            user = {
                'user_id': user[0],
                'user_name': user[1],
                'user_last': user[2],
                'user_email': user[3],
            }
        users.append(user)
        return jsonify({'usuario': users, 'Mensaje': "Se obtuvieron los datos correctamente"})
    except Exception as e:
        return jsonify({'Mensaje': str(e)})

# get user by email


@app.route('/map-api/login/<email>', methods=['GET'])
def get_user_by_email(email):
    try:
        cur = db.connection.cursor()
        sql = "SELECT * FROM login_user WHERE user_email = '{0}'".format(email)
        cur.execute(sql)
        data = cur.fetchone()
        print(data)
        pass_hash = hashlib.md5("contraseña".encode()).hexdigest()
        print(pass_hash)
        print(data[4])

        if data != None:
            user = {
                'user_id': data[0],
                'user_name': data[1],
                'user_last': data[2],
                'user_email': data[3],
            }
            return jsonify({'usuario': user, 'Mensaje': "Datos obtenidos correctamente"})
        elif data[4] == password:
            return jsonify({'Mensaje': "No se encontró el usuario"})
        else:
            return jsonify({'Mensaje': "No se encontró el usuario"})

    except Exception as e:
        return jsonify({'Mensaje': str(e)})


# Handle errors


def page_not_found(e):
    return '<h1>Page not found. :( </h1>', 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    app.run()
