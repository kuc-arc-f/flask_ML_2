# -*- coding: utf-8 -*-
# テスト4, 体重、身長の重回帰分析。
# 学習ロード　＞評価


import numpy as np
import numpy.random as random
from pandas import Series, DataFrame
import pandas as pd

import sklearn
import pickle

# test

dat = {  'no':  ["1"  ]
        ,'siki_price':['2' ]
        ,'rei_price':['1' ]
        ,'menseki'  :['20' ]
        ,'nensu'    :['5' ]
        ,'toho'     :['10' ]
        }

df = DataFrame(dat  )
print(df )
#print(df.info() )

params = {"a1" : 1, "a2" : 22}
print(params["a1"] )