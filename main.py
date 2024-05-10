from flask import Flask, render_template,request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def index():

    return render_template('index.html')

@app.route('/calcular_forma', methods=['GET','POST'])

def calcular_forma():

    try:

        Plastico = float(request.form.get("Plastico"))
        Vidrio = float(request.form.get("Vidrio"))
        Papel = float(request.form.get("Papel"))

        CO2_Plastico = 3.5 * Plastico
        CO2_Vidrio = 1.18 * Vidrio
        CO2_Papel = 0.19 * Papel

        Resultado = CO2_Plastico + CO2_Vidrio + CO2_Papel
        Resultado = f"{Resultado:.2f}"

        return render_template('index.html', Resultado = Resultado)
    except:
        Plastico = 0.0
        Vidrio = 0.0
        Papel = 0.0

        CO2_Plastico = 3.5 * Plastico
        CO2_Vidrio = 1.18 * Vidrio
        CO2_Papel = 0.19 * Papel

        Resultado = CO2_Plastico + CO2_Vidrio + CO2_Papel
        Resultado = f"{Resultado:.2f}"

        return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)