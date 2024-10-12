from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import pandas as pd
import shutil
import fitz
import os


def extract_abstract(file_path):
    """extract the abstract till the intro,conclusion,etc. part from each pdf file in the folder if there's no
    abstract for that file it'll return none and move to the next"""
    doc = fitz.open(file_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text("text")
    doc.close()
    text = text.lower()
    abstract_start = text.find("abstract")
    if abstract_start != -1:
        possible_endings = ["introduction", "method", "results", "conclusion"]
        abstract_end = len(text)
        for end_term in possible_endings:
            end_index = text.find(end_term, abstract_start)
            if end_index != -1 and end_index < abstract_end:
                abstract_end = end_index
        abstract = text[abstract_start:abstract_end].strip()
        word_limit = 300
        abstract_words = abstract.split()
        if len(abstract_words) > word_limit:
            abstract = ' '.join(abstract_words[:word_limit]) + "..."
        return abstract
    return None


# this is the file to put the pdfs that needs organizing
pdf_folder = "testing pdfs/"
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

abstract_list = []
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_folder, pdf_file)
    abstract = extract_abstract(pdf_path)
    if abstract:
        abstract_list.append((pdf_file, abstract))

# print(abstract_list)
#
# for pdf_file, abstract in abstract_list:
#     print(f"File: {pdf_file}\nAbstract: {abstract}\n")

"""as the 'extract_abstract' function returns a list of tuples each tuple contain (the pdf_file name, the abstract)
the following code is for separating them in order to convert the abstract to embeddings to prepare it
for clustering"""

# loading the model for embedding
model = SentenceTransformer("all-MiniLM-L6-v2")

abstracts = [item[1] for item in abstract_list]
pdf_filenames = [item[0] for item in abstract_list]
embeddings = model.encode(abstracts)
df = pd.DataFrame(embeddings)
df['filename'] = pdf_filenames


num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df['cluster'] = kmeans.fit_predict(embeddings)
# print(df[['filename', 'cluster']])
output_folder = "organized_pdfs"
os.makedirs(output_folder, exist_ok=True)

for cluster_num in df['cluster'].unique():
    cluster_folder = os.path.join(output_folder, f"Cluster_{cluster_num}")
    os.makedirs(cluster_folder, exist_ok=True)

    cluster_pdfs = df[df['cluster'] == cluster_num]['filename']
    for pdf_file in cluster_pdfs:
        src_path = os.path.join(pdf_folder, pdf_file)
        dst_path = os.path.join(cluster_folder, pdf_file)
        shutil.move(src_path, dst_path)

print("PDFs organized into clusters successfully!")
