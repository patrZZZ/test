import pyqr
import pandas as pd
import numpy as np
import json
import itertools
import os
import datetime
import instrument_equity as it
import time
import matplotlib.pyplot as plt
def get_vdf_path(symbol, exchange, date):
    symbol = symbol.upper()
    exchange = exchange.upper()
    filename = ' '
    temp_date = str(date)[:4] + '/' + str(date)[4:6] + '/' + str(date)[6:];
    if exchange == 'XNAS':
        if int(str(date)[:4]) == 2018 and int(str(date)[4:]) > 322:
            vdf_dir = '/apps/vdf/v4/' + exchange + '/' + temp_date + "/"
            path = vdf_dir + symbol + '.zst'
        elif int(str(date)[:4]) == 2018 and int(str(date)[4:]) <= 322:
            vdf_dir = '/apps/vdf/' + exchange + '/' + temp_date + "/"
            path = vdf_dir + symbol# + '.zst'
        else:
            vdf_dir = '/apps/vdf/' + exchange + '/' + temp_date + "/"
            path = vdf_dir + symbol + '.zst'
    elif exchange == 'XASE':
        if int(str(date)[:4]) == 2018:
            vdf_dir = '/apps/vdf/XASE_L1/' + temp_date + "/"
            path = vdf_dir + symbol
        else:
            vdf_dir = '/apps/vdf/XASE_L1/' + temp_date + "/"
            path = vdf_dir + symbol + '.zst'
            
    elif exchange == 'TAQ':
        if int(str(date)[:4]) == 2018:
            vdf_dir = '/apps/vdf/TAQtrades/' + temp_date + "/"
            path = vdf_dir + symbol
        else:
            vdf_dir = '/apps/vdf/TAQtrades/' + temp_date + "/"
            path = vdf_dir + symbol + '.zst'
    elif exchange == 'EDGA':
        vdf_dir = '/apps/vdf/EDGA/' + temp_date + "/"
        path = vdf_dir + symbol + '.zst'
    return path

