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
