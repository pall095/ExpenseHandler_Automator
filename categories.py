
    
def createCatDatabase( path ) :
    
    file = open( path , "r" )
    self.full_database = { }
    
    for line in file :
        
        line_splitted = line.strip().split( "," )
        self.full_database.update( { line_splitted[ 0 ] : line_splitted[ 1 : ] } )
