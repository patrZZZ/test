#Efficient Data and Financial Analytics with Python  Hilpisch Yves





np.where(df['col1-col2']>C, 1, 0)
np.random.standard_normal($size)

#numexpr
import numexpr as ne
ne.set_num_threads(4)
f = '3*log(a)+cos(a) ** 2'
%timeit r = ne.evaluate(f)

