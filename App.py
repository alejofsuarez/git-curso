from flask import Flask, render_template, request

app=Flask(__name__)
from form import Form

@app.route("/form/", methods=["GET", "POST"])
def formulario():
    login_form=Form(request.form)
    if request.method =="POST" and login_form.validate():
        """
        Aqui deben mostrar todos los datos enviados.
        """
    return render_template("form.html", #aca falta algo)


if __name__=="__main__":
    app.run(debug=True,port=8000)