import urllib3
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi

class Translator():
    def __init__(self) -> None:
        self.transcripts = None

    def Translate(self, newLang: str) -> str:
        transcript = self.transcripts.find_transcript(["en"])
        transcript = transcript.translate(newLang).fetch()

        translation = ""
        for dic in transcript:
            translation += dic["text"]

        return translation
    
    def GetVideoID(self, url: str) -> str:
        url = url.split("v=")
        return url[-1]

    def GetTranscript(self, url: str):
        #the video id is the unique string after v= in the url
        #so split the url by the v= and return the unique string after which will the video id
        vidID = self.GetVideoID(url)
        self.transcripts = YouTubeTranscriptApi.list_transcripts(vidID)

class WebScraper():
    def __init__(self) -> None:
        self.http = urllib3.PoolManager()
        
        self.page = None

    def ScrapePage(self, url: str):
        responce = self.http.request("GET", url)
        self.page = BeautifulSoup(responce.data, "html.parser")

    def GetTitle(self) -> str:
        return self.page.title.text