from flask import Blueprint, render_template

authentication = Blueprint("authentication", __name__)

@authentication.route("/sign-in", methods = ["GET", "POST"])
def sign_in_page():
    return render_template("sign_in.html")

@authentication.route("/sign-up", methods = ["GET", "POST"])
def sign_up_page():
    return render_template("sign_up.html")

@authentication.route("/sign-out")
def sign_out_page():
    return "<h1>Sign Out</h1>"