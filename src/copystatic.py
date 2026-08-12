import os
import shutil


def copy_contents_to_directory(source: str, destination: str) -> None:
    if not os.path.exists(destination):
        os.makedirs(destination)

    source_contents = os.listdir(source)
    for content in source_contents:
        working_path = os.path.join(source, content)
        dest_path = os.path.join(destination, content)
        print(f" ** {working_path} -> {dest_path}")
        if os.path.isfile(working_path):
            shutil.copy(working_path, dest_path)
        else:
            copy_contents_to_directory(working_path, dest_path)
