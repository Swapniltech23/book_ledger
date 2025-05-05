import streamlit as st

# Initialize an empty library book issuing ledger (a dictionary where keys are member names)
if 'library_ledger_advanced' not in st.session_state:
    st.session_state.library_ledger_advanced = {}

# Function to add or update a library member's book issuing record
def add_member_issued_book(member_name, book_title, issue_date, due_date):
    # Create a dictionary for the book issued
    book_issued = {
        "book_title": book_title,
        "issue_date": issue_date,
        "due_date": due_date
    }

    # Add the book issued to the member's list of issued books
    if member_name not in st.session_state.library_ledger_advanced:
        st.session_state.library_ledger_advanced[member_name] = []

    st.session_state.library_ledger_advanced[member_name].append(book_issued)
    st.success(f"Book '{book_title}' issued to {member_name} on {issue_date}, due on {due_date}.")

# Streamlit UI for adding book issuing records
st.title("Library Book Issuing Ledger")

with st.form(key="book_issuing_form"):
    member_name = st.text_input("Enter the member's name")
    book_title = st.text_input("Enter the book title")
    issue_date = st.date_input("Enter the date of issue")
    due_date = st.date_input("Enter the due date for returning the book")

    submit_button = st.form_submit_button("Add Book Record")

    if submit_button:
        if member_name and book_title and issue_date and due_date:
            add_member_issued_book(member_name, book_title, str(issue_date), str(due_date))
        else:
            st.error("Please fill in all the fields.")

# Display the advanced library ledger
st.subheader("Advanced Library Book Issuing Ledger:")
for member, books in st.session_state.library_ledger_advanced.items():
    st.write(f"**Member:** {member}")
    for book in books:
        st.write(f"  - **Book Title:** {book['book_title']}, Issued On: {book['issue_date']}, Due On: {book['due_date']}")
