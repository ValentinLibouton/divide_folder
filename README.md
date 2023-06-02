# Folder Division Utility

This utility allows you to divide a folder into multiple parts with equal volume distribution. It traverses all the files in the source folder, sorts them based on their file size in descending order, and then copies the files into different destination folders.

## Usage

```bash
python divide_folder.py source_folder destination_folder num_parts
```

- `source_folder`: Path to the source folder that you want to divide.
- `destination_folder`: Path to the destination folder where the divided parts will be stored.
- `num_parts`: Number of parts to divide the folder into.

The utility will create the specified number of destination folders in the destination folder and copy the files from the source folder to the destination folders in a balanced manner.

## Example

To divide the folder `/path/to/source_folder` into 2 parts and store them in the folder `/path/to/destination_folder`, you would run the following command:

```bash
python divide_folder.py /path/to/source_folder /path/to/destination_folder 2
```

This will create two destination folders named "part_1_of_2" and "part_2_of_2" in the `/path/to/destination_folder`. The files from the source folder will be distributed evenly between these two destination folders based on their file size.

## Dependencies

The utility requires the following dependencies:

- Python 3.x
- shutil

You can install the dependencies using pip:

```bash
pip install shutil
```
## License

This utility is licensed under ...