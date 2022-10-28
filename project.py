import numpy as np
from icecream import ic
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 

# declare matrix with np
gfg = np.array([[1,'fatih'],[2,'sarikaya'], [3], [4, 5,[6,7]]]) #,dtype=object,)    
  
# using array.flatten() method
flat_gfg = gfg.flatten()

ic(flat_gfg)

flat_gfg[0].reverse()
flat_gfg[1].reverse()
flat_gfg[3][2].reverse()
flat_gfg[3].reverse()

#ic("reversed_list:",flat_gfg)

final = flat_gfg[::-1]

ic(final)
