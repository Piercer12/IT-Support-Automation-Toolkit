#!/usr/bin/env python3
import re
import csv
import sys
import os

def contains_domain(address, domain):
    """Returns True if the email address contains the given domain."""
    domain_pattern = r'[\w\.-]+@' + re.escape(domain) + '$'
    if re.match(domain_pattern, address):
        return True
    return False

def replace_domain(address, old_domain, new_domain):
    """Replaces the old domain with the new domain in the address."""
    old_domain_pattern = r'@' + re.escape(old_domain) + '$'
    address = re.sub(old_domain_pattern, '@' + new_domain, address)
    return address

def main():
    # 1. Setup Input/Output Paths (Works on ANY computer)
    # Using 'sys.argv' allows the user to specify files via command line
    try:
        csv_file_location = sys.argv[1]
    except IndexError:
        print("Error: Please provide a CSV file path.")
        print("Usage: python3 domain_migrator.py <input_file.csv>")
        sys.exit(1)

    # Output file will be created in the same folder as the input
    report_file = os.path.splitext(csv_file_location)[0] + '_updated.csv'
    
    old_domain = 'abc.edu'
    new_domain = 'xyz.edu'

    user_data_list = []

    # 2. Process the CSV (Read & Update in one go)
    try:
        with open(csv_file_location, 'r', newline='') as f:
            reader = csv.reader(f)
            
            # Read header and find the 'Email Address' column dynamically
            header = next(reader)
            user_data_list.append(header)
            
            # Clean headers (remove accidental spaces) to find the right column
            clean_headers = [h.strip() for h in header]
            try:
                email_index = clean_headers.index('Email Address')
            except ValueError:
                # Fallback: Try finding a column that looks like an email header
                print("Warning: 'Email Address' column not found explicitly. searching...")
                email_index = 1 # Defaulting to column 2 if not found, or add better logic
            
            for row in reader:
                email = row[email_index].strip()
                
                if contains_domain(email, old_domain):
                    # Replace the email in the row directly
                    new_email = replace_domain(email, old_domain, new_domain)
                    row[email_index] = new_email
                    # (Optional) Print change for verification
                    # print(f"Updated: {email} -> {new_email}")
                
                user_data_list.append(row)

        # 3. Write the updated data
        with open(report_file, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerows(user_data_list)
            
        print(f"Success! Updated list saved to: {report_file}")

    except FileNotFoundError:
        print(f"Error: The file '{csv_file_location}' was not found.")

if __name__ == "__main__":
    main()