import os

def get_all_html_files(directory):
    # Căutăm fișierele HTML în directorul curent
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.html')]
    print(f"Fișiere găsite: {files}")  # Afișează fișierele găsite pentru debug
    return files

def main(input_folder):
    # Obținem fișierele HTML din directorul specificat
    files = get_all_html_files(input_folder)
    print(f"Găsite {len(files)} fișiere HTML.")
    if not files:
        print("Nu au fost găsite fișiere HTML în folderul specificat.")
        return

    # Continuăm cu procesul de comparare a fișierelor (codul tău existent)
    documents = [parse_html_file(file) for file in files]
    similarity_matrix = compute_combined_similarity(documents)
    group_documents(similarity_matrix, files)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Detectează pagini HTML similare.')
    parser.add_argument('input_folder', help='Calea către folderul cu fișiere HTML')
    args = parser.parse_args()
    main(args.input_folder)
