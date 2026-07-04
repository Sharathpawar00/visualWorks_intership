# Port Status Checker

A simple Python project that checks whether a specific port is open or closed on a given host.

## What It Does

- Takes a host address and port number as input
- Tries to connect to that host and port
- Prints whether the port is open or closed

## Requirements

- Python 3

No external packages are required.

## How To Run

Check a port using command-line arguments:

```bash
python port_status_checker.py 127.0.0.1 80
```

You can also run it without arguments and enter values when prompted:

```bash
python port_status_checker.py
```

Example output:

```text
Port 80 on 127.0.0.1 is closed.
```

## Project Task

Create a Python script that checks whether a specific port on a given system is open or closed. The program should take a port number as input and return its status.
