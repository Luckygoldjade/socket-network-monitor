# Developed on Python 3.12.0
# Requires the following packages:
# pip install prompt-toolkit

import threading
import time
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.patch_stdout import patch_stdout

# include all network monitor functions here
from network_monitor_functions import ping, traceroute, check_server_http, check_server_https, check_ntp_server, check_dns_server_status, check_tcp_port, check_udp_port

# Worker thread function
def worker(stop_event: threading.Event) -> None:
    """
    Function run by the worker thread.
    Prints a message every 5 seconds until stop_event is set.
    """

    # serviceChecks[i] = [service, server, port, protocol]



    while not stop_event.is_set():
        print("Hello from the worker thread.")
        # Add your network monitor tests here


        # Ping Usage Example
        print("Ping Example:")
        ping_addr, ping_time = ping("8.8.8.8")
        print(f"Google DNS (ping): {ping_addr[0]} - {ping_time:.2f} ms" if (ping_addr and ping_time is not None) else "Google DNS (ping): Request timed out or no reply received")

        # # Traceroute Usage Example
        # # Note: This function is included as an extra to round out the ICMP examples.
        # print("\nTraceroute Example:")
        # print("Google DNS (traceroute):")
        # print(traceroute("8.8.8.8"))




        # Which service to check
        # service = "http"
        if service == "http":
            # HTTP/HTTPS Usage Examples
            print("\nHTTP/HTTPS Examples:")
            http_url = "http://example.com"
            http_server_status, http_server_response_code = check_server_http(http_url)
            print(f"HTTP URL: {http_url}, HTTP server status: {http_server_status}, Status Code: {http_server_response_code if http_server_response_code is not None else 'N/A'}")


        if service == "https":
            https_url = "https://example.com"
            https_server_status, https_server_response_code, description = check_server_https(https_url)
            print(f"HTTPS URL: {https_url}, HTTPS server status: {https_server_status}, Status Code: {https_server_response_code if https_server_response_code is not None else 'N/A'}, Description: {description}")




        if service == "ntp":
            # NTP Usage Example
            print("\nNTP Example:")
            ntp_server = 'pool.ntp.org'  # Replace with your NTP server
            ntp_server_status, ntp_server_time = check_ntp_server(ntp_server)
            print(f"{ntp_server} is up. Time: {ntp_server_time}" if ntp_server_status else f"{ntp_server} is down.")

        if service == "dns":
            # DNS Usage Examples
            print("\nDNS Examples:")
            dns_server = "8.8.8.8" # Google's public DNS server

            dns_queries = [
                ('google.com', 'A'),        # IPv4 Address
                ('google.com', 'MX'),       # Mail Exchange
                ('google.com', 'AAAA'),     # IPv6 Address
                ('google.com', 'CNAME'),    # Canonical Name
                ('yahoo.com', 'A'),         # IPv4 Address
            ]

            for dns_query, dns_record_type in dns_queries:
                dns_server_status, dns_query_results = check_dns_server_status(dns_server, dns_query, dns_record_type)
                print(f"DNS Server: {dns_server}, Status: {dns_server_status}, {dns_record_type} Records Results: {dns_query_results}")




        if service == "tcp":
            # TCP Port Usage Example
            print("\nTCP Port Example:")
            tcp_port_server = "google.com"
            tcp_port_number = 80
            tcp_port_status, tcp_port_description = check_tcp_port(tcp_port_server, tcp_port_number)
            print(f"Server: {tcp_port_server}, TCP Port: {tcp_port_number}, TCP Port Status: {tcp_port_status}, Description: {tcp_port_description}")


        if service == "udp":
            # UDP Port Usage Example
            print("\nUDP Port Example:")
            udp_port_server = "8.8.8.8"
            udp_port_number = 53
            udp_port_status, udp_port_description = check_udp_port(udp_port_server, udp_port_number)
            print(f"Server: {udp_port_server}, UDP Port: {udp_port_number}, UDP Port Status: {udp_port_status}, Description: {udp_port_description}")









        time.sleep(5)


# Main function
def main() -> None:
    """
    Main function to handle user input and manage threads.
    Uses prompt-toolkit for handling user input with auto-completion and ensures
    the prompt stays at the bottom of the terminal.
    """
    # Event to signal the worker thread to stop
    stop_event: threading.Event = threading.Event()

    # Create and start the worker thread
    worker_thread: threading.Thread = threading.Thread(target=worker, args=(stop_event,))
    worker_thread.start()

    # Command completer for auto-completion
    # This is where you will add new auto-complete commands
    command_completer: WordCompleter = WordCompleter(['exit'], ignore_case=True)

    # Create a prompt session
    session: PromptSession = PromptSession(completer=command_completer)

    # Variable to control the main loop
    is_running: bool = True

    try:
        with patch_stdout():
            while is_running:
                # Using prompt-toolkit for input with auto-completion
                user_input: str = session.prompt("Enter command: ")

                # Once this monitor is running, exiting is the only command available and needed






                if user_input == "exit":
                    print("Exiting application...")
                    is_running = False
    finally:
        # Signal the worker thread to stop and wait for its completion
        stop_event.set()
        worker_thread.join()


if __name__ == "__main__":
    main()
