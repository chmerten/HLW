# Python script to play an mp3 recording and interact with Arduino to control relays

import time
import subprocess
import serial

# Set the path to the mp3 recording
mp3_path = "recording.mp3"

# Set the Arduino serial port (change this to the actual port)
arduino_port = "/dev/ttyACM0"

# Open the serial connection to Arduino
ser = serial.Serial(arduino_port, 9600, timeout=1)

# Function to play the mp3 recording
def play_mp3():
    subprocess.Popen(["mpg123", mp3_path])

# Function to control the relay
def control_relay(relay_number, action):
    # Send command to Arduino
    ser.write(f"{relay_number}:{action}\n".encode())
    response = ser.readline().decode().strip()
    print(f"Relay {relay_number} {action}: {response}")

# Main function
def main():
    try:
        # Play the mp3 recording
        play_mp3()

        # Wait for specific playtime (adjust as needed)
        time.sleep(10)  # Example: wait for 10 seconds

        # Control relay 1 (open)
        control_relay(1, "ON")

        # Wait for another specific playtime
        time.sleep(5)  # Example: wait for 5 seconds

        # Control relay 1 (close)
        control_relay(1, "OFF")

    except KeyboardInterrupt:
        print("Script interrupted by user.")
    finally:
        # Close the serial connection
        ser.close()

if __name__ == "__main__":
    main()
