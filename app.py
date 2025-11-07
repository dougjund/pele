from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/cursos', methods=['GET'])
def listar_cursos():
    cursos = [
        {"curso": "Harmonização Corporal com Glúteo", "data": "03/dez", "link": "https://www.even3.com.br/harmonizacao-corporal-com-gluteo-651624"},
        {"curso": "Harmonização Glútea", "data": "04/dez", "link": "https://www.even3.com.br/harmonizacao-glutea-644699"},
        {"curso": "Curso Full Face", "data": "05/dez", "link": "https://www.even3.com.br/preenchimento-facial-644563"},
        {"curso": "Curso Rinomodelação", "data": "06/dez", "link": "https://www.even3.com.br/curso-rinomodelacao-651191"},
        {"curso": "Endolaser facial e corporal", "data": "07/dez", "link": "https://www.even3.com.br/endolaser-facial-e-corporal-644501"},
        {"curso": "Curso Toxina Botulínica", "data": "09/dez", "link": "https://www.even3.com.br/curso-toxina-botulinica-644952"},
        {"curso": "Curso Bioestimuladores", "data": "10/dez", "link": "https://www.even3.com.br/curso-bioestimuladores-651215"},
        {"curso": "Curso Fios de PDO facial", "data": "11/dez", "link": "https://www.even3.com.br/curso-fios-de-pdo-facial-651253"},
        {"curso": "Curso Preenchimento Labial", "data": "12/dez", "link": "https://www.even3.com.br/curso-preenchimento-labial-651610"},
        {"curso": "Curso Preenchimento Corporal com Glúteo", "data": "13/dez", "link": "https://www.even3.com.br/curso-preenchimento-corporal-com-gluteo-651561"}
    ]
    return jsonify(cursos)

if __name__ == '__main__':
    app.run(debug=True)
