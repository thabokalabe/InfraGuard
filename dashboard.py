import matplotlib.pyplot as plt
import json

# Load processed data from JSON file
def load_processed_data(filename):
    with open(filename, 'r') as f:
        processed_data = json.load(f)
    return processed_data

# Create a bar chart for email users
def create_email_users_chart(email_data):
    users = email_data['users']
    server_name = email_data['server_name']

    plt.bar(server_name, users)
    plt.xlabel('Email Servers')
    plt.ylabel('Number of Users')
    plt.title('Email Server Users')
    plt.show()

# Create a line chart for web requests
def create_web_requests_chart(web_data):
    requests_per_minute = web_data['requests_per_minute']
    server_name = web_data['server_name']

    plt.plot(server_name, requests_per_minute, marker='o')
    plt.xlabel('Web Servers')
    plt.ylabel('Requests per Minute')
    plt.title('Web Server Requests')
    plt.show()

# Main function for creating the dashboard
def main():
    processed_data = load_processed_data('processed_data.json')

    email_data = processed_data['email_data']
    create_email_users_chart(email_data)

    web_data = processed_data['web_data']
    create_web_requests_chart(web_data)

    # Add more chart creation functions for other data as needed

if __name__ == "__main__":
    main()