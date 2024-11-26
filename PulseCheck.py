import os
import platform
import subprocess
from time import sleep
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import print as rprint

console = Console()

def display_logo():
    logo = """
    [bold cyan]
     ________   _____  _____
    |  ____\ \ / /\ \/ / _ \
    | |__   \ V /  \  / | | |
    |  __|   > <   /  \ | | |
    | |____ / . \ / /\ \| |_| |
    |______/_/ \_/_/  \_\\___/

    [bold yellow]Advanced IP Checker[/bold yellow] [white]-[/white] [green]Your friendly network assistant![/green][/bold cyan]
    """
    console.print(logo)

# Function to ping an IP address
def is_ip_alive(ip):
    if platform.system().lower() == "windows":
        command = ["ping", "-n", "1", ip]
    else:
        command = ["ping", "-c", "1", ip]

    try:
        response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return response.returncode == 0
    except Exception as e:
        console.log(f"[red]Error while pinging {ip}: {e}[/red]")
        return False

# Function to check IPs from a file
def check_ips_from_file(filename):
    try:
        with open(filename, "r") as file:
            ip_addresses = file.readlines()
    except FileNotFoundError:
        console.print(f"[red]File not found: {filename}[/red]")
        return

    ip_addresses = [ip.strip() for ip in ip_addresses if ip.strip()]

    live_ips = []
    dead_ips = []

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console) as progress:
        task = progress.add_task("Pinging IPs...", total=len(ip_addresses))

        for ip in ip_addresses:
            if is_ip_alive(ip):
                live_ips.append(ip)
            else:
                dead_ips.append(ip)
            progress.update(task, advance=1)

    # Display results
    console.rule("[green]Results[/green]")

    if live_ips:
        table = Table(title="Live IPs", style="green")
        table.add_column("IP Address", justify="center")
        for ip in live_ips:
            table.add_row(ip)
        console.print(table)
    else:
        rprint("[red]No live IPs found.[/red]")

    if dead_ips:
        table = Table(title="Dead IPs", style="red")
        table.add_column("IP Address", justify="center")
        for ip in dead_ips:
            table.add_row(ip)
        console.print(table)
    else:
        rprint("[green]No dead IPs found.[/green]")

# Main script
if __name__ == "__main__":
    display_logo()
    file_name = "ips.txt"  # Replace with your file name
    rprint(f"[blue]Reading IPs from:[/blue] [yellow]{file_name}[/yellow]")
    sleep(1)
    check_ips_from_file(file_name)
