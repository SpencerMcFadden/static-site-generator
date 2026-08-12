import os
import shutil


def copy_contents_to_directory(source: str, destination: str) -> None:
    if not os.path.exists(source):
        raise ValueError("source does not exist")
    os.mkdir(destination)

    source_contents = os.listdir(source)
    for content in source_contents:
        working_path = os.path.join(source, content)
        print(f" ** {working_path} -> {destination}")
        if os.path.isfile(working_path):
            shutil.copy(working_path, destination)
        else:
            copy_contents_to_directory(working_path, os.path.join(destination, content))
