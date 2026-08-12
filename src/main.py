import os
import shutil

path_static = "./static"
path_public = "./public"


def main():
    copy_contents_to_directory(path_static, path_public)


def copy_contents_to_directory(source: str, destination: str) -> None:
    if not os.path.exists(source):
        raise ValueError("source does not exist")
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)

    source_contents = os.listdir(source)
    for content in source_contents:
        working_path = os.path.join(source, content)
        if os.path.isfile(working_path):
            shutil.copy(working_path, destination)
        else:
            copy_contents_to_directory(working_path, os.path.join(destination, content))


main()
