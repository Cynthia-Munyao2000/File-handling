def convert_to_uppercase(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as file:
            content = file.read()  # Read the entire content of the file

        # Convert the content to uppercase
        content_uppercase = content.upper()

        # Open the output file in write mode to save the uppercase content
        with open(output_filename, 'w') as new_file:
            new_file.write(content_uppercase)  # Write the uppercase content to the new file

        print(f"Content successfully converted to uppercase and written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = "input.txt"
output_file = "output.txt"

convert_to_uppercase(input_file, output_file)
