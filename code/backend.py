from datetime import date, datetime
import sqlite3

# Should be running in the background
def check_date():
    connection = sqlite3.connect("items.db")
    cursor = connection.cursor()

    cursor.execute("SELECT item_name, expiry_date FROM items")
    items = cursor.fetchall()

    current_date = date.today()
    expired_items = []

    for item, expiry in items:
        expiry_date = datetime.strptime(expiry, "%Y-%m-%d").date()

        if current_date >= expiry_date:
            status = "Expired" if current_date > expiry_date else "Expires Today"
            expired_items.append({
                "Item Name": item,
                "Expiry Date": expiry_date.isoformat(),
                "Status": status
            })

    connection.close()
    return expired_items
    
    
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
    rows = cursor.fetchall()
    connection.close()

    # Ensure we return a list of dicts
    return [
        {"Item Name": row[0], "Date Stored": row[1], "Expiry Date": row[2]}
        for row in rows
    ]


def delete_item(item_name):
    connection = sqlite3.connect("items.db")
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM items WHERE item_name = ?", (item_name,))
    connection.commit()

    rows_deleted = cursor.rowcount  
    connection.close()

    return rows_deleted > 0  

