from flask import Flask, render_template
from research import top_beer, top_wine, top_spirit, top_alcohol, read_csv

app = Flask(__name__)

@app.route("/")
def create_chart():
    top_countries = {
        "Cerveja": top_beer(read_csv()),
        "Destilados": top_spirit(read_csv()),
        "Vinho": top_wine(read_csv()),
        "Total de alcool": top_alcohol(read_csv()),
    }
    title = ["id","País", "Cerveja", "Destilados", "Vinho", "Total de alcool"]
    return render_template("index.html", top_countries=top_countries, title=title, count=0)
