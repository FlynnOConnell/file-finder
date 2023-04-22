import concurrent.futures
import os
import time
from pathlib import Path
import json


def find_files_in_directory(directory, search_strings):
    nex_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.nex'):
                for arg in search_strings:
                    if arg in file:
                        nex_files.append(Path(root) / file)
                        break

    return nex_files


def find_nex_files(directory, *args):
    nex_files = {arg: [] for arg in args}

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(find_files_in_directory, subdir, args): subdir for
                   subdir in directory.glob('**/') if subdir.is_dir()}

        for future in concurrent.futures.as_completed(futures):
            subdir = futures[future]
            print(f"Searching in {subdir}")
            try:
                subdir_files = future.result()
                for file in subdir_files:
                    for arg in args:
                        if arg in file.name:
                            nex_files[arg].append(file)
            except Exception as e:
                print(f"Error processing {subdir}: {e}")

    return nex_files


def save_json():
    with open('C:\\Users\\dilorenzo\\Dropbox\\Lab\\SF\\Files', 'w') as f:
        json.dump(nex_files_dict, f)


def decode_filename(nexdict):
    filenames = {paradigm: [] for paradigm in nexdict.keys()}
    for paradigm, entry in nexdict.items():
        for file in entry:
            filenames[paradigm].append(file.name)
    return filenames


if __name__ == '__main__':
    dir = "R://"
    folder = Path(dir)
    search_strings = [
        'SCIN',
        'SFN']

    start_time = time.time()
    nex_files_dict = find_nex_files(folder, *search_strings)
    end_time = time.time()
    elapsed_time = end_time - start_time
    nex_files_names = decode_filename(nex_files_dict)
    save_json()
