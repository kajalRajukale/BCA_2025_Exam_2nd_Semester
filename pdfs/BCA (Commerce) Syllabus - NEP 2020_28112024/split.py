import os

def split_markdown_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    output_dir = os.path.join(os.path.dirname(input_file), 'chapters')
    os.makedirs(output_dir, exist_ok=True)

    current_file = None
    current_file_name = None

    for line in lines:
        if line.startswith('## '):
            if current_file:
                current_file.close()

            current_file_name = line.strip().replace(' ', '_').replace('##_', '') + '.md'
            current_file_path = os.path.join(output_dir, current_file_name)

            if os.path.exists(current_file_path):
                base_name, ext = os.path.splitext(current_file_name)
                counter = 1
                while os.path.exists(current_file_path):
                    current_file_name = f"{base_name}_{counter}{ext}"
                    current_file_path = os.path.join(output_dir, current_file_name)
                    counter += 1
                
            current_file = open(current_file_path, 'w')
        if current_file:
            current_file.write(line)

    if current_file:
        current_file.close()

if __name__ == "__main__":
    input_file = '/Users/ralphg/Desktop/C4B/Kajal/BCA/BCA (Commerce) Syllabus - NEP 2020_28112024/Semester II.md'
    split_markdown_file(input_file)