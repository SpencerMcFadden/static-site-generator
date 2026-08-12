import os
import shutil
import sys

from copystatic import copy_contents_to_directory
from page_generation import generate_pages_recursive

path_static = "./static"
path_docs = "./docs"
path_content = "./content"
template_path = "./template.html"


def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    print("Deleting docs directory...")
    if os.path.exists(path_docs):
        shutil.rmtree(path_docs)

    print("Copying static files to docs directory...")
    copy_contents_to_directory(path_static, path_docs)

    print("Generating content...")
    generate_pages_recursive(path_content, template_path, path_docs, basepath)


main()
