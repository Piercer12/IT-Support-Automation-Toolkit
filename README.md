# 🛠️ IT Support Automation Toolkit

## 🚀 Project Overview
This repository serves as a centralized collection of Python automation scripts and utilities designed to streamline daily IT support tasks. The tools included here focus on reducing manual workload for System Administrators by automating log analysis, data migration, and error tracking.

**Goal:** To apply Python scripting to solve real-world operational challenges in an Enterprise Support environment.

---

## 📂 Included Tools

### 1. Interactive Log Searcher (`log_search.py`)
A command-line interface (CLI) tool that allows support engineers to filter massive system logs based on dynamic user queries.

* **Problem Solved:** Manually "grepping" or reading logs for specific error codes is time-consuming and prone to human error.
* **Key Features:**
    * **Dynamic Filtering:** Accepts multiple keywords from the user to perform complex searches.
    * **Automated Export:** Saves all matching lines to a dedicated `errors_found.log` file for documentation.
    * **Cross-Platform:** Uses `os.path` and `os.makedirs` to ensure compatibility across Linux, Windows, and macOS.

### 2. Bulk User Domain Migrator (`domain_migrator.py`)
A Python automation script for batch processing user data during system migrations.

* **Problem Solved:** Automates the tedious task of updating email domains (e.g., changing `@abc.edu` to `@xyz.edu`) for hundreds of users in legacy databases or CSV exports.
* **Key Features:**
    * **CSV Parsing:** Reads and modifies CSV data structures programmatically.
    * **Regex Substitution:** Safely identifies and replaces email domains without affecting usernames.
    * **Dynamic Column Handling:** Automatically detects email columns even if headers contain whitespace errors.
 
    * ### 3. CLI Employee Email Lookup (`email_lookup.py`)
A quick command-line utility to retrieve user contact details without manually opening database files.

* **Problem Solved:** Saves time for IT support staff who frequently need to find user emails during account troubleshooting.
* **Key Features:**
    * **Instant Lookup:** Accepts a First and Last Name as arguments to return the email instantly.
    * **Dictionary Mapping:** Efficiently maps names to emails using Python dictionaries for O(1) lookup speed.
    * **Error Handling:** Gracefully handles missing names or missing database files.

---
### 🔹 Tool 3: How to Run `email_lookup.py`
1.  **Run the script:**
    Pass the user's First and Last name as arguments.
    ```bash
    python3 email_lookup.py John Doe
    ```
2.  **View Results:**
    Output: `Email for John Doe: jdoe@example.com`
    

    ### 4. Feedback to Web API Uploader (`feedback_uploader.py`)
A backend automation script that digitizes offline text data by uploading it to a RESTful API endpoint.

* **Problem Solved:** Bridges the gap between legacy file-based systems (offline feedback forms) and modern web dashboards.
* **Key Features:**
    * **API Integration:** Uses the Python `requests` library to send POST requests with JSON payloads.
    * **Data Parsing:** Extracts structured data (Title, Date, Author) from unstructured text files.
    * **Testing Mode:** Configured to use `httpbin.org` for live demonstration purposes without needing a local server.

---
### 🔹 Tool 4: How to Run `feedback_uploader.py`
1.  Navigate to the tool directory:
    ```bash
    cd Feedback-Uploader-Tool
    ```
2.  Run the script:
    ```bash
    python3 feedback_uploader.py
    ```
3.  **View Results:**
    The script will process the files in `feedback_data/` and display the HTTP success codes (200 OK) received from the test server.


    ### 5. Automated Sales Reporting System (`sales_report.py`)
A business intelligence script that ingests raw sales data (JSON) and outputs actionable insights via Email and CSV.

* **Problem Solved:** Automates the weekly task of calculating revenue leaders and sales trends, replacing manual Excel work.
* **Key Features:**
    * **JSON Parsing:** Converts nested JSON objects (Car Make/Model/Year) into flat, readable formats.
    * **Financial Analysis:** Algorithms identify the highest revenue generator and most popular sales year automatically.
    * **Automated Reporting:** Simulates sending an executive summary email and auto-generates a detailed CSV attachment.

---
### 🔹 Tool 5: How to Run `sales_report.py`
1.  Navigate to the directory:
    ```bash
    cd Sales-Reporting-Tool
    ```
2.  Run the script:
    ```bash
    python3 sales_report.py
    ```
3.  **View Results:**
    * The script will print an **Email Simulation** to the console.
    * It will generate a file named `sales_summary_report.csv` in the same folder.
  

### 6. Automated System Health Monitor (`system_health_monitor.py`)
A proactive infrastructure monitoring script that checks critical system resources (CPU, Memory, Disk, Network) and triggers alerts.

* **Problem Solved:** Prevents server crashes by detecting resource exhaustion before it becomes critical.
* **Key Features:**
    * **Resource Tracking:** Uses `psutil` and `shutil` libraries to inspect real-time system metrics.
    * **Threshold Logic:** Automatically triggers specific alerts if CPU > 80% or Free Disk < 20%.
    * **Network Verification:** Ensures local DNS resolution is functioning correctly.
    * **Alert Simulation:** Prints formatted alert messages to the console for testing purposes (can be extended to SMTP).

---
### 🔹 Tool 6: How to Run `system_health_monitor.py`
1.  **Install dependency:**
    (Note: This script requires the `psutil` library. If you don't have it, install it via pip)
    ```bash
    pip install psutil
    ```
2.  **Run the script:**
    ```bash
    python3 system_health_monitor.py
    ```
3.  **View Results:**
    The script will output the status of your current computer (e.g., `[OK] CPU Usage: 12%`).

---

## ⚙️ Installation & Usage

### Prerequisites
* Python 3.x installed
* Sample data files (e.g., `syslog.log` for logs, `user_emails.csv` for migration)

### 🔹 Tool 1: How to Run `log_search.py`
1.  **Run the script:**
    Pass the log file you want to analyze as an argument.
    ```bash
    python3 log_search.py syslog.log
    ```
2.  **Follow the prompt:**
    The script will ask: `What is the error?`
    * *Example Input:* `CRON ERROR`
3.  **View Results:**
    The script will save the results to: `~/data/errors_found.log`

### 🔹 Tool 2: How to Run `domain_migrator.py`
1.  **Run the script:**
    Pass the CSV file you want to update.
    ```bash
    python3 domain_migrator.py user_emails.csv
    ```
2.  **View Results:**
    The script will generate a new file in the same folder named `user_emails_updated.csv` containing the new domain addresses.

---

## 💡 Technical Skills Demonstrated
This repository showcases the following technical competencies relevant to **IT Operations** and **DevOps**:

* **File I/O Operations:** Reading/writing logs and CSVs safely using context managers (`with open...`).
* **Regular Expressions (Regex):** Using the `re` module for precise pattern matching and substitution.
* **Data Migration:** Automating bulk data updates and format standardization.
* **Defensive Programming:** Implementing `try/except` blocks and directory checks (`os.path.exists`) to build resilient tools.
* **CLI Development:** Handling command-line arguments using `sys.argv`.

---

## 📬 Contact
**Clarence Sulit**
* **Role:** Technical Support Lead & Automation Enthusiast
* **Portfolio:** [Link to your GitHub Profile]
* **Email:** sulitc6@gmail.com
