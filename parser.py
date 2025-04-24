# package init
from bs4 import BeautifulSoup
from collections import Counter
import os

def load_html(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return BeautifulSoup(file, 'lxml')

def extract_visible_text(soup):
    # Remove scripts/styles
    for tag in soup(['script', 'style', 'noscript']):
        tag.decompose()
    # Get all visible text
    return ' '.join(soup.stripped_strings)

def get_tag_frequencies(soup):
    tags = [tag.name for tag in soup.find_all()]
    return Counter(tags)

def get_dom_structure(soup, depth_limit=3):
    def traverse(node, depth):
        if depth > depth_limit or not hasattr(node, 'name'):
            return []
        structure = [node.name]
        for child in node.children:
            structure += traverse(child, depth + 1)
        return structure
    return traverse(soup.body if soup.body else soup, 0)

def parse_html_file(file_path):
    soup = load_html(file_path)
    text = extract_visible_text(soup)
    tags = get_tag_frequencies(soup)
    structure = get_dom_structure(soup)
    return {
        'path': file_path,
        'text': text,
        'tag_freq': tags,
        'dom_structure': structure
    }
