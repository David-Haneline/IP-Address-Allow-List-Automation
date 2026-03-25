### IP-Address-Allow-List-Automation

Python code to automate removal of disallowed IP Addresses from an allow list

## Project Overview

In a professional cybersecurity environment, managing access control lists is a critical task. This project demonstrates a Python-based automation tool that updates a server's "Allow List" by cross-referencing it against a list of unauthorized or restricted IP addresses.

Instead of manual editing, which is time consuming and prone to human error, this script ensures that the integrity of the security configuration is maintained through programmatic filtering.

## Project Origin and Continued Learning

The code originated while learning Python during the Google Cybersecurity Professional certification course.  Originally, the code used a basic **for loop**, and lacked any kind of error handling, as this was not covered in the course.  Recognizing the lack of error handling, and wanting to ensure the code was as correct and robust as possible, I used Google Gemini for advice and continued learning.  It was here that I was introduced to **List Comprehension**, a subject which I pursued further via Youtube.

## Key Features

Automated File I/O: Programmatically reads from and writes to security configuration files.

Robust Error Handling: Utilizes **try...except** blocks to prevent system crashes during missing file scenarios:

```python
    except FileNotFoundError:
        print(f"Error: The file '{import_file}' was not found. Please check the file path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

Data Transformation: Efficiently converts raw string data into iterable lists for precise filtering.

Optimized Filtering: Employs List Comprehension to ensure high performance and avoid common iteration bugs.


## Why List Comprehension?

To ensure the script is ready for use, and bug free, I used list comprehension:

```python
    # Efficiently filter unauthorized IPs
    ip_addresses = [ip for ip in ip_addresses if ip not in remove_list]
    
    with open(import_file, "w") as file:
        file.write(" ".join(ip_addresses))
```

This approach is more performant than a standard for loop and avoids the Index-Skipping Bug that occurs when removing items from a list while iterating through it.

## Error Handling & Reliability

The script is wrapped in a **try...except** block to handle **FileNotFoundError**. In a real-world security pipeline, this prevents the entire automation suite from failing if a single log file is moved or renamed.

## File Structure

ip_filter.py: The Python script.

allow_list.txt: A sample source of permitted IP addresses for testing.
