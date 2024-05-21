import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import time 
import os

# Selfmade depenendices
import utils as utl

    

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
    else:
        print( "No match!")

# Data management
categories_file = r"UsciteCTRL_19Mag2024.csv"
cat_database = utl.createCatDatabase( categories_file )

# Web App Management
st.title( "Expense Handler Portal")
st.markdown( "Questo è un messaggio di prova" )

# Connetting and getting existinga data as a pandas data frame
conn = st.connection( "gsheets" , type = GSheetsConnection )
existing_data = conn.read( worksheet = "Uscite"  , usecols = list( range( 6 ) ) , ttl = 5)
existing_data = existing_data.dropna( how = "all" )
expense_database = utl.createExpenseDatabase( existing_data )
#st.dataframe( existing_data )

# Page creation
expense_date = st.date_input( "Expense date")
expense_description = st.text_input( label = "Expense description" , key = "descr" )
expense_category = st.selectbox( "Categories" , cat_database.keys() , key = "cat" )
expense_subcategory = st.selectbox( "Subcategory" ,  options = cat_database[ expense_category ]  , key = "subcat")
expense_fixed = st.checkbox( label = "Fixed?" , key = "Fixed" )




add_button = st.button( label = "Add expense"  )
match_button = st.button( label = "Match expense" , on_click = findMatch_onClick , args = [ st.session_state.descr , expense_database ] ) 