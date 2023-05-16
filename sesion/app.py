# Imports
from flask import (
    Flask, 
    request, 
    render_template
)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

# Configuración
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/employeesdb40'
db = SQLAlchemy(app)

# Modelos
class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), server_default=db.text('uuid_generate_v4()'))
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    job_title = db.Column(db.String(60), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('now()'))
    image = db.Column(db.LargeBinary, nullable=True)

    def __init__(self, first_name, last_name, job_title):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Employee %r %r>' % (self.first_name, self.last_name)


# Endpoints
@app.route('/', methods=['GET'])
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

# Start server
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5006)
else:
    print('Importing {}'.format(__name__))
