from backend import store_items, show_items, check_date, delete_item
import streamlit as st
import pandas as pd

def main():
    st.title("Expired :green[Goods]")
    st.header("Enter Items", divider=True)

    # Input fields to add a new item
    with st.form("item_form", clear_on_submit=True):
        item_name = st.text_input("Item Name")
        expiry_date = st.date_input("Expiry Date")
        submitted = st.form_submit_button("Store Item")

        if submitted:
            if item_name:
                store_items(item_name, expiry_date.strftime("%d/%m/%y"))
                st.success(f"Stored: {item_name}")
            else:
                st.warning("Please enter an item name.")

    # Show all stored items
    st.header("Stored Items", divider=True)
    items = show_items()  # assumed to return a list of dicts

    if not items:
        st.info("No items found.")
    else:
        df = pd.DataFrame(items)
        st.dataframe(df, use_container_width=True)

    # Optional: Check for expired items
    st.header("Check for Expired Items", divider=True)
    if st.button("Check Expired"):
        expired = check_date()
        if not expired:
            st.success("No expired items.")
        else:
            df_expired = pd.DataFrame(expired)
            st.error("Expired items:")
            st.dataframe(df_expired, use_container_width=True)

    # Optional: Delete item by name
    st.header("Delete an Item", divider=True)
    item_to_delete = st.text_input("Enter item name to delete")
    if st.button("Delete Item"):
        result = delete_item(item_to_delete)  # assumed to return success/failure
        if result:
            st.success(f"Deleted: {item_to_delete}")
        else:
            st.warning("Item not found or could not be deleted.")


if __name__ == "__main__":
    main()
