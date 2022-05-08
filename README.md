# QA Embedded Test Python

## Part 1: Unit Testing
> Setup:
   - OS: Windows 10
   - Python version: 2.7.14 
   - pytest version: 3.10.0
   - IDE: VsCode
   
 # Question 1:
 > Function1 Named: printFirstRepeatedInteger
 - File Named: Function1.py
 - To Run the script ==>  **pytest Function1.py**
 - "A" and "B" are arrays that you need to enter values to test the functions
 
 # Question 2:
 > Function2 Named: FindFirstFile
 - File Named: Function1.py
 - To Run the script ==>  **pytest Function1.py**
 - "pf" is the path of your system to test the functions
   
 # Question 3:
 > Skipped
 
## Part 2: System Testing

# Question a:

Since Embedded and cloud have a WiFi connection, HTTP or REST protocols can test this case using GET and Post requests.
And to test WiFi API manually we can use application "Acrylic WiFi Home" and "inSSIDer" to scan WiFi
and to detect the SSID, Band (2.4 GHz or 5GHz), the amplitude and Channel.
Also we can use "JumpStart" to simulate the connection.

# Question b:

We can use Appium, it can run on real iOS and Android devices as well as simulated devices.
It  provide access to Bluetooth functionality through Bluetooth APIs. 
Bluetooth APIs are available in the android.bluetooth package.
There are classes and interfaces needed in order to create Bluetooth connections like:
( BluetoothAdapter, BluetoothDevice, BluetoothSocket, BluetoothServerSocket ...)
