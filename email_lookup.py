#!/usr/bin/env python3
import csv
import sys
import os

def populate_dictionary(filename):
    """Populate a dictionary with name/email pairs for easy lookup."""
    email_dict = {}
    try:
        with open(filename) as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                # Ensure the row has enough data to avoid index errors
                if len(row) >= 2:
                    name = str(row[0].lower().strip())
                    email = row[1].strip()
                    email_dict[name] = email
        return email_dict
    except FileNotFoundError:
        return None

def find_email(argv):
    """Return an email address based on the username given."""
    try:
        # Combine arguments to form the full name (e.g., "John Doe")
        fullname = str(argv[1] + " " + argv[2])
        
        # Look for the csv file in the current directory
        file_path = 'user_emails.csv'
        
        email_dict = populate_dictionary(file_path)
        
        if email_dict is None:
            return f"Error: '{file_path}' file not found."

        # Search for the name in the dictionary
        result = email_dict.get(fullname.lower())
        if result:
            return f"Email for {fullname}: {result}"
        else:
            return f"No email address found for '{fullname}'"
            
    except IndexError:
        return "Error: Missing parameters.\nUsage: python3 email_lookup.py [Firstname] [Lastname]"

def main():
    print(find_email(sys.argv))

if __name__ == "__main__":
    main()