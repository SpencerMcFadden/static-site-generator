import os
import shutil

from copystatic import copy_contents_to_directory
from page_generation import generate_pages_recursive

path_static = "./static"
path_public = "./public"
path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(path_public):
        shutil.rmtree(path_public)

    print("Copying static files to public directory...")
    copy_contents_to_directory(path_static, path_public)

    print("Generating content...")
    generate_pages_recursive(path_content, template_path, path_public)


main()
