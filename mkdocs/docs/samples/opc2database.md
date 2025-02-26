# EdgeController Project

This project is designed to connect to an OPC UA server, read variable values, and insert them into a MySQL database. It provides a simple interface for monitoring and logging data from industrial automation systems.

## Project Structure

```
python
├── OPCUA2SQL
    ├── opcua2sql.py       # Main logic for OPC UA connection and data logging
    ├── varlist.txt        # Variable names and types for OPC UA
    └── requirements.txt    # Required Python packages
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone https://github.com/br-automation-com/B-R-IoT-device-samples
   cd EdgeController
   ```

2. **Install required packages**:
   Navigate to the `OPCUA2SQL` directory and install the required packages using pip:
   ```
   pip install -r requirements.txt
   ```

3. **Configure the OPC UA server**:
   Update the `opcua2sql.py` file with the correct OPC UA server URL and database connection details.

4. **Define variables**:
   Edit the `varlist.txt` file to include the variable names and types you wish to monitor.

## Usage

Run the main script to start reading values from the OPC UA server and logging them into the MySQL database:
```
python opcua2sql.py
```

Ensure that the MySQL server is running and accessible with the credentials provided in the script. The data will be inserted into the specified table in the database.

## License

This project is licensed under the MIT License. See the LICENSE file for details.