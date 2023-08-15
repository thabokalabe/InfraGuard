import requests
import psutil
import time
import json

# Configuration - Replace with your actual configuration
API_ENDPOINTS = {
    'email_server': 'http://comnet.co.ls/api',
    'web_server': 'http://comnet.co.ls/api',
    # ... Add more endpoints for other components
}

# Function to collect data from email server
def collect_email_data():
    email_data = {}  # Placeholder for collected data
    try:
        response = requests.get(API_ENDPOINTS['email_server'])
        email_data = response.json()
    except Exception as e:
        print("Error collecting email server data:", e)
    return email_data

# Function to collect data from web server
def collect_web_data():
    web_data = {}  # Placeholder for collected data
    try:
        response = requests.get(API_ENDPOINTS['web_server'])
        web_data = response.json()
    except Exception as e:
        print("Error collecting web server data:", e)
    return web_data

# Function to collect system metrics
def collect_system_metrics():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    network_stats = psutil.net_io_counters()
    
    system_metrics = {
        'cpu_percent': cpu_percent,
        'memory_percent': memory_percent,
        'disk_usage': disk_usage,
        'network_stats': network_stats._asdict()
    }
    return system_metrics

# Main function to collect data and save to JSON file
def main():
    while True:
        email_data = collect_email_data()
        web_data = collect_web_data()
        system_metrics = collect_system_metrics()
        
        collected_data = {
            'email_data': email_data,
            'web_data': web_data,
            'system_metrics': system_metrics
        }
        
        with open('collected_data.json', 'w') as f:
            json.dump(collected_data, f, indent=4)
        
        print("Data collected and saved.")
        
        time.sleep(300)  # Sleep for 5 minutes before collecting data again

if __name__ == "__main__":
    main()