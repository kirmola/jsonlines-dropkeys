import jsonlines

def remove_keys_from_jsonl(input_file, output_file, keys_to_remove):
    """Remove specified keys from a JSONL file."""
    with jsonlines.open(input_file, 'r') as reader, jsonlines.open(output_file, 'w') as writer:
        for obj in reader:
            for key in keys_to_remove:
                obj.pop(key, None)  # Remove key if it exists
            writer.write(obj)

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Remove specified keys from a JSONL file.")
    parser.add_argument("input_file", help="Path to input JSONL file")
    parser.add_argument("output_file", help="Path to output JSONL file")
    parser.add_argument("--keys", nargs="+", required=True, help="Keys to remove")

    args = parser.parse_args()

    remove_keys_from_jsonl(args.input_file, args.output_file, args.keys)
    print(f"Processed file saved to: {args.output_file}")
