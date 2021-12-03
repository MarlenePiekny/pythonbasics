import os
import shutil


def is_existed_file(file_name: str):
    return os.path.isfile(file_name)


def create_directory(directory_name: str):
    current_path = os.getcwd()
    if not os.path.exists(current_path + "/" + directory_name):
        os.mkdir(current_path + "/" + directory_name)


def copy_file_into_new_directory(new_directory_name, existing_file_name):
    current_path = os.getcwd()
    if is_existed_file(existing_file_name):
        create_directory(new_directory_name)
        shutil.copy(current_path + "/" + existing_file_name,
                    current_path + "/" + new_directory_name + "/" + existing_file_name)


def main():
    assert is_existed_file("zoo.txt")
    copy_file_into_new_directory("dossier", "zoo.txt")


if __name__ == '__main__':
    main()
