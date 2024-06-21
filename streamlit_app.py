import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import time 
import datetime

# Selfmade depenendices
import utils as utl

# Button behavior
def deleteLast_onClick( existing_data ):
    existing_data.drop( existing_data.tail( 1 ).index , inplace = True )
    conn.update( worksheet = "Uscite" , data = existing_data )

def updateOutput_onClick( conn , new_expense_list , existing_data ) :
    
    new_expense = utl.createNewExpense( new_expense_list )
    
    if type( new_expense ) is not int :
    
        updated_frame = pd.concat( [existing_data , new_expense ] , ignore_index = True )
        conn.update( worksheet = "Uscite" , data = updated_frame )
        st.session_state[ "terminal" ] = "Expense logged!"
    
    else: 
        
        if new_expense == 1 :
            st.session_state[ "terminal" ] = "Expense refused, description!"
        
        elif new_expense == 2 :
            st.session_state[ "terminal" ] = "Expense refused, amount must be > 0!"
    

def findMatch_onClick( input_descr , expense_database  ) :
  
    match = utl.findMatch( input_descr , expense_database ) 
    print( f"Input Description: { input_descr} ")

    if match != None :
        print( f"Category: {match[0]}" )
        print( f"Category: {match[1]}" )
        print( f"Fixed: {match[2]}" )
        st.session_state[ 'cat' ] = match[ 0 ]
        time.sleep( 0.1 )
        st.session_state[ 'subcat' ] = match[ 1 ]
        time.sleep( 0.1 )
        st.session_state[ 'Fixed' ] = match[ 2 ]
        st.session_state[ "terminal" ] = "Match found!"
    else:
        st.session_state[ "terminal" ] = "No match"

# Data management
categories_file = r"UsciteCTRL_19Mag2024.csv"
cat_database = utl.createCatDatabase( categories_file )

# Web App Management
st.title( "Expense Handler Portal")
st.markdown( "Applicazione creata da Matteo Pallomo" )

# Connetting and getting existinga data as a pandas data frame
conn = st.connection( "gsheets" , type = GSheetsConnection )
existing_data = conn.read( worksheet = "Uscite"  , usecols = list( range( 8 ) ) , ttl = 5)
existing_data = existing_data.dropna( how = "all" )
expense_database = utl.createExpenseDatabase( existing_data )
#st.dataframe( existing_data )

# Page creation
expense_date = st.date_input( "Expense date")
expense_amount = st.number_input( "Expense amount" )
expense_description = st.text_input( label = "Expense description" , key = "descr" )

with st.container( ) :
    col1 , col2 , col3 = st.columns( 3 )
    with col1 :
        expense_category = st.selectbox( "Categories" , cat_database.keys() , key = "cat" )
    with col2 : 
        expense_subcategory = st.selectbox( "Subcategory" ,  options = cat_database[ expense_category ]  , key = "subcat")

    with col3 :
        expense_fixed = st.checkbox( label = "Fixed?" , key = "Fixed" )

# Processing
new_expense_list = [ expense_date , expense_amount , expense_description , expense_category , expense_subcategory , expense_fixed ]

with st.container( ):
    
    col1 , col2 , col3 = st.columns( 3 )
    with col1:
        add_button = st.button( label = "Add expense" , on_click = updateOutput_onClick , args = [ conn , new_expense_list , existing_data ] , use_container_width = True )
    with col2:
        match_button = st.button( label = "Match expense" , on_click = findMatch_onClick , args = [ st.session_state.descr , expense_database ] , use_container_width = True )
    with col3 :
        delete_last = st.button( label = "Delete Last" , on_click = deleteLast_onClick , args = [ existing_data ] , use_container_width = True )


terminal = st.text_area( "Terminal" , key = "terminal" )
laste_expense = st.table( existing_data.iloc[ -1 ] )    



