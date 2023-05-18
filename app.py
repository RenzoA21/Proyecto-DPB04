from server import *

import os

os.environ['PGPASSWORD'] = '12345'

from flask import (Flask, request, render_template)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/Pharmacy'
db = SQLAlchemy(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5006)
else:
    print('Importing {}'.format(__name__))
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOW_EXTENSIONS

@app.route('/create-user', methods=['POST'])
def create_user():
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    fecha_nacimiento = request.form.get('fecha_nacimiento')
    rol = request.form.get('rol')
    email = request.form.get('email')
    contrasena = request.form.get('contrasena')
    sexo = request.form.get('sexo')
    telefono = request.form.get('telefono')


    usuario = Usuario(nombre, apellido, fecha_nacimiento, rol, email, contrasena, sexo, telefono)
    
    db.session.commit()

    return jsonify({'success': True, 'id': usuario.id, 'message': 'Employee created successfully'}), 201

