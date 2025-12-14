#!/usr/bin/env python3
import os
import requests
import sys

def upload_feedback(source_dir):
    """
    Reads text files from a directory and posts them to a web API.
    """
    # Using httpbin.org to simulate a real API endpoint for demonstration
    # In a real scenario, this would be your company's internal server IP
    API_URL = 'https://httpbin.org/post' 
    
    # Check if the directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Directory '{source_dir}' not found.")
        return

    feedback_files = os.listdir(source_dir)
    success_count = 0

    print(f"Processing {len(feedback_files)} files from {source_dir}...")

    for file in feedback_files:
        # Only process .txt files to avoid hidden system files
        if not file.endswith('.txt'):
            continue

        file_path = os.path.join(source_dir, file)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                # Parsing the standard feedback format:
                # Line 1: Title, Line 2: Name, Line 3: Date, Line 4+: Content
                title = f.readline().strip()
                name = f.readline().strip()
                date = f.readline().strip()
                content = f.read().strip()

                # Create the payload
                feedback_data = {
                    "title": title,
                    "name": name,
                    "date": date,
                    "feedback": content
                }

            # Send POST request
            print(f"Uploading: {title}...")
            response = requests.post(API_URL, json=feedback_data)

            # Check for success (200 OK or 201 Created)
            if response.status_code in [200, 201]:
                print(f"  [✓] Success! Server responded: {response.status_code}")
                success_count += 1
            else:
                print(f"  [X] Failed. Status code: {response.status_code}")

        except Exception as e:
            print(f"  [!] Error processing {file}: {e}")

    print(f"\nCompleted. Uploaded {success_count} files successfully.")

if __name__ == "__main__":
    # Point to the local 'feedback_data' folder
    # Uses generic pathing to work on any OS
    current_dir = os.path.dirname(os.path.abspath(__file__))
    feedback_path = os.path.join(current_dir, 'feedback_data')
    
    upload_feedback(feedback_path)