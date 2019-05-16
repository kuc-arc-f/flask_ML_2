# 日本語

# coding: utf-8

from flask import Flask
from flask_cors import CORS
import numpy as np

class VectBase:
    #
    def __init__(self):
        from flaskr.include.pred_price import  PredPrice
        self.pred=PredPrice()
        self.model = self.pred.load_model()
        print("#end-pred-Price ")
    #
    def predict(self, params ):
        df = self.pred.load_data( params )
        price = self.model.predict(df )
        price_int = np.array( price , np.int32)
        #print(text )
        return price_int
        
### main()
app = Flask(__name__)
CORS(app)
app.config.from_object('flaskr.config')
vect=VectBase()

import flaskr.views