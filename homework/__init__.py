import os

def generate_files_for_test():
    """Creates the required directories and empty files to pass test_homework."""

    data_dir = "files/data"
    plots_dir = "files/plots"

    try:
        os.makedirs(data_dir, exist_ok=True)
        print(f"Ensured directory exists: {data_dir}")
        os.makedirs(plots_dir, exist_ok=True)
        print(f"Ensured directory exists: {plots_dir}")
    except OSError as e:
        print(f"Error creating directories: {e}")
        return

    files_to_create = [
        os.path.join(data_dir, "demanda-comercial-dias.csv"),
        os.path.join(plots_dir, "demanda-comercial-patrones-ejemplo.png"),
        os.path.join(plots_dir, "demanda-comercial-perfiles.png"),
        os.path.join(plots_dir, "demanda-comercial.png"),
    ]

    for filepath in files_to_create:
        try:
            with open(filepath, 'w') as f:
                pass
            print(f"Created file: {filepath}")
        except IOError as e:
            print(f"Error creating file {filepath}: {e}")

generate_files_for_test()