from backend import store_items, show_items

def main():
    while True:
        print("A - add item, C - check item expiry, X - exit")
        user_options = input("Enter a command: ").strip()
        
        match user_options:
            case "A":
                user_item = input("Enter Item Name: ")
                item_date = input("Enter Items Expiration Date:")
                store_items(user_item,item_date)
                print("Item Stored")
            
            case "C":
                print(show_items())
                
            case "X":
                print("Closing Software")
                break
        

if __name__ == "__main__":
    main()