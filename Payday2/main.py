#!/usr/bin/env python
from progress.bar import Bar
import requests, os, json

ABSO_PATH = os.path.dirname(__file__)
MASKS = json.loads("".join(open("data.json", "r").readlines()))

def file_exists(path, filename, supposed_length):
    filename += ".png"
    path_to_file = os.path.join(path, filename)
    if os.path.exists(path_to_file):
        if os.path.getsize(path_to_file) == supposed_length:
            return True
        # else:
        #     print(os.path.getsize(path_to_file))
        #     print(supposed_length)
    return False

def get_input(s, upper_bound):
    ui = input(s)
    try:
        ui = int(ui)
    except:
        pass
    while type(ui) != int or (ui < 0 or ui > upper_bound):
        ui = input(s)
        try:
            ui = int(ui)
        except:
            pass
    return ui

def download(mask_data=MASKS["Main Masks"]['Main Crew'], output_folder="Main Masks\Main Crew"):
    '''
    Downloads and saves images.\n
    Arguments: 
        mask_data: A dictionary with 3 items: 
            full_names: an array of all the filenames. These names will be used when saving the files.
            url_names: an array of all the name used in the url corresponding to the full names.
            size: a string indicating the total size of all the images.
        output_folder: The relative path to the output folder for saving all the images. The script will create the folder if it does not exist. 
    Returns:
        None
    '''

    num_of_files = len(mask_data["full_names"])
    size = mask_data["size"]
    selected_subcategory = "[" + output_folder.replace('\\', '] > [') + "]"
    ui = input(f"Are you sure you want to download {num_of_files} file(s) in {selected_subcategory}?\nAt least {size} of disk space is required. [y/n]? ")

    if ui in "Yy":
        path = os.path.join(ABSO_PATH, output_folder)
        if (not os.path.exists(path)):
            os.makedirs(path)

        for i in range(num_of_files):
            url_name = mask_data["url_names"][i]
            full_name = mask_data["full_names"][i]

            url = f"https://fbi.paydaythegame.com/img/masks/full/{url_name}_dif.png"
            
            res = requests.get(url, stream=True)
            
            already_exists = file_exists(path, full_name, int(res.headers['Content-Length']))
            can_download = res.status_code == 200
            chunk_size = 1024
            if not already_exists:
                if can_download:
                    try:
                        total = int(res.headers['Content-Length'])
                        with open(f"./{output_folder}/{full_name}.png", "wb") as f:
                            bar = Bar(f'[{i + 1: >3}/{num_of_files: >3}] {full_name: <30}', max=total, suffix='%(percent).1f%%')
                            
                            for data in res.iter_content(chunk_size):
                                bar.next(n=min(chunk_size, total))
                                f.write(data)
                                total -= chunk_size
                            bar.finish()
                    except:
                        print(f"Error while downloading {full_name}'s mask.")
                else:
                    print(f"Error while downloading {full_name}'s mask. Error code: {res.status_code}")
            else:
                print(f"[{i + 1: >3}/{num_of_files: >3}] {full_name: <30} |File exists, skipping download.")

if __name__ == "__main__":
    while (True):
        print("Select a category to download:")
        print("[0] Quit :(")
        for i, v in enumerate(MASKS):
            print(f"[{i + 1}] {v}")
        selected_cat = get_input("> ", len(MASKS)) - 1
        cat = list(MASKS.keys())
        print()

        if (selected_cat == -1):
            break
        
        while True:
            print(f"Select a sub-category in [{cat[selected_cat]}] to download:")
            print(f"[0] Back.")
            for i, v in enumerate(MASKS[cat[selected_cat]]):
                print(f"[{i + 1}] {v}")
            selected_subcat = get_input("> ", len(MASKS[cat[selected_cat]])) - 1
            subcat = list(MASKS[cat[selected_cat]].keys())
            print()

            if (selected_subcat == -1):
                break
                    
            mask_data = MASKS[cat[selected_cat]][subcat[selected_subcat]]
            output_folder = f"{cat[selected_cat]}\{subcat[selected_subcat]}"
            download(mask_data, output_folder)
            print()