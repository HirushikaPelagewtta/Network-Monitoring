# Network Monitoring System

A Python-based network monitoring solution that automatically discovers and tracks devices on your local network, providing real-time status updates through a web interface.

## Overview

This network monitoring system uses Nmap for network discovery and Flask for the web interface. It continuously scans your network to detect active devices, tracks their status over time, and stores historical data in an SQLite database. The system provides an intuitive web dashboard to view all monitored devices and their current status.

## Features

- **Automatic Network Discovery**: Uses Nmap to scan and discover devices on your network
- **Real-time Device Monitoring**: Tracks device status (up/down) and updates timestamps
- **SQLite Database Storage**: Lightweight database for storing device information and history
- **Web Dashboard**: Flask-based web interface for viewing device status
- **Device Status Tracking**: Monitors IP addresses, hostnames, status, and last seen timestamps
- **Automatic Status Updates**: Marks devices as "down" when they're no longer detected
- **Network Statistics**: Shows count of active devices
- **Command Line Interface**: Direct database viewing through terminal

## Technologies Used

- **Python 3.x** - Main programming language
- **Nmap** - Network discovery and security auditing
- **Flask** - Web framework for the dashboard interface
- **SQLite** - Lightweight database for data storage
- **python-nmap** - Python wrapper for Nmap

## Prerequisites

Before running this application, make sure you have the following installed:

- **Python 3.6+**
- **Nmap** - Network discovery tool
- **pip** - Python package installer

### System Requirements
- Linux, macOS, or Windows
- Network access to devices you want to monitor
- Administrator/root privileges may be required for some Nmap operations

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/HirushikaPelagewtta/Network-Monitoring.git
   cd Network-Monitoring/Network\ Monitoring\ project
   ```

2. **Install Python dependencies**
   ```bash
   pip install python-nmap flask
   ```

3. **Install Nmap** (if not already installed)
   
   **Ubuntu/Debian:**
   ```bash
   sudo apt-get install nmap
   ```
   
   **macOS:**
   ```bash
   brew install nmap
   ```
   
   **Windows:**
   Download and install from [nmap.org](https://nmap.org/download.html)

## Configuration

### Network Configuration

By default, the system scans the `192.168.1.0/24` subnet. To monitor a different network:

1. Open `Net_Monitoring.py`
2. Modify the subnet variable in the `main()` function:
   ```python
   subnet = "YOUR_NETWORK/24"  # Example: "10.0.0.0/24"
   ```

### Database Configuration

The system automatically creates an SQLite database (`devices.db`) with the following structure:
- **ip** (TEXT PRIMARY KEY) - Device IP address
- **hostname** (TEXT) - Device hostname
- **status** (TEXT) - Current status (up/down)
- **last_seen** (TIMESTAMP) - Last detection timestamp

## Usage

### 1. Run Network Scan

Execute the network monitoring script to scan your network and update the database:

```bash
python Net_Monitoring.py
```

This will:
- Scan the configured subnet for active devices
- Update device information in the database
- Mark previously active but now offline devices as "down"

### 2. View Database Contents

Check all monitored devices using the database viewer:

```bash
python Check_db.py
```

Output example:
```
IP Address | Hostname | Status | Last Seen
--------------------------------------------------
192.168.1.1 | router.local | up | 2025-07-19 10:30:45
192.168.1.100 | laptop-001 | down | 2025-07-19 09:15:22
192.168.1.50 | printer | up | 2025-07-19 10:30:45
```

### 3. Launch Web Dashboard

Start the Flask web interface:

```bash
python Web_interface.py
```

Then open your web browser and navigate to:
```
http://localhost:5000
```

The dashboard provides:
- List of all monitored devices
- Current status of each device
- Count of active devices
- Last seen timestamps

## Project Structure

```
Network Monitoring project/
├── Net_Monitoring.py      # Main network scanning and monitoring script
├── Check_db.py           # Command-line database viewer
├── Web_interface.py      # Flask web dashboard
├── devices.db           # SQLite database (created automatically)
└── templates/
    └── index.html       # Web dashboard template (required)
```

## Automation

### Scheduled Monitoring

To automatically run network scans at regular intervals, set up a cron job (Linux/macOS):

```bash
# Edit crontab
crontab -e

# Add this line to run every 5 minutes
*/5 * * * * /usr/bin/python3 /path/to/your/project/Net_Monitoring.py
```

### Windows Task Scheduler

For Windows, use Task Scheduler to run `Net_Monitoring.py` at regular intervals.

## Troubleshooting

### Common Issues

1. **Permission Denied**: Some Nmap operations require administrator privileges
   ```bash
   sudo python Net_Monitoring.py  # Linux/macOS
   ```

2. **Nmap Not Found**: Ensure Nmap is installed and in your system PATH

3. **No Devices Found**: 
   - Verify the subnet configuration matches your network
   - Check firewall settings
   - Ensure devices respond to ping

4. **Web Interface Not Loading**:
   - Check if Flask is properly installed
   - Verify the `templates/index.html` file exists
   - Check if port 5000 is available

### Debug Mode

Enable Flask debug mode for development:
```python
# In Web_interface.py, the debug mode is already enabled
app.run(debug=True, host='0.0.0.0', port=5000)
```

## Future Enhancements

- [ ] Add email/SMS notifications for device status changes
- [ ] Implement device grouping and categorization
- [ ] Add network performance metrics (latency, bandwidth)
- [ ] Create REST API for external integrations
- [ ] Add authentication and user management
- [ ] Implement data export functionality
- [ ] Add mobile-responsive design

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Hirushika Pelagewtta**
- GitHub: [@HirushikaPelagewtta](https://github.com/HirushikaPelagewtta)

## Acknowledgments

- [Nmap Project](https://nmap.org/) for the powerful network discovery tool
- [Flask](https://flask.palletsprojects.com/) for the lightweight web framework
- Python-nmap library developers for the Python wrapper

---

For questions, issues, or feature requests, please open an issue on GitHub.
