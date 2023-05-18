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

@app.route('/recetas', methods=['GET'])
def mostrarxº_recetas():
    recetas = Receta.query.all()
    serialized_recetas = [receta.serialize() for receta in recetas]
    return jsonify(serialized_recetas)

@app.route('/recetas', methods=['GET'])
def obtener_receta(receta_id):
    receta = Receta.query.get(receta_id)
    if receta:
        serialized_receta = receta.serialize()
        return jsonify(serialized_receta)
    else:
        return jsonify({'mensaje': 'Receta no encontrada'})
    
@app.route('/recetas', methods=['POST'])   
def crear_receta():
    
    medicamento = request.form.get('medicamento')
    tipo_de_toma = request.form.get('tipo_de_toma')
    cantidad = request.form.get('cantidad')
    unidad_medida = request.form.get('unidad_medida')
    porcentaje = request.form.get('porcentaje')
    ml_g = request.form.get('ml_g')

    nueva_receta = Receta(medicamento, tipo_de_toma, cantidad, unidad_medida, porcentaje, ml_g)

    db.session.add(nueva_receta)
    db.session.commit()

    return jsonify({'mensaje': 'Receta creada exitosamente'})

@app.route('/cajero', methods=['POST'])   
def crear_cajero():
    
    registro_inscripcion = request.form.get('registro_inscripcion')
    verificacion = request.form.get('verificacion')
    necesidad = request.form.get('necesidad')
    validacion = request.form.get('validacion')
    costo = request.form.get('costo')
    entrega = request.form.get('entrega')

    
    nuevo_cajero = Cajero(registro_inscripcion, verificacion, necesidad, validacion, costo, entrega)

    
    db.session.add(nuevo_cajero)
    db.session.commit()

    return jsonify({'mensaje': 'Cajero creado exitosamente'})

@app.route('/cajero', methods=['POST'])   
def validar_cajero(cajero_id):
    cajero = Cajero.query.get(cajero_id)
    if cajero:
        
        cajero.validacion = True 

        db.session.commit()

        return jsonify({'mensaje': 'Cajero validado exitosamente'})
    else:
        return jsonify({'mensaje': 'Cajero no encontrado'})
