# Python-File-Organizer

This Python script automatically sorts files in a specified directory into subfolders based on their file extensions.

## Features

*   Creates subfolders for "Documents," "Videos," and "Images" if they don't already exist.
*   Moves files with extensions `.pdf`, `.doc` to the "Documents" folder.
*   Moves files with extensions `.mp4`, `.mov` to the "Videos" folder.
*   Moves files with extensions `.png`, `.jpeg`, `.jpg` to the "Images" folder.
*   Handles potential errors during file moving, such as file access issues.
*   Provides informative output messages indicating which files have been moved and any errors encountered.

## Requirements

*   Python 3.x
*   No external libraries are required (uses built-in `os` and `shutil` modules).

## How to Use

1.  **Save the Code:** Save the provided Python code as a `.py` file (e.g., `file_sorter.py`).

2.  **Modify the Path:** Change the `path` variable at the beginning of the script to the absolute path of the directory you want to sort.

    ```python
    path = r"D:\Code\Sorting" # Replace with your directory path
    ```

    *   **Important Note for Windows Users:** Use raw strings (prefixed with `r`) for Windows paths to avoid issues with backslashes. For example: `r"C:\My\Files"`.

3.  **Run the Script:** Open a terminal or command prompt, navigate to the directory where you saved the script, and execute it using the following command:

    ```bash
    python file_sorter.py
    ```
