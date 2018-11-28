import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''Datetime and Filter'''

'''Dataframe'''
df.where(df['a'] !=0, np.nan)
df.drop(colume_name, axis = 1) #1 for colume
df.dropna(axis = 0)
df.fillna(method = 'ffill')
df = pd.concat([df1, df2])
corr = df['A'].corr(df['B'])


df = df.reset_index().set_index(['clock.timestamp'])

date_list = [i for i in date_list if i > div_date[idx - 1]]

def rename_symbol(name):
    symbol_list = ['STERLING', 'EURIBOR', 'BOBL', 'BUND', 'ST EUROBTP', 'EURO-BTP', 'FOAT', 'SCHATZ', 'UL T-BONDS', 'ULT TNOTE',
                   'T-BONDS', '10Y T-NOTE', '5Y T-NOTE', '2Y T-NOTE', '30D INT RT', 'CRUDE', 'IMM 3M EUR', 'BRENT', 'LONG GILT']
    symbol_dict = dict(zip(symbol_list, value_list))
    temp_list = filter(lambda x: x in name, symbol_list)
     
def get_business_day(date, delta = 1): #input/output format is INTEGER of "%Y%m%d"   "delta = 1 next business day" it skips holiday!
        #delta must be -1 or 1 (or else doesnt work well)
        date = str(date)
        date = dt.datetime.strptime(date, "%Y%m%d").date() + dt.timedelta(delta)
        while ((date.weekday() == 6) or (date.weekday() ==5)):
                if delta <0:
                        date = date + dt.timedelta(-1)
                elif delta >0:
                        date = date + dt.timedelta(1)
        date = dt.datetime.strftime(date, "%Y%m%d")
        date = int(date)
        return date
    
'''Main Function'''
if __name__ == "__main__":
        if (len(sys.argv)==4):
                date = "unknown"
                filename_abn = sys.argv[1]
        elif (len(sys.argv)==1):
                date = int(datetime.datetime.today().strftime("%Y%m%d"))
                filename_abn = "./{}_abn.txt".format(date)
                
'''Class and Lambda'''  
class statement():
    def __init__(self, a, b):
        df_abn['pos'] = df_abn.apply(lambda x: int(x['pos']), axis = 1)
        df_abn = pd.DataFrame(np.array(statement_list).T, columns = ['inst', 'pos'])
        pos_df['inst'] = pos_df.apply(lambda x: x['inst'][0:4] if x['inst'][0:4] in self.eurex_list else x['inst'], axis = 1)
        df_abn = self.df_abn.merge(pos_df, on = 'inst')
    
    def resample_book(sample_time, start_time, end_time):
                if "book" in dir(self):
                        self.book = self.book.between_time(start_time, end_time, include_end = True)
                        self.book = self.book.resample(sample_time, how = 'last', fill_method = 'ffill') #for second x, [x, x+1], take the last    

df_candle = self.md.trades['trades.price'].resample('5Min').ohlc()


                        
'''Itertools.izip'''      
for i,j,k in itertools.izip(name_list_n, name_list_o1, name_list_o2):
    df_delta_ZF[i] = df_book_ZF[j].pct_change(1)
    df_delta_ZF[i].where(df_delta_ZF[k] != 0, np.nan)                
'''sklearn'''
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
def linear_reg(df):
    msk = np.random.rand(len(df)) < 0.8
    train = df[msk]
    test = df[~msk]
    regr =  linear_model.LinearRegression()
    regr.fit(train.iloc[:, 0:-1].values, train['Y'].values)
    y_pred = regr.predict(test.iloc[:,0:-1].values)
    print("Coefficients: \\n")
    print regr.coef_
    # The mean squared error
    print("Mean squared error: %.2f"
          % mean_squared_error(test['Y'].values, y_pred))
    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % r2_score(test['Y'].values, y_pred))

'''plot'''    
df_delta_ZF.plot(kind = 'scatter', x = 'delta_bid_edge', y = 'Y')
plt.show()

df3.hist(column = ['delta_bid_qty'], bins = 100)

'''string split'''
#s = string with space.
for st in s.split():
    name_list.append(st.split(':')[0])
for date, row in df_pos.iterrows():
    
    
    
    
from sklearn import linear_model
import scipy.odr as odr
linear = odr.Model(f_TLS)
mydata = odr.Data(self.df_model[GE_name], self.df_model['ZF'])
myodr = odr.ODR(mydata, linear, beta0 = [4., 0.])
myoutput = myodr.run()
tls_beta = myodr.output.beta[0]
corr = self.df_model['ZF'].corr(self.df_model[GE_name])

