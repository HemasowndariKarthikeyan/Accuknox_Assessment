import requests
import time


def check_uptime(url):
    """
    Function to check the uptime of an application by sending an HTTP GET request.

    Parameters:
    url (str): The URL of the application to check.

    Returns:
    str: The status of the application ("up" or "down").
    """
    try:
        # Send an HTTP GET request to the application URL
        response = requests.get(url)

        # Check the status code of the response
        if response.status_code == 200:
            return "Application is UP"
        else:
            return f"Application is DOWN (Status Code: {response.status_code})"

    except requests.exceptions.RequestException as e:
        # Catch any error that occurs (e.g., network errors, timeouts)
        return f"Application is DOWN (Error: {str(e)})"


def monitor_uptime(url, interval=60):
    """
    Function to monitor the application's uptime at regular intervals.

    Parameters:
    url (str): The URL of the application to monitor.
    interval (int): Time in seconds between each uptime check.
    """
    print(f"Starting uptime monitor for: {url}")

    # Continuously check the uptime every 'interval' seconds
    while True:
        status = check_uptime(url)
        print(f"Status: {status}")

        # Wait for the specified interval before checking again
        time.sleep(interval)


# Example Usage
if __name__ == "__main__":
    app_url = "http://your-application-url.com"  # Replace with your app's URL
    monitor_uptime(app_url, interval=60)  # Monitor every 60 seconds
