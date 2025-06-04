from datetime import date, time, datetime

def main():
    food_expiry_date = "04/06/2025"
    expiry_date = datetime.strptime(food_expiry_date, "%d/%m/%Y").date() #converts date strings to actual dates
    current_date = date.today()
    
    if current_date == expiry_date:
        print(f"XXXX Food has expired today: {current_date}")

if __name__ == "__main__":
    main()