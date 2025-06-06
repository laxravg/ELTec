# ELTec Spanish Corpus Analysis

## Project Overview
This repository contains the Spanish ELTec (European Literary Text Collection) corpus and related analysis. The project focuses on sentiment analysis of literary texts from Spain, specifically examining how different geographic locations are portrayed in Spanish literature from different time periods.

## Spanish_ELTec_Corpus
The Spanish ELTeC subcorpus consists of 87 XML-encoded literary texts from different time periods (1840-1920). Each text includes rich metadata such as author information, publication year, and word count.

### Data Structure
The folder contains 2 kind of files: 
- XML original ELTec files: Contains the original Spanish ELTec level 1 data
- Annotated files: Contains the annotated version of the corpus using spaCy, including part-of-speech tags and named entities. This type of files end with the suffix "_annotated.xml"

## Experiment files
The experiment files are the jupyter notebooks named "SentimentAnalysis.ipynb" and "All_instances.ipynb".

- The `SentimentAnalysis.ipynb` notebook was used to conduct experiments using only 30 of the instances that obtained the highest confidence score when analyzing the sentiment of the text window.

- The `All_instances` analysis includes results from all instances that mentioned one of the locations of interest. This was done in order to analyze how many times foreign location were mentioned across the corpus, not taking into account the confidence score of the sentiment classification.

## Methodology of the experiments
### Data Preprocessing
1. **Text Processing**:
   - The original ELTec files were processed using spaCy to extract the text and metadata. 
   - Applied POS and NER tagging using spaCy
   - Enhanced with "mrm8488/bert-spanish-cased-finetuned-ner" for improved entity recognition
   - Filtered for geographic locations of interest: America, Cuba, Philippines, Egypt, and Asia
   - Resulting files: annotated versions and the files within the "Name Entity Extraction" folder. 
        - entities_frequency.csv: shows the results using spaCY.
        - filtered_entities.csv: shows the results using the transformer model.
   

2. **Sentiment Analysis**:
   - Used tabularisai/multilingual-sentiment-analysis model
   - Extracted 100-token windows around each geographic mention
   - Analyzed sentiment with five categories, later collapsed to Positive/Negative
   - Retained top 30 results by confidence score for analysis
   - Resulting files: 
        - sentiment.csv: shows the results using the transformer model. 


3. **Visualization**:
    - Created 40 individual text files with semantically meaningful words
    - Applied TF-IDF filtering to remove common, uninformative terms
    - Generated word clouds for each location-sentiment-period combination

## Results
### Sentiment Analysis
- The `SentimentAnalysis.ipynb` notebook was used to conduct experiments on texts from countries with the highest confidence scores.
- The `All_instances` analysis includes results from all files in the ELTec subcorpus.

### Output Files
- `results/` directory contains:
  - Processed text windows (`.txt` files)
  - Word clouds visualization in the "WordCloud" folder

## Usage
To reproduce the analysis:
1. Navigate to the `SentimentAnalysis.ipynb` notebook
2. Follow the instructions in the notebook to process the data and generate results

## Requirements
- Python 3.x
- Jupyter Notebook
- Required Python packages (see `requirements.txt`):
  - spaCy
  - Transformers
  - WordCloud
  - NLTK
  - Pandas
  - Matplotlib

