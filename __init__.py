import os
from pathlib import Path
import hyperlink as hy
import tkinter as TK


class data_inputs:
    def __init__(self):
        path = os.getcwd().replace(os.sep, "/")
        name = Path(__file__).name
        full = str(path) + "/" + str(name)
        indv = full.split("/")

        self.path = path
        self.name = name
        self.full = full
        self.indv = indv


    def market_data(self):
        pass

    @staticmethod
    def help():
        url1 = hy.parse(u'http://www.google.com')
        ber1 = url1.replace(scheme=u'https', port=443)
        org1 = ber1.click(u'.').to_text()
        url2 = hy.parse(u'http://www.stackoverflow.com/')
        ber2 = url2.replace(scheme=u'https', port=443)
        org2 = ber2.click(u'.').to_text()

        print("Visit", org1, "for the docs \n")
        print("I will raise exceptions for most things that are obvious so you can understand my messy code.")
        print("Beleive it or not there is actually a dev who doesn't want you to spend 8hrs on stack overflow.")
        print("Just in case though", org2, ":)")

    @staticmethod
    def ahhhhhhhh():
        raise Exception("Here are some more errors because you seem to be having a lot of them :)")
