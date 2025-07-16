import nmap
import sqlite3
from datetime import datetime

def scan_network(subnet):
    nm = nmap.PortScanner()
    nm.scan(hosts=subnet, arguments='-sn')

    devices = []
    for host in nm.all_hosts():
        hostname = nm[host].hostname() if nm[host].hostname() else "Unknown"
        status = nm[host].state() if nm[host].state() else "Unknown"
        devices.append({'ip': host, 'hostname': hostname, 'status': status})

    return devices 

def create_db():
    conn = sqlite3.connect('devices.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS devices (
                    ip TEXT PRIMARY KEY,
                    hostname TEXT,
                    status TEXT,
                    last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )''')
    conn.commit()
    conn.close()



def insert_or_update_device(ip, hostname, status):
    conn = sqlite3.connect('devices.db')
    c = conn.cursor()

    # Get the local time
    local_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    c.execute('''INSERT OR REPLACE INTO devices (ip, hostname, status, last_seen)
                 VALUES (?, ?, ?, ?)''', (ip, hostname, status, local_time))

    conn.commit()
    conn.close()

def mark_disconnected_devices(active_ips):
    """Update the status of previously active devices to 'down' if not found in the new scan."""
    conn = sqlite3.connect('devices.db')
    c = conn.cursor()
    c.execute("UPDATE devices SET status='down' WHERE ip NOT IN ({})".format(
        ','.join('?' * len(active_ips))
    ), active_ips)
    conn.commit()
    conn.close()

def main():
    subnet = "192.168.1.0/24"  # Set the subnet here
    create_db()

    # Perform network scan
    scanned_devices = scan_network(subnet)
    
    # Extract active IPs
    active_ips = [device['ip'] for device in scanned_devices]

    # Insert or update scanned devices
    for device in scanned_devices:
        insert_or_update_device(device['ip'], device['hostname'], device['status'])

    # Mark disconnected devices as "down"
    if active_ips:
        mark_disconnected_devices(active_ips)

    print("Network scan completed. Database updated.")

if __name__ == "__main__":
    main()
