from backend import check_date

def main():
    user_item = input("Enter Item Name: ")
    item_date = input("Enter Items Expiration Date:")
    print(check_date(user_item,item_date))
        

if __name__ == "__main__":
    main()