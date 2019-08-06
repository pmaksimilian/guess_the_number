from flask import Flask, request, make_response, render_template
import random

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    secret_number = request.cookies.get("secret_number")

    response = make_response(render_template("index.html"))
    if not secret_number:
        new_number = random.randint(1, 10)
        response.set_cookie("secret_number", str(new_number))

    return response


@app.route("/", methods=["POST"])
def result():
    secret_number = int(request.cookies.get("secret_number"))
    try:
        guess = int(request.form.get("guess"))
    except(ValueError):
        message = "not really a number"
        return render_template("oops.html", message=message)

    if secret_number == guess:
        new_number = random.randint(1, 10)
        response = make_response(render_template("success.html"))
        response.set_cookie("secret_number", str(new_number))
        return response
    elif secret_number > guess:
        message = "too small"
        return render_template("oops.html", message=message)
    elif secret_number < guess:
        message = "too big"
        return render_template("oops.html", message=message)


if __name__ == '__main__':
    app.run(debug=True)
