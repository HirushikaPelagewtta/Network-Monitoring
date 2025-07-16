import sqlite3

def fetch_all_devices():
    """Fetches all device records from the database."""
    conn = sqlite3.connect('devices.db')
    c = conn.cursor()
    
    c.execute("SELECT * FROM devices")
    rows = c.fetchall()
    
    conn.close()
    return rows

def display_devices(devices):
    """Displays the fetched device records in a readable format."""
    print("IP Address | Hostname | Status | Last Seen")
    print("-" * 50)
    for row in devices:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

def main():
    """Main function to fetch and display devices."""
    devices = fetch_all_devices()
    display_devices(devices)

if __name__ == "__main__":
    main()
