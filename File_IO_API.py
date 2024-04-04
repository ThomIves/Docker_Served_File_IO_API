from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel

import File_IO as file_io
import json
import os


class Client_Storage_Object(BaseModel):
    File_Name: str
    Client_Name: str
    Client_Email: str
    Client_Phone: str
    Client_Company: str
    Client_ID: str
    Agent_Name: str
    Agent_Email: str
    Agent_Phone: str


class Company_Storage_Object(BaseModel):
    File_Name: str
    Rep_Name: str
    Rep_Email: str
    Rep_Phone: str


app = FastAPI()
# C:\Users\tives\Envs\py312std\Scripts\activate
# uvicorn File_IO_API:app --port 8005 --reload


files_location = "./files"

origins = [
    "http://127.0.0.1:3000", # Outlook Add-In
    "http://127.0.0.1:5500"  # VS Code Live Server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/list_files")
def get_json_file_list():
    file_io.prepare_dir(f"{files_location}")
    file_list = os.listdir(f"{files_location}")

    return file_list


@app.get("/load_client_object_from_json_file")
def get_data_object_from_json_file(file_name: str):
    data_obj = file_io.load_object_from_json_file(file_name)

    return data_obj


@app.post("/store_client_object_to_json_file")
def post_user_object_to_json_file(storage_object: Client_Storage_Object):
    the_dict = {}

    the_dict["File_Name"] = storage_object.File_Name
    the_dict["Client_Name"] = storage_object.Client_Name
    the_dict["Client_Email"] = storage_object.Client_Email
    the_dict["Client_Phone"] = storage_object.Client_Phone
    the_dict["Client_Company"] = storage_object.Client_Company
    the_dict["Client_ID"] = storage_object.Client_ID
    the_dict["Agent_Name"] = storage_object.Agent_Name
    the_dict["Agent_Email"] = storage_object.Agent_Email
    the_dict["Agent_Phone"] = storage_object.Agent_Phone

    return file_io.store_object_to_json_file(the_dict, storage_object.File_Name)


@app.post("/store_client_objects_list_to_json_file")
def post_data_object_to_json_file(storage_objects: List[Client_Storage_Object]):
    clients = []

    number_of_clients = len(storage_objects)

    for client_num in range(number_of_clients):
        clients.append({})

        clients[client_num]["File_Name"] = storage_objects[client_num].File_Name
        clients[client_num]["Client_Name"] = storage_objects[client_num].Client_Name
        clients[client_num]["Client_Email"] = storage_objects[client_num].Client_Email
        clients[client_num]["Client_Phone"] = storage_objects[client_num].Client_Phone
        clients[client_num]["Client_Company"] = storage_objects[client_num].Client_Company
        clients[client_num]["Client_ID"] = storage_objects[client_num].Client_ID
        clients[client_num]["Agent_Name"] = storage_objects[client_num].Agent_Name
        clients[client_num]["Agent_Email"] = storage_objects[client_num].Agent_Email
        clients[client_num]["Agent_Phone"] = storage_objects[client_num].Agent_Phone

    response = file_io.store_object_to_json_file(clients, storage_objects[0].File_Name)
    
    return response