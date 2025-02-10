import json
import os


def convert_to_jsonl(input_file, output_file):
    """
    Converts a JSON file (with a specific structure) to a JSONL file.

    Args:
        input_file: Path to the input JSON file.
        output_file: Path to the output JSONL file.
    """

    try:
        with open(
            input_file, "r", encoding="utf-8"
        ) as f_in:  # Handle potential encoding issues
            data = json.load(f_in)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{input_file}'.")
        return
    except Exception as e:  # Catch any other potential errors
        print(f"An unexpected error occurred while reading the input file: {e}")
        return

    try:
        with open(output_file, "w", encoding="utf-8") as f_out:
            for item in data:
                new_item = {
                    "instruction": item["instruction"],
                    "input": item["input"],
                    "output": item["output"],
                }
                f_out.write(
                    json.dumps(new_item, ensure_ascii=False) + "\n"
                )  # ensure_ascii=False for Korean
    except Exception as e:
        print(f"An unexpected error occurred while writing to the output file: {e}")
        return

    print(f"Successfully converted '{input_file}' to '{output_file}'.")


# Example usage:
input_filename = "regen.json"  # Replace with your input file name
output_filename = "output.jsonl"  # Replace with your desired output file name

convert_to_jsonl(input_filename, output_filename)
