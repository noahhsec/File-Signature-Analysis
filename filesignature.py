import magic
import sys

def identify_file_type(file_path):
    try:
        magic_obj = magic.Magic()
        file_type = magic_obj.from_file(file_path)
        return file_type
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python filesignature.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    file_type = identify_file_type(file_path)

    if file_type:
        print(f"File type: {file_type}")
    else:
        print("Unable to determine file type.")
