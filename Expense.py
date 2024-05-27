class Entry :
    
    def __init__( self , date , value , descr , cat , subcat , fixed ) :
        
        self.date = date 
        self.value = value 
        self.descr =str( descr )
        self.cat = cat
        self.subcat = subcat
        if fixed == True : self.fixed = "TRUE"
        else : self.fixed = "FALSE"