from server import *

import os

os.environ['PGPASSWORD'] = '12345'

from flask import Flask, render_template, jsonify, request
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

@app.route('/login-user', methods=['POST'])
def login_user():
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        
        usuario_valido = Usuario.query.filter_by(nombre_usuario=usuario, contrasena=contrasena).first()

        if usuario_valido:
            mensaje = f'Inicio de sesión exitoso. Bienvenido, {usuario}!'
        else:
            mensaje = 'Inicio de sesión fallido. Usuario o contraseña incorrectos.'
        return mensaje


@app.route('/create-receta', methods=['POST'])
def create_receta():
    medicamento = request.form.get('medicamento')
    tipo_de_toma = request.form.get('tipo_de_toma')
    cantidad = int(request.form.get('cantidad'))
    unidad_medida = request.form.get('unidad_medida')
    porcentaje = float(request.form.get('porcentaje'))
    ml_g = float(request.form.get('ml_g'))

    if not medicamento or not tipo_de_toma or not cantidad or not unidad_medida or not porcentaje or not ml_g:
        return jsonify({'success': False, 'message': 'Todos los campos son requeridos'}), 400
    total = cantidad * porcentaje

    receta = Receta(medicamento=medicamento, tipo_de_toma=tipo_de_toma, cantidad=cantidad, unidad_medida=unidad_medida, porcentaje=porcentaje, ml_g=ml_g, total=total)
    db.session.add(receta)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Receta creada exitosamente'}), 201


@app.route('/create-delivery', methods=['POST'])
def create_delivery():
    direccion = request.form.get('direccion')
    vehiculo = request.form.get('vehiculo')
    placa = request.form.get('placa')
    metodo_pago = request.form.get('metodo_pago')
    hora_entrega = request.form.get('hora_entrega')

    if 'image_pedido' not in request.files:
        return jsonify({'success': False, 'message': 'No image provided'}), 400
    
    file = request.files['image_pedido']

    if file.filename == '':
        return jsonify({'success': False, 'message': 'No image provided'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'success': False, 'message': 'File extension not allowed'}), 400
    
    delivery = Delivery(direccion, vehiculo, placa, metodo_pago, hora_entrega)
    db.session.add(delivery)
    db.session.commit()
    
    cwd = os.getcwd()

    delivery_dir = os.path.join(app.config['UPLOAD_FOLDER'], str(delivery.id))
    os.makedirs(delivery_dir, exist_ok=True)

    upload_folder = os.path.join(cwd, delivery_dir)

    absolute_path = os.path.join(upload_folder, file.filename)
    file.save(absolute_path)
    file.close()

    relative_path = os.path.join(delivery_dir, file.filename)

    delivery.image_path = relative_path
    db.session.commit()

    return jsonify({'success': True, 'id': delivery.id, 'message': 'Delivery created successfully'}), 201
