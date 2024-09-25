# Code Hub

'''
1. Install Graphviz

Windows:
https://graphviz.org/download/
-> graphviz-12.1.1 (64-bit) EXE installer [sha256]
1) Open the Start Menu, search for "Environment Variables," and select "Edit the system environment variables."
2) In the System Properties window, click on the Environment Variables button.
3) Under System variables, find the Path variable and click Edit.
4) Click New and add the path where Graphviz is installed, typically something like C:\Program Files\Graphviz\bin\.
5) Click OK to close all windows, and then restart your terminal or IDE.

macOS: 
brew install graphviz.

Linux: 
sudo apt-get install graphviz.

2. Install packages
pip install -r requirements.txt

[!] png is already generated but this is the tool I'm using for creating visuals

'''
import database_schema as schema
import erd_creation as erd

def main():
    # Task 1: Create the database schema
    print("Creating database schema...")
    schema.create_db()
    print("Database schema created successfully.")

    # Task 2: Create the ERD
    print("Generating ERD...")
    erd.create_erd()
    print("ERD generated successfully. Check bookhaven_erd.png.")

if __name__ == "__main__":
    main()
