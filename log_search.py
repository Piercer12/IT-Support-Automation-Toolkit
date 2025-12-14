#!/usr/bin/env python3
import sys
import os
import re

def error_search(log_file):
    # Get the search query from the user
    error = input("What is the error? ")
    returned_errors = []
    
    # Open the file using UTF-8 to avoid encoding issues
    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            error_patterns = ["error"]
            
            # Create regex patterns for each word in the user's input
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
            
            # Check if ALL keywords exist in the current log line
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
                
    return returned_errors

def file_output(returned_errors):
    # Define the output path (creates a 'data' folder in your home directory)
    # Note: Ensure the directory exists or the script might fail if the folder is missing.
    output_dir = os.path.expanduser('~') + '/data/'
    output_file = output_dir + 'errors_found.log'
    
    # Check if directory exists, if not, create it (Added safety step)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(output_file, 'w') as file:
        for error in returned_errors:
            file.write(error)
    
    print(f"Results saved to: {output_file}")

if __name__ == "__main__":
    try:
        # Takes the log file as a command line argument
        log_file = sys.argv[1]
        returned_errors = error_search(log_file)
        file_output(returned_errors)
        sys.exit(0)
    except IndexError:
        print("Error: Please provide the input log file path.")
        print("Usage: ./log_search.py [path_to_logfile]")
        sys.exit(1)