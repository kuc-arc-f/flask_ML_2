# -*- coding: utf-8 -*-
# predict


import numpy as np
import numpy.random as random
from pandas import Series, DataFrame
import pandas as pd

# 可視化モジュール
#import matplotlib.pyplot as plt
#import matplotlib as mpl
#import seaborn as sns
# 機械学習モジュール
import sklearn
import pickle

#
#class ReqParam:
#    def __init__(self, ):
#        return 0
#
class PredPrice:
    def __init__(self):
        self.params = {}
    #
    def load_model(self):
        filename = 'flaskr/files/model.pkl'
        model = pickle.load(open(filename, 'rb'))
        return model
    #
    def load_data(self, params):
        dat = {  'no':  [1 ]
        ,'siki_price': [params["siki_price"] ]
        ,'rei_price':  [params["rei_price"]  ]
        ,'menseki'  :  [params["menseki"] ]
        ,'nensu'    :  [params["nensu"] ]
        ,'toho'     :  [params["toho"] ]
        }
        df = DataFrame(dat  )
        df = df.assign(siki_price=pd.to_numeric( df.siki_price ))
        df = df.assign(rei_price =pd.to_numeric( df.rei_price ))
        df = df.assign(menseki =pd.to_numeric( df.menseki ))
        df = df.assign(nensu   =pd.to_numeric( df.nensu ))
        df = df.assign(toho    =pd.to_numeric( df.toho ))
        #print(df.info() )
        return df
