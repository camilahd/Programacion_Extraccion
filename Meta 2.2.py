# Camila Elizabeth Hernandez Alaniz
# 951
# meta 2.2

from mysql.connector import connect, Error
#Ejercicio 1
class MySQLConnect:
    def __init__(self, host, user, password, database):
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self._connection = None
    @property
    def host(self):
        return self._host
    @host.setter
    def host(self, value):
        self._host = value
    @property
    def user(self):
        return self._user
    @user.setter
    def user(self, value):
        self._user = value
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        self._password = value
    @property
    def database(self):
        return self._database
    @database.setter
    def database(self, value):
        self._database = value

    def conectar(self):
        try:
            dbConexion = connect(host=self._host, user=self._user, password=self._password, database=self._database)
            print("Conexion exitosa")
            return dbConexion
        except Error as e:
            print(f"Error: {e}")
            return e

    def desconectar(self, dbConexion):
        if dbConexion:
            dbConexion.close()
            print("Desconexion exitosa")
        else:
            print("No hay una conexion activa")
"""
# Ejemplo
conexion_bd = MySQLConnect(host="localhost", user="root", password="Cam1", database="olimpiadas")
conexion = conexion_bd.conectar()
conexion_bd.desconectar(conexion)
"""


#Ejercicio 2
class PaisMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, id, nombre):
        connection = self.conectar()
        if connection:
            try:
                cursor = connection.cursor()
                sql = "INSERT INTO Pais (id, nombre) VALUES (%s, %s)"
                cursor.execute(sql, (id, nombre))
                connection.commit()
                print("Insercion exitosa")
                return True
            except Error as e:
                print(f"Error al insertar en la tabla Pais: {e}")
            finally:
                if cursor:
                    cursor.close()
                self.desconectar(connection)
        return False

    def editar(self, id, nuevo_nombre):
        connection = self.conectar()
        if connection:
            try:
                cursor = connection.cursor()
                # Validar
                existe_nombre_query = "SELECT COUNT(*) FROM Pais WHERE nombre = %s AND id != %s"
                cursor.execute(existe_nombre_query, (nuevo_nombre, id))
                existe_nombre = cursor.fetchone()[0]
                if existe_nombre == 0:
                    # El nombre no existe y se realiza la actualización
                    update_query = "UPDATE Pais SET nombre = %s WHERE id = %s"
                    cursor.execute(update_query, (nuevo_nombre, id))
                    connection.commit()
                    print("Edición exitosa.")
                else:
                    print("El nombre ya existe en la tabla Pais")
            except Error as e:
                print(f"Error al editar en la tabla Pais: {e}")
            finally:
                if cursor:
                    cursor.close()
                self.desconectar(connection)

    def eliminar(self, id):
        connection = self.conectar()
        if connection:
            try:
                cursor = connection.cursor()
                delete_query = "DELETE FROM Pais WHERE id = %s"
                cursor.execute(delete_query, (id,))
                connection.commit()
                if cursor.rowcount > 0:
                    print("Eliminacion exitosa")
                    return True
                else:
                    print("No se encontro el elemento con el ID")
            except Error as e:
                print(f"Error al eliminar en la tabla Pais: {e}")
            finally:
                if cursor:
                    cursor.close()
                self.desconectar(connection)
        return False

    def consultar(self, filtro):
        connection = self.conectar()
        resultados = []

        if connection:
            try:
                cursor = connection.cursor()
                select_query = f"SELECT * FROM Pais WHERE {filtro}"
                cursor.execute(select_query)
                resultados = cursor.fetchall()
            except Error as e:
                print(f"Error al consultar en la tabla Pais: {e}")
            finally:
                if cursor:
                    cursor.close()
                self.desconectar(connection)
        return resultados
"""
# Ejemplo
pais_db = PaisMySQL(host="localhost", user="root", password="Cam1", database="olimpiadas")
pais_db.insertar(id=1, nombre="Mexico")
pais_db.insertar(id=2, nombre="Canada")
pais_db.editar(id=1, nuevo_nombre="Estados Unidos Mexicanos")
pais_db.eliminar(id=2)
resultados = pais_db.consultar("nombre LIKE '%E%'")
print("Resultados de la consulta:", resultados)
"""


