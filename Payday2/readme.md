# Payday 2  
## Context:  
Payday 2 is a game I played from 2015 - 2017. Recently (2022) I found out there exists a page with almost every in-game image resources called [PAYDAY 2: FBI Files](https://fbi.paydaythegame.com/).  
This script is made to download all the in-game masks from that page, the categories are referenced from the official game fandom [PAYDAY Wiki | Masks](https://payday.fandom.com/wiki/Masks_(Payday_2)#Trivia).  
Some masks from the wiki are only available on consoles, which the FBI page do not have resources to download. The wiki also miss about < 20 masks that are available on the FBI page.  
## Script:  
#### Dependencies:  
Python 3.9  
Packages:  
* progress
#### How to run:  
Install all required packages with `pip install -r requirements.txt`.  
Run the script with `python main.py`.  
  
The script will present some categories for downloading, including:  
* 6 categories in the wiki page.  
* 1 category for all the masks, and the main crew's masks.  
* 1 category for the miscellaneous masks that are available on the FBI page but not on the wiki page, of which I cannot find the sources, or cannot classify into the other categories.  
```
Select a category to download:
[0] Quit :(
[1] Main Masks
[2] Community Masks
[3] Normal Masks
[4] DLC Masks
[5] Event Masks
[6] Collaboration Masks
[7] Infamous Masks
[8] Miscellaneous Masks
> 1
```
  
After selecting a category, it will ask for the sub-categories:  
```
Select a sub-category in [Main Masks] to download:
[0] Back.
[1] Main Crew
[2] All Masks
> 1
```
  
When the sub-category is selected, it will ask for confirmation to download and start the downloading process. All the folders and sub-folders are created automatically.  
The naming scheme of the masks is as follow:  
* For [Main Masks] > [Main Crew]: {crew_name} ({mask_name}).  
* For the masks in other categories (excluding those that intersect with the above category): {mask_name} ({source}). The source field is to avoid masks with the same name, for example "The Bullet" (Normal mask, or Enter the Gungeon Collaboration mask).   
```
Are you sure you want to download 22 file(s) in [Main Masks] > [Main Crew]?
At least 30.3 MB (31,776,494 bytes) of disk space is required. [y/n]? y
[  1/ 22] Bodhi                          |################################| 100.0%
[  2/ 22] Bonnie                         |################################| 100.0%
[  3/ 22] Chains                         |################################| 100.0%
[  4/ 22] Clover                         |################################| 100.0%
[  5/ 22] Dallas                         |################################| 100.0%
[  6/ 22] Dragan                         |################################| 100.0%
[  7/ 22] Duke                           |################################| 100.0%
[  8/ 22] Ethan                          |################################| 100.0%
[  9/ 22] Hila                           |################################| 100.0%
[ 10/ 22] Houston (Hoxton)               |################################| 100.0%
[ 11/ 22] Hoxton (Hoxton Reborns)        |################################| 100.0%
[ 12/ 22] Jacket (Richard Returns)       |################################| 100.0%
[ 13/ 22] Jimmy                          |################################| 100.0%
[ 14/ 22] Jiro                           |################################| 100.0%
[ 15/ 22] John Wick (Collateral)         |################################| 100.0%
[ 16/ 22] Joy                            |################################| 100.0%
[ 17/ 22] Rust                           |################################| 100.0%
[ 18/ 22] Sangres                        |################################| 100.0%
[ 19/ 22] Scarface                       |################################| 100.0%
[ 20/ 22] Sokol                          |################################| 100.0%
[ 21/ 22] Sydney                         |################################| 100.0%
[ 22/ 22] Wolf                           |################################| 100.0%
```
  
The script does check if the files exist, although sometimes the URL from the FBI page redirects to a different cache with a slightly different version of the file, and it will download the new version.  
```
Are you sure you want to download 22 file(s) in [Main Masks] > [Main Crew]?
At least 30.3 MB (31,776,494 bytes) of disk space is required. [y/n]? y
[  1/ 22] Bodhi                          |File exists, skipping download.
[  2/ 22] Bonnie                         |File exists, skipping download.
[  3/ 22] Chains                         |File exists, skipping download.
[  4/ 22] Clover                         |File exists, skipping download.
[  5/ 22] Dallas                         |File exists, skipping download.
[  6/ 22] Dragan                         |File exists, skipping download.
[  7/ 22] Duke                           |################################| 100.0%
[  8/ 22] Ethan                          |File exists, skipping download.
[  9/ 22] Hila                           |File exists, skipping download.
[ 10/ 22] Houston (Hoxton)               |File exists, skipping download.
[ 11/ 22] Hoxton (Hoxton Reborns)        |File exists, skipping download.
[ 12/ 22] Jacket (Richard Returns)       |File exists, skipping download.
[ 13/ 22] Jimmy                          |File exists, skipping download.
[ 14/ 22] Jiro                           |File exists, skipping download.
[ 15/ 22] John Wick (Collateral)         |File exists, skipping download.
[ 16/ 22] Joy                            |################################| 100.0%
[ 17/ 22] Rust                           |################################| 100.0%
[ 18/ 22] Sangres                        |File exists, skipping download.
[ 19/ 22] Scarface                       |File exists, skipping download.
[ 20/ 22] Sokol                          |File exists, skipping download.
[ 21/ 22] Sydney                         |File exists, skipping download.
[ 22/ 22] Wolf                           |File exists, skipping download.
```

