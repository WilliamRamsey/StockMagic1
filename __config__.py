from pathlib import Path
import os
import tkinter as tk
import requests as rq

path = os.getcwd().replace(os.sep, "/")
name = Path(__file__).name
full = str(path) + "/" + str(name)
absp = full.split("/")

<<<<<<< HEAD
=======
stockmagic_path = path + "/" + "StockMagic"
os.makedirs(stockmagic_path)
>>>>>>> Initial commit



