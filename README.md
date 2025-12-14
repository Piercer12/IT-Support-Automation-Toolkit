# 🛠️ IT Support Automation Toolkit

## 🚀 Project Overview
This repository serves as a centralized collection of Python automation scripts and utilities designed to streamline daily IT support tasks. The tools included here focus on reducing manual workload for System Administrators by automating log analysis, error tracking, and file management.

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
    * **Error Handling:** Robust validation to prevent crashes if input files are missing.

---

## ⚙️ Installation & Usage

### Prerequisites
* Python 3.x installed
* A sample log file (e.g., `syslog.log` or any `.txt` file)

### How to Run `log_search.py`
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/it-support-toolkit.git](https://github.com/yourusername/it-support-toolkit.git)
    cd it-support-toolkit
    ```

2.  **Run the script:**
    Pass the log file you want to analyze as an argument.
    ```bash
    python3 log_search.py syslog.log
    ```

3.  **Follow the prompt:**
    The script will ask: `What is the error?`
    * *Example Input:* `CRON ERROR` (This searches for lines containing both "CRON" and "ERROR")

4.  **View Results:**
    The script will create a directory and save the results:
    `~/data/errors_found.log`

---

## 💡 Technical Skills Demonstrated
This repository showcases the following technical competencies relevant to **IT Operations** and **DevOps**:

* **File I/O Operations:** Reading, writing, and appending to files safely using context managers (`with open...`).
* **Regular Expressions (Regex):** Using the `re` module for pattern matching to filter noise from data.
* **Defensive Programming:** Implementing `try/except` blocks and directory checks (`os.path.exists`) to build resilient tools.
* **CLI Development:** Handling command-line arguments using `sys.argv`.

---

## 📬 Contact
**Clarence Sulit**
* **Role:** Technical Support Lead & Automation Enthusiast
* **Portfolio:** [Link to your GitHub Profile]
* **Email:** sulitc6@gmail.com
