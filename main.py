from flask import Flask, render_template, request
from scraper import Translator, WebScraper

#init the app
app = Flask(__name__)

translator = Translator()
scraper = WebScraper(translator)

#return the index page at the start
@app.route("/")
def main():
    return render_template("index.html")

#when the details have been entered then run this method
@app.route("/index", methods=["GET", "POST"])
def getURL():
    if request.method == "POST":
        print(request.form["url"])
        scraper.ScrapePage(request.form["url"])

        return render_template("video.html")