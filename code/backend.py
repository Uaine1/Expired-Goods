from datetime import date, datetime

def check_date(item_name, expiry_date):
    #userinput = userinput.strip()

    try:
        expiry_date = datetime.strptime(expiry_date, "%d/%m/%y").date() #converts date strings to actual dates
    except ValueError:
        return "Invalid date format, use dd/mm/yy. "
    
    current_date = date.today()
    
    if current_date == expiry_date:
        return(f"{item_name} Food has expired today: {current_date}")
    
    elif current_date > expiry_date:
        return(f"{item_name} Food has expired on {expiry_date}")
    
    else:
        return(f"{item_name} is safe until {expiry_date}")