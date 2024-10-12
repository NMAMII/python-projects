# AutoClusterPDFs 

## Overview

**PDFClusterAI** is an AI-powered tool that organizes research papers (PDFs) into clusters based on their abstract content. By leveraging **Sentence Transformers** for generating embeddings and **K-Means** clustering, it automatically groups the PDFs by topic or content similarity. This tool helps researchers or students to efficiently categorize and manage their research papers.

## Features

- **Automatic Abstract Extraction**: Extracts the abstract section from research papers.
- **Text Embedding using AI**: Converts the abstract into meaningful embeddings using pre-trained models.
- **K-Means Clustering**: Clusters the PDFs into groups based on their abstract content.
- **Automatic Folder Organization**: Moves the PDFs into corresponding cluster folders.
  
## Dependencies

- Python 3.x
- `fitz` (PyMuPDF)
- `sentence-transformers`
- `sklearn`
- `pandas`
- `shutil`
  
Install dependencies using:

```bash
pip install sentence-transformers scikit-learn pandas pymupdf
```
## How It Works
- Abstract Extraction: The script extracts the abstract section of each PDF by identifying the position of the word "abstract" and trims it until the start of a common section like "Introduction" or "Methods."
- Text Embedding: The abstracts are converted into numerical embeddings using a pre-trained model from SentenceTransformers.
- Clustering: K-Means clustering is applied on the embeddings to group similar papers into a specified number of clusters.
- Organizing PDFs: The PDFs are moved to separate folders named by their cluster number, allowing you to easily navigate through related papers.
## Usage
Place your research papers (PDFs) in the testing pdfs/ folder.
Run the script to extract abstracts, cluster the PDFs, and automatically organize them into folders based on their clusters.
