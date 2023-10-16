import subprocess
import sys
import psutil

def start_application(app_path):
    process = subprocess.Popen(app_path)
    return process

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python startapp.py <application_path>")
        sys.exit(1)

    app_path = sys.argv[1]

    try:
        app_process = start_application(app_path)
        print(f"Started {app_path}.")
        print("Press Ctrl+C to close the Python script and the application.")

        while True:
            try:
                app_process.wait(timeout=1)
            except subprocess.TimeoutExpired:
                pass

    except KeyboardInterrupt:
        print("Exiting...")
        app_process.kill()

    except Exception as e:
        print(f"An error occurred: {e}")
