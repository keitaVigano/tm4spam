# TM4SPAM

## 1. System Requirements

- **Language**: Python
- **Platform**: Google Colab (recommended) or Local Environment
- **Libraries**: Managed via [Poetry](https://python-poetry.org/) (recommended for local execution)

For local usage, this project uses **Poetry** to manage the environment and dependencies. All required packages are declared in the `pyproject.toml` file, ensuring consistency and reproducibility across systems.

To install and activate the environment locally:

```bash
poetry install
poetry shell
```
## 2. Project Structure

```
├── data/
│   └── splits/
│       ├── train.csv                     # Cleaned training set
│       ├── test.csv                      # Cleaned test set
│       └── raw/
│           ├── train_raw.csv             # Raw version of training data
│           └── test_raw.csv              # Raw version of test data
│
├── models/                               # Folder for saving trained models
│
├── notebooks/
│   ├── classification.ipynb              # Classification workflow for logistic (TF-IDF, embeddings)
│   ├── classification_bert.ipynb         # Classification using DistilBERT
│   ├── compare_classification.ipynb      # Compare multiple classification models
│   ├── preprocessing.ipynb               # Data loading and preprocessing
│   └── topic_modeling.ipynb              # Topic modeling with Berttopic
│
├── report/
│   ├
│
├── src/
│   ├── __init__.py                       # Python module initializer
│   ├── preprocessing.py                  # Script for data preprocessing
│   └── setup_nltk.py                     # Script to download NLTK resources
│
├── pyproject.toml                        # Project dependencies and config (Poetry)
├── poetry.lock                           # Exact package versions locked by Poetry
├── LICENSE                               # Project license
├── .gitignore                            # Git ignore rules
└── README.md                             # Project documentation
```

## 3. Data, Models
The dataset used for this project is the **All-Scam-Spam** collection, which contains a wide range of scam and spam text samples. It is publicly available on Hugging Face and can be accessed at the following link:
https://huggingface.co/datasets/FredZhang7/all-scam-spam

For the classification task, we fine-tuned the **DistilBERT** model on this dataset. The fine-tuned model has been uploaded to the Hugging Face and is available at:
https://huggingface.co/cornualghost/tm4spam-distilbert

## 4. How to Run
- Open the desired notebook on **Google Colab**.
- Execute all cells sequentially.
- Required data and dependencies are loaded within the notebooks using pre-defined Google Drive links.

## 5. Local Usage (Optional)

To run the project locally, follow these steps:

1. **Download or clone the repository** to your local machine.

2. **Install dependencies using Poetry**:
   ```bash
   poetry install
   ```

3. **Activate the virtual environment**:
   ```bash
   poetry shell
   ```

4. **Run the notebooks manually** using your preferred environment (e.g., JupyterLab, VS Code).

## 6. Notes

To reproduce the full workflow, it is recommended to execute the notebooks in the following order:

1. `preprocessing.ipynb` – Load and preprocess the dataset.
2. `classification.ipynb` – Perform baseline classification using traditional methods (e.g., TF-IDF, word embeddings).
3. `classification_bert.ipynb` – Fine-tune and evaluate the DistilBERT model.
4. `compare_classification.ipynb` – Compare the performance of the different classification approaches.
5. `topic_modeling.ipynb` – Apply topic modeling (e.g., LDA) to explore the semantic structure of the text data.