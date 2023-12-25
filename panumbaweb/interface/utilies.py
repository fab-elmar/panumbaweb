import paramiko



# unused
def ssh_to_server(hostname, port, username, key_file, command):
    # Initialize the SSH client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the server
    try:
        client.connect(hostname, port=port, username=username, key_filename=key_file)
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read()
        return output
    except Exception as e:
        print(f"Connection failed: {e}")
        return None
    finally:
        client.close()
