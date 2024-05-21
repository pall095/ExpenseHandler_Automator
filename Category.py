class Category :
    
    categoriesList = [] 
    
    #ReadType:
    #    0 = from file.
    
    def readF( self , path ) :
        
        file = open( path , "r" )
        
        for line in file :
            
            line = line.split( "," )
            print( line )
    
    def __init__( self, path , readType = 0 ) :
        
        if readType == 0 :           
            self.readFromFile( path )
        
        
        