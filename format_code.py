import autopep8
import sys

def format_code(file_path):
    """Formats the Python code in the given file using autopep8."""
    try:
        with open(file_path, 'r') as file:
            code = file.read()

        formatted_code = autopep8.fix_code(
            code,
            options={'aggressive': 1}
        )

        with open(file_path, 'w') as file:
            file.write(formatted_code)

        print(f"Formatted code in {file_path}")

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python format_code.py <file_path>")
    else:
        file_path = sys.argv[1]
        format_code(file_path)
