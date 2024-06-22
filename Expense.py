class Entry :
    
    def __init__( self , date , value , descr , cat , subcat , fixed ) :
        
        self.date = date 
        self.value = value 
        self.descr =str( descr )
        self.cat = cat
        self.subcat = subcat
        if fixed == "TRUE" : self.fixed = 1
        else : self.fixed = 0