#Ejercicio 3
class OlimpiadaMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, id, year):
        connection = self.conectar()
        if connection:
            try:
                cursor = connection.cursor()
                sql = "INSERT INTO Olimpiada (id, year_olimpiada) VALUES (%s, %s)"
                cursor.execute(sql, (id, year))
                connection.commit()
                print("Insertion exitosa")
                return True
            except Error as e:
                print(f"Error al insertar en la tabla Olimpiada: {e}")
            finally:
                if cursor:
                    cursor.close()
                self.desconectar(connection)
        return False

    def editar(self, id, nuevo_year):
        connection = self.conectar()
        if connection:
            try:
                cursor = connection.cursor()
                # Validar
                existe_year_query = "SELECT COUNT(*) FROM Olimpiada WHERE year_olimpiada = %s AND id != %s"
                cursor.execute(existe_year_query, (nuevo_year, id))
                existe_year = cursor.fetchone()[0]
                if existe_year == 0:
                    # El año no existe y se realiza la actualización
                    update_query = "UPDATE Olimpiada SET year_olimpiada = %s WHERE id = %s"
                    cursor.execute(update_query, (nuevo_year, id))
                    connection.commit()
                    print("Edición exitosa")
                else:
                    print("El año ya existe en la tabla Olimpiada")
            except Error as e:
                print(f"Error al editar en la tabla Olimpiada: {e}")
            finally:
                if cursor:
                    cursor.close()
                self.desconectar(connection)

    def eliminar(self, id):
        connection = self.conectar()
        if connection:
            try:
                cursor = connection.cursor()
                delete_query = "DELETE FROM Olimpiada WHERE id = %s"
                cursor.execute(delete_query, (id,))
                connection.commit()
                if cursor.rowcount > 0:
                    print("Eliminacion exitosa")
                    return True
                else:
                    print("No se encontro el elemento con el ID")
            except Error as e:
                print(f"Error al eliminar en la tabla Olimpiada: {e}")
            finally:
                if cursor:
                    cursor.close()
                self.desconectar(connection)
        return False

    def consultar(self, filtro):
        connection = self.conectar()
        resultados = []

        if connection:
            try:
                cursor = connection.cursor()
                select_query = f"SELECT * FROM Olimpiada WHERE {filtro}"
                cursor.execute(select_query)
                resultados = cursor.fetchall()
            except Error as e:
                print(f"Error al consultar en la tabla Olimpiada: {e}")
            finally:
                if cursor:
                    cursor.close()
                self.desconectar(connection)
        return resultados
"""
#Ejmeplo
olimpiada_db = OlimpiadaMySQL(host="localhost", user="root", password="Cam1", database="olimpiadas")
olimpiada_db.insertar(id=1, year=2022)
olimpiada_db.insertar(id=2, year=2023)
olimpiada_db.editar(id=1, nuevo_year=2020)
olimpiada_db.eliminar(id=2)
resultados = olimpiada_db.consultar("year_olimpiada > 1990")
print("Resultados de la consulta:", resultados)
"""

#Ejercicio 4
class ResultadosMySQL(MySQLConnect):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        connection = self.conectar()
        if connection:
            try:
                cursor = connection.cursor()
                sql = "INSERT INTO Resultados (idOlimpiada, idPais, idGenero, oro, plata, bronce) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (idOlimpiada, idPais, idGenero, oro, plata, bronce))
                connection.commit()
                print("Insercion exitosa")
                return True
            except Error as e:
                print(f"Error al insertar en la tabla Resultados: {e}")
            finally:
                if cursor:
                    cursor.close()
                self.desconectar(connection)
        return False

    def editar(self, idOlimpiada, idPais, idGenero, nuevo_oro, nuevo_plata, nuevo_bronce):
        connection = self.conectar()
        if connection:
            try:
                cursor = connection.cursor()
                # Validar que los nuevos valores sean enteros positivos
                if nuevo_oro > 0 and nuevo_plata > 0 and nuevo_bronce > 0:
                    update_query = "UPDATE Resultados SET oro = %s, plata = %s, bronce = %s WHERE idOlimpiada = %s AND idPais = %s AND idGenero = %s"
                    cursor.execute(update_query, (nuevo_oro, nuevo_plata, nuevo_bronce, idOlimpiada, idPais, idGenero))
                    connection.commit()
                    print("Edicion exitosa")
                else:
                    print("Los nuevos valores deben ser enteros positivos")
            except Error as e:
                print(f"Error al editar en la tabla Resultados: {e}")
            finally:
                if cursor:
                    cursor.close()
                self.desconectar(connection)

    def eliminar(self, idOlimpiada, idPais, idGenero):
        connection = self.conectar()
        if connection:
            try:
                cursor = connection.cursor()
                delete_query = "DELETE FROM Resultados WHERE idOlimpiada = %s AND idPais = %s AND idGenero = %s"
                cursor.execute(delete_query, (idOlimpiada, idPais, idGenero))
                connection.commit()
                if cursor.rowcount > 0:
                    print("Eliminacion exitosa")
                    return True
                else:
                    print("No se encontró el elemento")
            except Error as e:
                print(f"Error al eliminar en la tabla Resultados: {e}")
            finally:
                if cursor:
                    cursor.close()
                self.desconectar(connection)
        return False

    def consultar(self, filtro):
        connection = self.conectar()
        resultados = []

        if connection:
            try:
                cursor = connection.cursor()
                select_query = f"SELECT * FROM Resultados WHERE {filtro}"
                cursor.execute(select_query)
                resultados = cursor.fetchall()
            except Error as e:
                print(f"Error al consultar en la tabla Resultados: {e}")
            finally:
                if cursor:
                    cursor.close()
                self.desconectar(connection)
        return resultados
#Ejemplo
resultados_db = ResultadosMySQL(host="localhost", user="root", password="Cam1", database="olimpiadas")
resultados_db.insertar(idOlimpiada=1, idPais=1, idGenero=3, oro=2, plata=1, bronce=1)
resultados_db.editar(idOlimpiada=1, idPais=1, idGenero=3, nuevo_oro=3, nuevo_plata=2, nuevo_bronce=1)
resultados_db.eliminar(idOlimpiada=1, idPais=1, idGenero=3)
resultados = resultados_db.consultar("idPais = 2")
print("Resultados de la consulta:", resultados)

