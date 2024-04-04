import File_IO as file_io


files_location = "./files"

file_io.prepare_dir(files_location)

the_D = file_io.load_object_from_json_file("first_file.json")
print(the_D)
print()

the_D["key_1"] = 1.0
the_D["key_2"] = 2.0

file_io.store_object_to_json_file(the_D, "first_file.json")

the_D = file_io.load_object_from_json_file("first_file.json")
print(the_D)