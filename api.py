from flask import Flask, jsonify
from pprint import pprint

app = Flask(__name__)

FRETES = {
    "SEDEX": 1.0,
    "AZUL": 1.2,
    "AMAZON": 1.4
}

@app.route("/frete/<int:cep>" , methods=["GET"])
def get_frete(cep):
    if (len( str(cep) ) >= 8):
        response_error = {
            "status": "error",
            "response": "Tamanho inválido"
        }
        return jsonify(response_error)
    
    

    first_num = int( str(cep)[0] )

    frete_value = 0


    if (first_num <= 2):
        frete_value = 6
    elif (first_num <= 4):
        frete_value = 8
    elif (first_num <= 6):
        frete_value = 10
    elif (first_num <= 9):
        frete_value = 12

    response_data = {
        "status": "OK",
        "response": {
            "SEDEX": 0,
            "AZUL": 0,
            "AMAZON": 0
        }
    }

    for frete, valor in FRETES.items():
        response_data["response"][frete] = frete_value*valor

    
    
    pprint(response_data)
    return jsonify(response_data)


if __name__ == "__main__":
    app.run(debug= True)
    

