import os
import shutil
import argparse


def traverse_files(folder_path):
    file_list = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            relative_path = os.path.relpath(file_path, folder_path)
            file_info = [relative_path, file, file_size]
            file_list.append(file_info)

    sorted_file_list = sorted(file_list, key=lambda x: x[2], reverse=True)
    return sorted_file_list


def copy_files_to_destination(sorted_file_list, destination_folder, num_parts, args):
    destination_folders = [os.path.join(destination_folder, f"part_{i + 1}_of_{num_parts}") for i in range(num_parts)]
    destination_sizes = [get_folder_size(folder) for folder in destination_folders]

    for file_info in sorted_file_list:
        source_relative_path, file_name, file_size = file_info
        destination_index = min(range(num_parts), key=destination_sizes.__getitem__)
        destination_folder_path = destination_folders[destination_index]
        destination_file_path = os.path.join(destination_folder_path, source_relative_path)
        os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)
        shutil.copy2(os.path.join(args.source_folder, source_relative_path), destination_file_path)
        destination_sizes[destination_index] += file_size


def create_destination_folders(destination_folder, num_parts):
    for i in range(num_parts):
        folder_name = f"part_{i + 1}_of_{num_parts}"
        folder_path = os.path.join(destination_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)


def get_folder_size(folder):
    total_size = 0
    for dirpath, _, filenames in os.walk(folder):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size


def main():
    parser = argparse.ArgumentParser(description='Divide a folder into multiple parts with equal volume distribution')
    parser.add_argument('source_folder', help='Path to the source folder')
    parser.add_argument('destination_folder', help='Path to the destination folder')
    parser.add_argument('num_parts', type=int, help='Number of parts to divide the folder into')
    args = parser.parse_args()

    create_destination_folders(args.destination_folder, args.num_parts)
    sorted_file_list = traverse_files(args.source_folder)
    copy_files_to_destination(sorted_file_list, args.destination_folder, args.num_parts, args)


if __name__ == '__main__':
    main()
