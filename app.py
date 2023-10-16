# import library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# Inisiasi object flask
app = Flask(__name__)

# Inisiasi object flask_restful
api = Api(app)

# inisiasi variabel kosong bertipe dictionary
identitas = {} # variabel global, dictionary = json

# Inisiasi object flask_cors
CORS(app)

# membuat class Resource
class ContohResource(Resource):
    # metode get dan post
    def get(self):
        # response = {"msg":"Hallo Dunia, ini app restful pertamaku"}
        return identitas
    
    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        alamat = request.form["alamat"]
        hobi = request.form["hobi"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        identitas["alamat"] = alamat
        identitas["hobi"] = hobi
        response = {"msg" : "Data berhasil dimasukan"}
        return response

    
# setup resourcenya
api.add_resource(ContohResource, "/api", methods=["GET","POST"])

if __name__ == "__main__":
    app.run(debug=True)