class md():
    def __init__(self, symbol, exchange, date):#, implied = True):  #year/month/date in date format, symbol = display symbol
        '''
        import instrument as it
        symbol = symbol.upper()
        exchange = exchange.upper()
        #
        #self.implied = implied
        filename = ' '
        temp_date = str(date)[:4] + '/' + str(date)[4:6] + '/' + str(date)[6:];
        if int(str(date)[:4]) == 2018 and int(str(date)[4:]) > 322:
            vdf_dir = '/apps/vdf/v4/' + exchange + '/' + temp_date + "/"
            self.path = vdf_dir + symbol + '.zst'
        elif int(str(date)[:4]) == 2018 and int(str(date)[4:]) <= 322:
            vdf_dir = '/apps/vdf/' + exchange + '/' + temp_date + "/"
            self.path = vdf_dir + symbol# + '.zst'
        else:
            vdf_dir = '/apps/vdf/' + exchange + '/' + temp_date + "/"
            self.path = vdf_dir + symbol + '.zst'
        '''
        self.path = it.get_vdf_path(symbol, exchange, date)
        self.symbol = symbol
        self.exchange = exchange
        self.date = date
        self.pre_open = pd.Timestamp(str(date), tz='US/Eastern') + pd.Timedelta('3 hours 30 min')
        self.mkt_open = pd.Timestamp(str(date), tz='US/Eastern') + pd.Timedelta('9 hours 29 min 58 sec')
        self.mkt_open_r = pd.Timestamp(str(date), tz='US/Eastern') + pd.Timedelta('9 hours 30 min')        
        self.mkt_close = pd.Timestamp(str(date), tz='US/Eastern') + pd.Timedelta('10 hours 59 min 58 sec')
        #result, self.tickSize = it.get_tickSize(symbol, date, exchange)
        #result, self.feedMultiplier = it.get_feedMultiplier(symbol, date, exchange)
        #self.feedMultiplier = 1.0
        self.book = []
        #we want to store simple book, and trade
        #self.get_fast_book(60) #1 min book
        #self.get_price()
        #self.result = result
        #print self.path
        
    def get_df_clean(self):
        self.df = pyqr.read_vdf(self.path, preserve_na=True, 
                           filter = ['book.BID.price.0', 'book.BID.qty.0', 'book.BID.ocount.0', 'book.ASK.price.0', 'book.ASK.qty.0', 'book.ASK.ocount.0', 'book.event', "clock.timestamp", "trades.event", 'trades.price', 'trades.qty', 'trades.dir'])        
        book_idx = self.df["book.event"]==1
        trade_idx = self.df["trades.event"]==1
        #
        self.df = self.df[(book_idx) | (trade_idx)].reset_index(drop=True)
        self.df = self.df.dropna()
        book_idx = self.df["book.event"]==1
        trade_idx = self.df["trades.event"]==1        
        self.df["clock.timestamp"] = pd.DatetimeIndex(self.df["clock.timestamp"]).tz_localize("GMT").tz_convert("US/Eastern")
        self.df.index = self.df['clock.timestamp']
        #print self.df 
        #self.df["wmp"] = ((self.df["book.BID.price.0"]*self.df["book.ASK.qty.0"])+(self.df["book.ASK.price.0"]*self.df["book.BID.qty.0"])) / (self.df["book.BID.qty.0"] + self.df["book.ASK.qty.0"])
        #self.df["sp"] = np.round_((self.df["book.ASK.price.0"] - self.df["book.BID.price.0"]) /self.tickSize * self.feedMultiplier)
        self.df["trades.qty"][self.df["trades.event"]==0] = 0 #make trades qty = 0 
        print "clean generated"
        
    def get_df_trade(self):
        self.trades = pyqr.read_vdf(self.path, preserve_na=True, 
                           filter = ['book.BID.price.0', 'book.BID.qty.0', 'book.BID.ocount.0', 'book.ASK.price.0', 'book.ASK.qty.0', 'book.ASK.ocount.0', "clock.timestamp", "trades.event", 'trades.price', 'trades.qty', 'trades.dir']) #, "trades.volume", "trades.msgnum", "trades.tickdir", "trades.matchnum", "ready.pktnum", "book.update_time", "book.exch_update_time", "book.exch_send_time", "book.exch_transact_time", "trades.exch_send_time", "trades.exch_transact_time"])
        self.trades = self.trades[self.trades['trades.event'] == 1]
        self.trades.index = self.trades["clock.timestamp"]
        self.trades.index = self.trades.index.tz_localize("GMT").tz_convert("US/Eastern")
        self.trades["clock.timestamp"] = self.trades.index
        pre_open_idx = self.trades.index[self.trades["clock.timestamp"] > self.pre_open][0]
        mkt_open_idx = self.trades.index[self.trades["clock.timestamp"] > self.mkt_close][0]
        self.trades = self.trades[pre_open_idx : mkt_open_idx]
        print 'trades generated'
    
    def get_rolling_trades_qty(self, timeSpan1 = 10000000, timeSpan2 = 30000000):
        df = self.trades
        temp_change = df
        rolling_sum = []
        for index, row in temp_change.iterrows():
            temp_idx_start = df.index[df["clock.timestamp"] > row['clock.timestamp'] - datetime.timedelta(0, 0, timeSpan1)][0]
            sub_df = df[temp_idx_start:index]
            qty_sum = sub_df['trades.qty'].sum()
            rolling_sum.append(qty_sum)
        df_rolling = pd.DataFrame(np.array(rolling_sum).T, columns = ['rolling_qty'])
        self.trades = self.trades.drop('clock.timestamp', axis = 1)
        self.trades = self.trades.reset_index()
        self.trades['trades.rolling_qty'] = df_rolling['rolling_qty']
        self.trades.index = self.trades['clock.timestamp']

    def get_pre_open_vol_prc(self):
        pre_open_path = it.get_vdf_path(self.symbol, 'TAQ', self.date)
        df = pyqr.read_vdf(pre_open_path, preserve_na=True, 
                       filter = ["clock.timestamp", "trades.event", 'trades.price', 'trades.qty'])
        pre_open_idx = df.index[df["clock.timestamp"] > self.pre_open][0]
        mkt_open_idx = df.index[df["clock.timestamp"] > self.mkt_open][0]
        df = df[pre_open_idx : mkt_open_idx]
        df.index = df["clock.timestamp"]
        df.index = df.index.tz_localize("GMT").tz_convert("US/Eastern")
        #self.test = df[df['trades.event'] ==1]
        try:
            self.pre_open_vol = df.ix[df['trades.event'] > 0, 'trades.qty'].sum()
            self.pre_open_prc = df[df['trades.event'] > 0]['trades.price'].iloc[-1]
        except:
            self.pre_open_vol = 0
            self.pre_open_prc = 0
        #print self.pre_open_prc
    def prod_prep(self):
        self.get_df_trade()
        pre_open_idx = self.trades.index[self.trades["clock.timestamp"] > self.mkt_open_r][0]
        mkt_open_idx = self.trades.index[self.trades["clock.timestamp"] > self.mkt_close][0]
        self.trades = self.trades[pre_open_idx : mkt_open_idx]
        self.get_rolling_trades_qty()
        print 'prod_prep finished'

#path = get_vdf_path('FB', 'TAQ', 20180507)
#df = pyqr.read_vdf(path, preserve_na=True)
fig, axes = plt.subplots(nrows=2, ncols=2)

name = 'SORL'
temp = md(name, 'TAQ', 20180515)
temp.get_df_trade()
temp.trades = temp.trades.groupby(level = 0).first()
temp.trades['trades.price'].resample('1S').bfill().plot(ax=axes[0,0])
temp1 = md('IMTE', 'TAQ', 20180515)
temp1.get_df_trade()
temp1.trades = temp1.trades.groupby(level = 0).first()
temp1.trades['trades.price'].resample('1S').bfill().plot(ax=axes[1,0])
plt.show()
df = pd.read_pickle('./preMktvol.p')
print df[name]['20180510':'20180515']
print temp.trades
#TAQnbbo
