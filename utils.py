import pandas as pd
from Expense import Entry


def findMatch( descr , expense_database ) :
    
    for exp in expense_database :
        
        if descr in exp.descr :
            return [ exp.cat , exp.subcat , bool( exp.fixed ) ]
        
    return None
    
def createCatDatabase( path ) :
    
    file = open( path , "r" )
    database = { }
    
    for line in file :
        
        line_splitted = line.strip().split( "," )
        database.update( { line_splitted[ 0 ] : line_splitted[ 1 : ] } )

    return database


def createExpenseDatabase( data_frame ) :
    
    expenseDatabase = [ ]
    
    for row , content in data_frame.iterrows( ) :
        
        content = list( content )
        current_expense = Entry( content[ 0 ] ,  content[ 1]  , content[ 2 ] , content[ 3 ] , content[ 4 ] , content[ 5 ] )
        expenseDatabase.append( current_expense )
        
    return expenseDatabase
        

def matchDescr( descr , exp_database , session ) :
    
    for expense in exp_database :
        
        if descr in expense.descr :
            
            session.cat = expense.cat
            session.subcat = expense.subcat
            session.fixed = expense.fixed 
        
    