from backend import store_items, show_items, check_date, delete_item

def main():
    running = True
    
    while running:
        print(f"{check_date()}\n") 
        print("Commands:")
        print("A - add item, C - check expired goods, S - show item inventory, D - delete an item, X - exit")
        user_options = input("Enter a command: ").strip().capitalize()
        
        
        match user_options:
            case "A":
                user_item = input("Enter the item name: ").strip().title()
                item_date = input("Enter Item's Expiration Date:")
                store_items(user_item,item_date)
                print("Item Stored\n")
            
            case "C":
                print(check_date())
                
            case "S":
                print(show_items())
                
            case "D":
                user_item = input("Enter the item name: ").strip().title()
                delete_item(user_item)
                print("Item Deleted\n")
                
            case "X":
                print("Closing Software")
                running = False
        

if __name__ == "__main__":
    main()