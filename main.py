from flask import Flask, render_template, request, jsonify
from scraper import Translator, WebScraper

#init the app
app = Flask(__name__)

translator = Translator()
scraper = WebScraper()


@app.route("/languages", methods=["GET", "POST"])
def GetLanguages():
    languages = translator.GetLanguages()
    return jsonify(languages)

@app.route("/translate/<lang>", methods=["GET", "POST"])
def GetTranslation(lang):
    print(lang)

    translation = translator.Translate(lang)
    message = {'lang':translation}
    return jsonify(message)


#return the index page at the start
@app.route("/")
def Main():
    return render_template("index.html")

#when the details have been entered then run this method
@app.route("/index", methods=["GET", "POST"])
def GetURL():
    if request.method == "POST":
        scraper.ScrapePage(request.form["url"])
        title = scraper.GetTitle()
        
        translator.GetTranscript(request.form["url"])
        text = translator.Translate("en")

        vidURL = "https://www.youtube.com/embed/" + translator.GetVideoID(request.form["url"])

        return render_template("video.html", title=title, videoURL=vidURL, text=text)