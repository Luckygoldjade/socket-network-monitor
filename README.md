# Socket Network Monitoring System

A Python-based socket programming project that monitors network uptime using custom service checks and an echo server-client model. This project demonstrates client-server communication, network monitoring automation, and user-defined service configuration.

## Project Overview

This system includes three main components:

1. **Network Monitoring Server**  
   Continuously monitors various internet services (HTTP, HTTPS, ICMP, DNS, NTP, TCP, UDP) for a list of configured servers. It also checks the status of a custom UDP Echo Server to validate socket communication.

2. **UDP Echo Server**  
   A continuously running UDP server that listens for and responds to echo messages. It acts as a target for the network monitor to validate internal network health.

3. **UDP Echo Client**  
   Sends echo messages to the UDP Echo Server and validates the response. Integrated into the network monitor to test server health.

## Project Structure

```bash
├── network_monitor_command.py       # Main app to monitor services
├── UDP_echo_server.py               # Standalone echo server
├── timestamp_printing.py            # Utility for time-stamped console output
├── network_monitor_functions.py     # Custom service check functions
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
```

## Features

- Modular Python code for easy extension and testing
- Command-line interface with word completion for usability
- Supports custom server/service configurations using dictionaries
- Supports custom time intervals per service
- Timestamped logging for network events
- Works on both internal (Echo Server) and external (e.g., google.com) services
- Concurrent service checks using Python threading for real-time and interval-based monitoring

## Threading and Concurrency

This project uses Python's `threading` module to perform multiple service checks in parallel. Each service is monitored in its own thread, allowing:

- Different frequency intervals for each service
- Minimal blocking or delays in the monitoring loop
- Real-time responsiveness and scalability

This design mirrors real-world network monitoring systems, where asynchronous, concurrent checks are crucial to reduce latency and ensure timely alerts.

## Setup

Install required packages:

```bash
pip install -r requirements.txt
```

## How to Run

Run each script in a separate terminal:

```bash
# Terminal 1: Start Echo Server (always on)
python UDP_echo_server.py

# Terminal 2: Launch Network Monitor
python network_monitor_command.py
```

## Sample Monitored Services

You can configure services like:

- `HTTP` for websites (e.g., `www.google.com`)
- `ICMP` for ping checks
- `DNS`, `NTP` for protocol-specific monitoring
- `UDP` port checks on external domains
- Internal loopback check via the UDP Echo Server

## Custom Configuration

In `network_monitor_command.py`, configure:

```python
service_config = {
    "www.google.com": {
        "services": ["HTTP", "ICMP"],
        "interval": 60  # seconds
    },
    "pool.ntp.org": {
        "services": ["NTP"],
        "interval": 120
    },
    "localhost": {
        "services": ["UDP"],
        "interval": 180
    }
}
```

## Final Report

For full implementation details, screenshots, and system behavior, refer to the final report:
[Sockets_Project_1_042024_v01.pdf](docs/Sockets_Project_1_042024_v01.pdf)

## Screenshots

Located in `/docs/screenshots/` (if provided):

- Service check with 1, 2, 3, 4, 5-minute intervals
- Echo client/server message confirmations
- Timestamped logging of network status

## Technologies Used

- Python 3.x
- UDP & TCP Sockets
- ICMP, HTTP, HTTPS, DNS, NTP protocols
- Threading and asynchronous checks
- Prompt Toolkit for user input management

## License

This project is released under the MIT License.
