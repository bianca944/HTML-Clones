print("HTML Clone")
import os
import argparse
from clone_grouper.parser import parse_html_file
from clone_grouper.similarity import compute_combined_similarity
from clone_grouper.clustering import group_documents

def get_all_html_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.html')]

def main(input_folder):
    files = get_all_html_files(input_folder)
    print(f"Found {len(files)} HTML files in '{input_folder}'")

    documents = [parse_html_file(file) for file in files]
    similarity_matrix = compute_combined_similarity(documents)
    clusters = group_documents(similarity_matrix)

    # Map index back to file names
    grouped_files = [[documents[idx]['path'] for idx in group] for group in clusters]

    print("\nGrouped documents:")
    for group in grouped_files:
        print(group)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_folder', help='Path to folder containing HTML files')
    args = parser.parse_args()
    main(args.input_folder)
