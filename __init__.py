# Hello world
# This file is the primary file containing all the StockMagic operations
# Per usual this file will have comments to help any given user understand

# This program uses these packages so it is recommended that you have them installed
import os
from pathlib import Path
import hyperlink as hy
import tkinter as TK
import requests
import matplotlib.pyplot as plt
from datetime import datetime as dt
import webbrowser as wb
import pandas as pd


# This is the primary class for StockMagic

class data_inputs:
    # This function must be run to set up the StockMagic Directory
    # To run this function you will need to generate keys from ALPACA
    # !!! MUST RUN THIS FUNCTION TO INITIALIZE THE STOCKMAGIC PROCESS !!!

    """RUN THIS FUNCTION AS 'x = stockmagic.data_inputs(<ALPACA API KEY>, <ALPACA SECRET KEY>)'"""

    def __init__(self, keyy, skey):
        path = os.getcwd().replace(os.sep, "/")
        name = Path(__file__).name
        full = str(path) + "/" + str(name)
        indv = full.split("/")

        self.path = path
        self.name = name
        self.full = full
        self.indv = indv
        self.keyy = keyy
        self.skey = skey

        BASE_URL = "https://paper-api.alpaca.markets"
        BARS_URL = "https://data.alpaca.markets/v1/bars"
        ORDERS_URL = "{}/v2/orders".format(BASE_URL)
        ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
        HEADERS = {'APCA-API-KEY-ID': keyy, 'APCA-API-SECRET-KEY': skey}

        self.BASE_URL = BASE_URL
        self.BARS_URL = BARS_URL
        self.ORDERS_URL = ORDERS_URL
        self.ACCOUNT_URL = ACCOUNT_URL
        self.HEADERS = HEADERS
        # print("\nSuccessfully initialized StockMagic with ALPACA keys as follows: \n"
        # "API-KEY: " + self.keyy + "\n" +
        # "SEC-KEY: " + self.skey + "\n")

    # This is the primary streaming function.
    # It takes the length of the bars as well as the stock to collect data for
    # All symbols must be capitol
    """RUN THIS FUNCTION AS 'x.market_data(time=<insert valid time here>, symbol=<insert CQC symbol here>)'"""

    def market_data(self, *args, time, symbol):

        symbol = symbol.replace("$", "p")
        plt.style.use("dark_background")

        # keys and urls
        if time == "1Min":
            MIN_URL = "{}/1Min?symbols={}&limit=1000".format(self.BARS_URL, symbol)
            TIME = "1Min"
        elif time == "1Hour":
            MIN_URL = "{}/15Min?symbols={}&limit=1000".format(self.BARS_URL, symbol)
            TIME = "1Hour"
        elif time == "1Day":
            MIN_URL = "{}/5Min?symbols={}&limit=1000".format(self.BARS_URL, symbol)
            TIME = "1Day"
        else:
            raise Exception("Unaccepted value entered \n"
                            "Please choose one of the following: \n"
                            "\"1Min\"\n"
                            "\"1Hour\"\n"
                            "\"1Day\"")

        day = requests.get(MIN_URL, headers=self.HEADERS)
        dy = day.json()

        def write_file(path, symbol):
            name = path + "/" + symbol + ".csv"
            f = open(name, "w+")
            f.truncate()
            f.write("Date,Open,High,Low,Close,Volume,OpenInterest\n")
            for bar in dy[symbol]:
                t = dt.fromtimestamp(bar['t'])
                day = t.strftime("%Y-%m-%d")
                line = "{},{},{},{},{},{},{},\n".format(day, bar['o'], bar['h'], bar['l'], bar['c'], bar['v'], 0,
                                                        00)
                f.write(line)

        for symbol in dy:
            # open file
            base = self.path + "/STOCK DATA/"
            frame = "{}/".format(time)
            path = base + frame

            if symbol != "message":
                this = str(args)
                print(this + " | " + symbol)
                if os.path.exists(path):
                    write_file(path=path, symbol=symbol)

                else:
                    os.makedirs(path)
                    write_file(path=path, symbol=symbol)
            else:
                print(dy)
                print("^^^")
                raise Exception("Something went went wrong while communicating with ALPACA")
            # format data

    def from_list(self, column_name, directory, time):
        df = pd.read_csv(directory)
        stocks = df[column_name]
        thing = 0
        for symbol in stocks:
            symbol = symbol.replace("$", "p")
            thing = thing + 1
            DI = data_inputs(keyy=self.keyy, skey=self.skey)
            DI.market_data(thing, time=time, symbol=symbol)

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
