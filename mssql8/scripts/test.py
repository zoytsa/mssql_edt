import os

current_directory = os.getcwd()
print(current_directory)
# source_path = os.path.join(current_directory, "src", "tmp_tes.mdo")
# destination_path = os.path.join(current_directory, "scripts", "metadata-inner-sync", "catalog_metedata_tes2.mdo")

# current_directory = os.getcwd()

source_path = os.path.join(current_directory, "mssql8", "src", "tmp_tes.mdo")
destination_path = os.path.join(current_directory, "mssql8", "scripts", "metadata-inner-sync", "catalog_metedata_tes2.mdo")

print(source_path)
print(destination_path)
