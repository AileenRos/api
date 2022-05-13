from flask import Flask, jsonify, request
from config import config
from flask_mysqldb import MySQL


#servidor
app = Flask(__name__)

conexion=MySQL(app)

#comprobación 
@app.route('/estudiantes', methods=['GET'])
def index():
#Conexión a la base de datos
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT estudiantes id, nombre, correo, password FROM estudiantes"
        cursor.execute(sql)
        datos = cursor.fetchall()
        estudiantes = []
        for fila in datos:
            estudiantes = {'id':fila[0], 'nombre':fila[1],'correo':fila[2],'password':fila[3]}
            estudiantes.append(estudiantes)
            return jsonify({'estudiantes':estudiantes, 'mensaje':"Listado de alumnos"})
    except Exception as ex:
        return jsonify({'mensaje':"Error"})    

@app.route('/estudiantes/<id>', methods=['GET'])
def leer_e(id):
    try:
        cursor= conexion.connection.cursor()
        sql = "SELECT id, nombre, correo, password, FROM estudiantes WHERE id = '{0}'".format(id)
        cursor.excute(sql)
        if datos != None:
            datos = {'id':datos[0], 'nombre':datos[1],'correo':datos[2],'password':datos[3]}
    except Exception as ex:
        return jsonify({'mensaje':"Error"})         

#registro
@app.route('/registro/estudiantes', methods=['POST'])
def registro_estudiante():
    try:
        print (request.json)
        cursor= conexion.connection.cursor()
        sql = """INSERT INTO estudiantes (id, nombre, correo, password), VALUES ('{0}','{1}','{2}','{3}')""".format(request.json['id'],request.json['nombre'],request.json['correo'],request.json['password'])
        cursor.excute(sql)
        conexion.connection.commit() #confirma la acción de inserción
        return jsonify({'mensaje':"Estudiante registrado"})
    except Exception as ex:
        return jsonify({'mensaje':"Error"})

#cada vez que se encuentre un error 404 muestra este mensaje
def pagina_no_encontrada(error):
        return "<h1>Esta página no existe</h1>", 404

#actualización del servidor automáticamente
if __name__ == '__main__':
    #accediendo a config.py
    app.config.from_object(config['development'])
    #Manegajor de errores
    app.register_error_handler(404,pagina_no_encontrada)
    app.run()
