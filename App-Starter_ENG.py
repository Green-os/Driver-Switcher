import subprocess

def run_command_with_dri_prime(driver_index, command):
    try:
        # Validate the driver index
        if driver_index not in [0, 1]:
            raise ValueError("Unknown driver index. <Provide names and numbers for your drivers.>")
            # Example -> "0 for Intel HD Graphics 520 or 1 for AMD Radeon R5 M330."

        # Run the entered command with the "DRI_PRIME" driver index
        subprocess.run(f'DRI_PRIME={driver_index} {command}', shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Command terminated with this error: {e}")
    except ValueError as ve:
        print(f"Driver error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    try:
        # Obtain the desired driver index from the user
        DRI = int(input("Choose the driver <Provide names and numbers for your drivers>: "))
        # Example -> "0 for Intel HD Graphics 520 or 1 for AMD Radeon R5 M330."

        # Incorrect input
        if DRI not in [0, 1]:
            raise ValueError("Unknown input. Please enter 0 or 1")

        command = input("Enter your command: ")

        # Run the entered command with the "DRI_PRIME" driver index
        run_command_with_dri_prime(DRI, command)

    except ValueError as ve:
        print(f"Unknown input: {ve}")
    except KeyboardInterrupt:
        print("\nProcess canceled by the user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
