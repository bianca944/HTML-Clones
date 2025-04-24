# package init
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
import numpy as np

def compute_text_similarity(docs):
    texts = [doc['text'] for doc in docs]
    vectorizer = TfidfVectorizer().fit_transform(texts)
    similarity_matrix = cosine_similarity(vectorizer)
    return similarity_matrix

def compute_tag_similarity(doc1, doc2):
    # Convert tag counts to full vector (using union of all tags)
    all_tags = list(set(doc1['tag_freq'].keys()) | set(doc2['tag_freq'].keys()))
    vec1 = np.array([doc1['tag_freq'].get(tag, 0) for tag in all_tags])
    vec2 = np.array([doc2['tag_freq'].get(tag, 0) for tag in all_tags])
    
    # Cosine similarity
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return np.dot(vec1, vec2) / (norm1 * norm2 + 1e-10)

def compute_dom_structure_similarity(doc1, doc2):
    # Compare DOM paths using Jaccard similarity
    set1 = set(doc1['dom_structure'])
    set2 = set(doc2['dom_structure'])
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union != 0 else 0

def compute_combined_similarity(documents, weight_text=0.5, weight_dom=0.25, weight_tag=0.25):
    N = len(documents)
    sim_matrix = np.zeros((N, N))
    
    text_sim = compute_text_similarity(documents)
    
    for i in range(N):
        for j in range(i, N):
            dom_sim = compute_dom_structure_similarity(documents[i], documents[j])
            tag_sim = compute_tag_similarity(documents[i], documents[j])
            combined = (weight_text * text_sim[i][j] +
                        weight_dom * dom_sim +
                        weight_tag * tag_sim)
            sim_matrix[i][j] = sim_matrix[j][i] = combined
    return sim_matrix
