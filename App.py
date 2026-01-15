from flask import Flask, render_template, request

app = Flask(__name__)

def classificar_imc(imc):
    if imc < 16:
        return "Magreza grave"
    elif imc <= 16.9:
        return "Magreza moderada"
    elif imc <= 18.4:
        return "Magreza leve"
    elif imc <= 24.9:
        return "Peso normal"
    elif imc <= 29.9:
        return "Sobrepeso"
    elif imc <= 34.9:
        return "Obesidade grau I"
    elif imc <= 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

@app.route("/", methods=["GET", "POST"])
def index():
    imc = None
    classificacao = None

    if request.method == "POST":
        peso = float(request.form["peso"])
        altura = float(request.form["altura"])
        imc = peso / (altura ** 2)
        classificacao = classificar_imc(imc)

    return render_template("index.html", imc=imc, classificacao=classificacao)

app.run(debug=True)


