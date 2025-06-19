from datetime import date, datetime
import sqlite3

# Should be running in the background
def check_date(item_name, expiry_date):
    current_date = date.today()
    
    store_items(item_name, current_date, expiry_date)
    
    if current_date == expiry_date:
        return(f"{item_name} Food has expired today: {current_date}")
    
    elif current_date > expiry_date:
        return(f"{item_name} Food has expired on {expiry_date}")
    
    else:
        return(f"{item_name} is safe until {expiry_date}")
    
    
def store_items(item_name, expiry_date):
    try:
        expiry_date = datetime.strptime(expiry_date, "%d/%m/%y").date() #converts date strings to actual dates
    except ValueError:
        return "Invalid date format, use dd/mm/yy. "
    
    date_stored = date.today()
    
    connection = sqlite3.connect("items.db")
    cursor = connection.cursor()
    
    #storing_item = 
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS items(
        item_id INTEGER PRIMARY KEY,
        item_name TEXT,
        date_stored DATE,
        expiry_date DATE)""")
    
    cursor.execute("INSERT INTO items (item_name, date_stored, expiry_date) VALUES(?,?,?)", (item_name, date_stored, expiry_date))
    
    connection.commit()
    
    """cursor.execute("SELECT * FROM items")
    item_rows = cursor.fetchall()
    
    for row in item_rows:
        return(row)"""
        

def show_items():
    connection = sqlite3.connect("items.db")
    cursor = connection.cursor()
    
    cursor.execute("SELECT item_name, expiry_date FROM items")
    item_row = cursor.fetchall()
    
    connection.close()
    
    if not item_row:
        return "No items found"
    
    items_list = "Stored item:\n"
    
    for item_name, expiry_date in item_row:
        items_list += f"{item_name}: Expires on {expiry_date}\n"
        
    return items_list