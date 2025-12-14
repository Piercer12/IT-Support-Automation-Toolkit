#!/usr/bin/env python3
import shutil
import psutil
import socket
import os
import sys

# Define thresholds
DISK_THRESHOLD = 20  # Percent
CPU_THRESHOLD = 80   # Percent
MEM_THRESHOLD = 100 * 1024 * 1024  # 100MB in bytes

def send_alert(subject, body):
    """
    Simulates sending an administrative email alert.
    In a production environment, this would use 'smtplib'.
    """
    print("--------------------------------------------------")
    print(f"[ALERT TRIGGERED] Sending email to admin...")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    print("--------------------------------------------------\n")

def check_disk_usage():
    """Checks if available disk space is lower than 20%."""
    du = shutil.disk_usage("/")
    # Calculate percentage of FREE space
    free_percent = (du.free / du.total) * 100
    
    if free_percent < DISK_THRESHOLD:
        subject = f"Error - Available disk space is less than {DISK_THRESHOLD}%"
        body = f"Warning: Only {free_percent:.2f}% disk space remaining."
        send_alert(subject, body)
    else:
        print(f"[OK] Disk Space: {free_percent:.2f}% free")

def check_cpu_usage():
    """Checks if CPU usage is higher than 80%."""
    # usage interval=1 second for accurate reading
    usage = psutil.cpu_percent(1)
    
    if usage > CPU_THRESHOLD:
        subject = f"Error - CPU usage is over {CPU_THRESHOLD}%"
        body = f"Warning: CPU usage is at {usage}%."
        send_alert(subject, body)
    else:
        print(f"[OK] CPU Usage: {usage}%")

def check_memory_usage():
    """Checks if available memory is less than 100MB."""
    mem = psutil.virtual_memory()
    
    if mem.available < MEM_THRESHOLD:
        subject = "Error - Available memory is less than 100MB"
        body = f"Warning: Only {mem.available / (1024*1024):.2f} MB memory available."
        send_alert(subject, body)
    else:
        print(f"[OK] Memory Available: {mem.available / (1024*1024):.2f} MB")

def check_localhost():
    """Checks if localhost resolves correctly to 127.0.0.1."""
    try:
        hostname = socket.gethostbyname('localhost')
        if hostname != '127.0.0.1':
            subject = "Error - localhost cannot be resolved to 127.0.0.1"
            body = f"Warning: Localhost resolves to {hostname}."
            send_alert(subject, body)
        else:
            print("[OK] Localhost resolution verified.")
    except socket.error:
        send_alert("Error - Localhost resolution failed", "Could not resolve 'localhost'.")

def main():
    print("Running System Health Checks...\n")
    check_disk_usage()
    check_cpu_usage()
    check_memory_usage()
    check_localhost()
    print("\nHealth check complete.")

if __name__ == "__main__":
    main()