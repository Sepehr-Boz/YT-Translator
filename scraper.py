import urllib3
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi

class Translator():
    def __init__(self) -> None:
        self.transcripts = None

    def printAll(self):
        transcript = self.transcripts.find_transcript(["en"])
        print(transcript.fetch())

        transcript = transcript.translate("fa")
        print(transcript.fetch())

    def GetTranscript(self, url: str):
        #the video id is the unique string after v= in the url
        #so split the url by the v= and return the unique string after which will the video id
        def GetVideoID(url: str) -> str:
            url = url.split("v=")
            return url[-1]

        vidID = GetVideoID(url)
        self.transcripts = YouTubeTranscriptApi.list_transcripts(vidID)

        self.printAll()

class WebScraper():
    def __init__(self, translator: Translator) -> None:
        self.http = urllib3.PoolManager()
        self.translator = translator

    def ScrapePage(self, url: str):
        responce = self.http.request("GET", url)
        page = BeautifulSoup(responce.data, "html.parser")

        print(page.head.text)
        transcript = self.translator.GetTranscript(url)