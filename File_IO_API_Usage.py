import requests
import json

# file_io_api_server_name_and_port = "http://127.0.0.1:8005"
file_io_api_server_name_and_port = "http://127.0.0.1:8006"


def get_file_list():
    url = f"{file_io_api_server_name_and_port}/list_files"

    headers = {"Content-Type": "application/json"}
    file_io_response = requests.get(url=url, headers=headers)

    data = json.loads(file_io_response.text)
    
    return data

def get_client_object_from_json_file(file_name):
    url = f"{file_io_api_server_name_and_port}/load_client_object_from_json_file?file_name={file_name}"

    headers = {"Content-Type": "application/json"}
    file_io_response = requests.get(url=url, headers=headers)

    data = json.loads(file_io_response.text)
    
    return data


def store_client_object_to_json_file(client_data_D):
    url = f"{file_io_api_server_name_and_port}/store_client_object_to_json_file"
    headers = {"Content-Type": "application/json"}
    jsonized_data = json.dumps(client_data_D, default=str)
    file_io_response = requests.post(url=url, headers=headers, data=jsonized_data)

    return file_io_response

def store_client_objects_list_to_json_file(client_data_D_list):
    url = f"{file_io_api_server_name_and_port}/store_client_objects_list_to_json_file"
    headers = {"Content-Type": "application/json"}
    jsonized_data = json.dumps(client_data_D_list, default=str)
    file_io_response = requests.post(url=url, headers=headers, data=jsonized_data)

    return file_io_response


####### Calls To Functions ########
### Call 1
file_list = get_file_list()
type_file_list = type(file_list)
print(file_list)
print(type_file_list)
print()

### Call 2
new_client_object = {
    "File_Name": "Second_Client.json",
    "Client_Name": "Sue Ives",
    "Client_Email": "sue.ives@donkey.org",
    "Client_Phone": "505.555.3452",
    "Client_Company": "Dockeys On The Edge",
    "Client_ID": "007",
    "Agent_Name": "Death Con 5",
    "Agent_Email": "dogs.out@now.org",
    "Agent_Phone": "505.555.0985"
  }

client_storage_response = store_client_object_to_json_file(new_client_object)
print(client_storage_response.text)
print()

### Call 3
client_object = get_client_object_from_json_file("Second_Client.json")
type_client_object = type(client_object)
print(client_object)
print(type_client_object)
print()

### Call 4
new_client_objects_list = [
    {
        "File_Name": "Client_List_2.json",
        "Client_Name": "David Ives",
        "Client_Email": "david.ives@mowers.net",
        "Client_Phone": "505.555.3449",
        "Client_Company": "Testers",
        "Client_ID": "003",
        "Agent_Name": "Eye Care",
        "Agent_Email": "eye.care@alot.net",
        "Agent_Phone": "505.555.0982"
    },
    {
        "File_Name": "Client_List_2.json",
        "Client_Name": "Abby Ives",
        "Client_Email": "anna.ives@spicy.net",
        "Client_Phone": "505.555.7773",
        "Client_Company": "Exercise Physiologists",
        "Client_ID": "004",
        "Agent_Name": "Beat You Up",
        "Agent_Email": "beat.up@you.net",
        "Agent_Phone": "505.555.0983"
    }
]

clients_storage_response = store_client_objects_list_to_json_file(new_client_objects_list)
print(clients_storage_response.text)
print()

### Call 5
client_objects = get_client_object_from_json_file("Client_List_2.json")
type_client_objects = type(client_objects)
print(client_objects)
print(type_client_objects)
print()