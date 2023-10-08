import shutil
import os

current_directory = os.getcwd()
# print(current_directory)

source_path = os.path.join(current_directory, "mssql8", "src", "catalogs", "tes", "tes.mdo")
# print(source_path)

destination_path = os.path.join(current_directory, "python-core", "metadata-inner-sync", "catalog_metedata_tes5.mdo")
print(destination_path)


# Копирование файла
shutil.copy2(source_path, destination_path)
