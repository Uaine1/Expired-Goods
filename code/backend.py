from datetime import date, datetime
import sqlite3

# Should be running in the background
def check_date():
    connection = sqlite3.connect("items.db")
    cursor = connection.cursor()
    
    cursor.execute("SELECT item_name, expiry_date from items")
    items = cursor.fetchall()
    
    current_date = date.today()
    db_items = []
    
    for item, expiry in items:
        expiry_date = datetime.strptime(expiry, "%Y-%m-%d").date()
        
        if current_date == expiry_date:
            db_items.append(f"{item} Food has expired today: {current_date}")
        
        elif current_date > expiry_date:
            db_items.append(f"{item} Food has expired on {expiry_date}")
        
        else:
            db_items.append(f"{item} is safe until {expiry_date}")
            
    connection.close()
        
    return "\n".join(db_items)
    
    
def store_items(item_name, expiry_date):
    try:
        expiry_date = datetime.strptime(expiry_date, "%d/%m/%y").date() #converts date strings to actual dates
    except ValueError:
        return "Invalid date format, use dd/mm/yy. "
    
    date_stored = date.today()
    
    connection = sqlite3.connect("items.db")
    cursor = connection.cursor()
    
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
    
    cursor.execute("SELECT item_name, date_stored, expiry_date FROM items")
    item_row = cursor.fetchall()
    
    connection.close()
    
    if not item_row:
        return "No items found"
    
    items_list = "Stored item:\n"
    
    for item_name, date_stored, expiry_date in item_row:
        items_list += f"{item_name}: Date Stored on {date_stored} - Expires on {expiry_date}\n"
        
    return items_list


def delete_item(item_name):
    connection = sqlite3.connect("items.db")
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM items WHERE item_name = ?", (item_name,))
    connection.commit()
    
    connection.close()
    
