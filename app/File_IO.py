import json
import os


files_location = "./files"


def prepare_dir(dir_name):
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)


def prepare_file_dir(file_name):
    tree_list = file_name.split("/")[:-1]
    if tree_list:
        dir_path = "/".join(tree_list)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)


def load_object_from_json_file(file_name):
    file_name = f"{files_location}/{file_name}"
    prepare_file_dir(file_name)
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            object = json.load(f)
    else:
        object = {}

    return object


def store_object_to_json_file(the_dict, file_name):
    file_name = f"{files_location}/{file_name}"
    prepare_file_dir(file_name)
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(the_dict, f, ensure_ascii=False, indent=4, default=str)

    if os.path.exists(file_name):
        # print(f"Successfully stored {file_name} to {file_name}")
        return {"status": "Success"}
    else:
        # print(f"Failed to store {file_name} to {file_name}")
        return {"status": "Failure"}
    

def load_text_from_file(file_name):
    file_name = f"{files_location}/{file_name}"
    prepare_file_dir(file_name)
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = ""

    return text


def store_text_to_file(text, file_name):
    file_name = f"{files_location}/{file_name}"
    prepare_file_dir(file_name)
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(text)

    if os.path.exists(file_name):
        return {"status": "Success"}
    else:
        return {"status": "Failure"}
    

def remove_file(file_name):
    file_name = f"{files_location}/{file_name}"
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        return {"message": f"{file_name} does not exist"}

    if not os.path.exists(file_name):
        return {"message": f"Successfully deleted {file_name}"}
    
