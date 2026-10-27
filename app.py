from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/help")
def help():
    texto_ayuda_1 = "Introduce dos números válidos y selecciona una operación."
    texto_ayuda_2 = "Puedes usar +, -, * o / para realizar operaciones."
    texto_ayuda_3 = "Recuerda que no se puede dividir entre cero."
    texto_ayuda = [texto_ayuda_1, texto_ayuda_2, texto_ayuda_3]
    return render_template("help.html", texto_ayuda=texto_ayuda)

@app.route("/", methods=["GET", "POST"]) #PUT PATCH DELETE
def calculadora():
    resultado = None
    error = None
    numero1 = ""
    numero2 = ""

    if request.method == "POST":
        numero1 = request.form.get("numero1", "")
        numero2 = request.form.get("numero2", "")
        operacion = request.form.get("operacion", "")

        try:
            a = float(numero1)
            b = float(numero2)

            if operacion == "+":
                resultado = a + b
            elif operacion == "-":
                resultado = a - b
            elif operacion == "*":
                resultado = a * b
            elif operacion == "/":
                if b == 0:
                    error = "No se puede dividir entre cero."
                else:
                    resultado = a / b
            else:
                error = "Operación no válida."

        except ValueError:
            error = "Introduce dos números válidos."

    return render_template(
        "index.html",
        numero1=numero1,
        numero2=numero2,
        resultado=resultado,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True)









