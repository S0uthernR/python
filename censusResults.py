import os

import census2010

baxter_pop = census2010.allData['AR']['Baxter']['pop']

print('The population of Baxter county Arkansas in 2010 was ' + str(baxter_pop))
