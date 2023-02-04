

def SET_BIT( reg, bitnum ) :
    
    """ Setting a specific bit of an int number """
    
    reg     = int(reg)
    
    bitnum  = int(bitnum)
    
    (reg) |= (1 << (bitnum))
    
    return reg
    
    
def CLR_BIT( reg, bitnum ) :
    
    """ Clearing a specific bit of an int number """
    
    reg     = int(reg)
    
    bitnum  = int(bitnum)
    
    (reg) &= ~(1 << (bitnum))
    
    return reg
    
     
def TOGGLE_BIT( reg, bitnum ) :
    
    """ Setting a specific bit of an int number """
    
    reg     = int(reg)
    
    bitnum  = int(bitnum)
    
    (reg) ^= (1 << (bitnum))
    
    return reg
    
      
def GET_BIT( reg, bitnum ) :
    
    """ Setting a specific bit of an int number """
    
    reg     = int(reg)
    
    bitnum  = int(bitnum)
    
    (((reg)>>(bitnum)) & 1)
    
    return reg
   
   
   
   