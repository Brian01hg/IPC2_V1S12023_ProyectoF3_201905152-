import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/usuarios')
def obtener_usuarios():
    usuarios = [
        {
            "rol": "cliente",
            "nombre": "John",
            "apellido": "Doe",
            "telefono": "123456789",
            "correo": "john.doe@example.com",
            "contrasena": "mipassword123"
        },
        {
            "rol": "administrador",
            "nombre": "Jane",
            "apellido": "Smith",
            "telefono": "987654321",
            "correo": "jane.smith@example.com",
            "contrasena": "password456"
        }
    ]
    return jsonify({"usuario": usuarios})

@app.route('/categorias_peliculas')
def obtener_categorias_peliculas():
    categorias = [
        {
            "nombre": "Acción",
            "peliculas": {
                "pelicula": [
                    {
                        "titulo": "Avengers: Endgame",
                        "director": "Joe Russo, Anthony Russo",
                        "anio": "2019",
                        "fecha": "2023-06-05",
                        "hora": "18:30",
                        "imagen": "https://usaccinema.com/image1.png",
                        "precio": "42"
                    },
                    {
                        "titulo": "John Wick",
                        "director": "Chad Stahelski",
                        "anio": "2014",
                        "fecha": "2023-06-06",
                        "hora": "20:00",
                        "imagen": "https://usaccinema.com/image2.png",
                        "precio": "45"
                    },
                    {
                        "titulo": "Misión Imposible: Fallout",
                        "director": "Christopher McQuarrie",
                        "anio": "2018",
                        "fecha": "2023-06-07",
                        "hora": "19:15",
                        "imagen": "https://usaccinema.com/image2.png",
                        "precio": "55"
                    }
                ]
            }
        },
        {
            "nombre": "Comedia",
            "peliculas": {
                "pelicula": [
                    {
                        "titulo": "Deadpool",
                        "director": "Tim Miller",
                        "anio": "2016",
                        "fecha": "2023-06-05",
                        "hora": "20:30",
                        "imagen": "https://usaccinema.com/image5.png",
                        "precio": "65"
                    },
                    {
                        "titulo": "Superbad",
                        "director": "Greg Mottola",
                        "anio": "2007",
                        "fecha": "2023-06-06",
                        "hora": "21:00"
                    },
                    {
                        "titulo": "Bridesmaids",
                        "director": "Paul Feig",
                        "anio": "2011",
                        "fecha": "2023-06-07",
                        "hora": "20:15",
                        "imagen": "https://usaccinema.com/image3.png",
                        "precio": "42"
                    }
                ]
            }
        }
    ]
    return jsonify({"categoria": categorias})

@app.route('/salas')
def obtener_salas():
    salas = {
        "cine": {
            "nombre": "Cine ABC",
            "salas": {
                "sala": [
                    {
                        "numero": "#USACIPC2_202212333_1",
                        "asientos": "100"
                    },
                    {
                        "numero": "#USACIPC2_202212333_2",
                        "asientos": "80"
                    },
                    {
                        "numero": "#USACIPC2_202212333_3",
                        "asientos": "120"
                    }
                ]
            }
        }
    }
    return jsonify(salas)

@app.route('/tarjetas')
def obtener_tarjetas():
    tarjetas = [
        {
            "tipo": "Debito",
            "numero": "1234567890123456",
            "titular": "John Doe",
            "fecha_expiracion": "12/2024"
        },
        {
            "tipo": "Credito",
            "numero": "9876543210987654",
            "titular": "Jane Smith",
            "fecha_expiracion": "08/2023"
        }
    ]
    return jsonify({"tarjeta": tarjetas})

if __name__ == '__main__':
    app.run()