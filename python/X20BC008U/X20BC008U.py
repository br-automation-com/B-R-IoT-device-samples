import time
from opcua import Client
from opcua import ua
import os

# OPC UA Server URL
OPC_UA_SERVER = "opc.tcp://192.168.1.1:4840"
# URI for the namespace
URI = "http://br-automation.com/OpcUa/BC/io-system/"
# Path to the variable list file
VAR_LIST = "varlist.txt"

class X20BC008U():
    """
    Class to handle the connection and subscription to the OPC UA server for the X20BC008U device.
    """

    def __init__(self, var_path=[], var_name=[], var_id=[]):
        """
        Initialize the X20BC008U object with variable paths, names, and IDs.
        """
        self.variable_path = var_path
        self.variable_name = var_name
        self.variable_id = var_id

    def event_notification(self, event):
        """
        Handle event notifications from the OPC UA server.
        """
        print("Python: New event", event)
    
    def load_config(self, path, callback_class):
        """
        Load the configuration from the varlist.txt file and subscribe to the variables.

        Args:
            path (str): Path to the varlist.txt file.
            callback_class (class): The callback class for handling data change notifications.
        """
        # Absolute path to varlist.txt
        varlist_path = os.path.join(os.path.dirname(__file__), path)

        # Read variable names and types from varlist.txt
        with open(varlist_path, "r") as file:
            for line in file.readlines():
                if line.startswith("#"):
                    continue
                var_path, var_name = line.strip().split(";")
                path_list = var_path.split(", ")
                var_path = [f"{self.uri_idx}:{item}" for item in path_list]  

                print(var_path)
                var_id = self.objects.get_child(var_path)
                print("var id is: ", var_id)
                var_node = self.client.get_node(var_id)
                print("var value is: ", var_node.get_value())

                self.variable_path.append(var_path)
                self.variable_name.append(var_name)
                self.variable_id.append(var_id)

                # subscribing to a variable node
                handler = callback_class(self.variable_path, self.variable_name, self.variable_id)
                sub = self.client.create_subscription(500, handler)
                handle = sub.subscribe_data_change(var_id)
                time.sleep(0.1)

    def connect(self, OPC_UA_SERVER, URI):
        """
        Connect to the OPC UA server and initialize the root and objects nodes.

        Args:
            OPC_UA_SERVER (str): The URL of the OPC UA server.
            URI (str): The URI for the namespace.
        """
        # Create a client and connect to the server
        self.client = Client(OPC_UA_SERVER)

        try:
            self.client.connect()
            print("Connected to the OPC UA Server")

            # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
            self.root = self.client.get_root_node()
            print("Root node is: ", self.root)
            self.objects = self.client.get_objects_node()
            print("Objects node is: ", self.objects)

            # Node objects have methods to read and write node attributes as well as browse or populate address space
            print("Children of root are: ", self.root.get_children())

            # getting our namespace idx
            self.uri_idx = self.client.get_namespace_index(URI)

        except Exception as e:
            print(e)

class DataCallback(object):
    """
    Callback class to handle data change and event notifications from the OPC UA server.
    """

    def __init__(self, var_path=[], var_name=[], var_id=[]):
        """
        Initialize the DataCallback object with variable paths, names, and IDs.
        """
        self.variable_path = var_path
        self.variable_name = var_name
        self.variable_id = var_id

    def datachange_notification(self, node, val, data):
        """
        Handle data change notifications from the OPC UA server.

        Args:
            node (Node): The node that changed.
            val (any): The new value of the node.
            data (DataChangeNotification): Additional data about the change.
        """
        if node in self.variable_id:
            index = self.variable_id.index(node)
            var_name = self.variable_name[index]
            print(f"Python: New data change event for {var_name}: {val}")
        else:
            print(f"Python: New data change event for unknown node {node}: {val}")

    def event_notification(self, event):
        """
        Handle event notifications from the OPC UA server.

        Args:
            event (EventNotification): The event notification.
        """
        print("Python: New event", event)

if __name__ == "__main__":
    bus_controller = X20BC008U()
    bus_controller.connect(OPC_UA_SERVER, URI)
    bus_controller.load_config(VAR_LIST, DataCallback)


