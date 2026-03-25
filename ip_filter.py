def update_file(import_file, remove_list):
    """
    Automates the removal of unauthorized IP addresses from an allow list.

    Args:
        import_file (str): The path to the text file containing IP addresses.
        remove_list (list): A list of IP addresses to be removed from the file.
    """
    try:
        # Step 1: Read the file content
        with open(import_file, "r") as file:
            ip_addresses = file.read().split()

        # Step 2: Remove unauthorized IPs
        ip_addresses = [ip for ip in ip_addresses if ip not in remove_list]

        # Step 3: Rewrite the file with the clean data
        with open(import_file, "w") as file:
            file.write(" ".join(ip_addresses))

        print(f"Success: {import_file} has been updated. Unauthorized IPs removed.")

    except FileNotFoundError:
        print(f"Error: The file '{import_file}' was not found. Please check the file path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# --- Execution Section ---
if __name__ == "__main__":
    # Define your parameters
    target_file = "allow_list.txt"
    unauthorized_ips = ["192.168.1.1", "10.0.0.5", "172.16.0.2"]

    # Run the function
    update_file(target_file, unauthorized_ips)
