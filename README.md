# Kidney Disease Classification

This project aims to classify kidney CT scan images into categories such as cyst, normal, tumor, or stone using deep learning and computer vision techniques.

The project is hosted on Azure, you can [click here](https://kidneydiseaseclassification.azurewebsites.net/) to visit the deployed project.

This project mainly utilizes following tools :

- Tensorflow and Keras
- MLFLOW and Dagshub for Experiment Tracking 
- DVC for pipeline versioning
- FastAPI for server
- Docker for containerization
- Azure for deployment

## Table of Contents

- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)

## Project Structure

The project follows a modular structure for better organization and maintainability. Here's an overview of the directory structure:

- `.github/workflows`: GitHub Actions workflows for CI/CD.
- `src/`: Source code directory.
  - `KidneyDiseaseClassifier/`
    - `components/`: Modules for different stages of the pipeline.
    - `utils/`: Utility functions.
    - `config/`: Configuration settings.
    - `pipeline/`: Scripts for pipeline stages.
    - `entity/`: Data entity classes.
    - `constants/`: Constants used throughout the project.
- `config/`: Configuration files.
- `trial_notebooks/`: Directory for trials and experiments in jupyter notebook.
- `app.py`: FastAPI server.
- `Dockerfile`: Docker configuration for containerization.
- `requirements.txt`: Project dependencies.
- `setup.py`: Setup script for installing the project.
- `main.py`: Main script for execution.

## Setup

To set up the project environment, follow these steps:

1. Clone this repository.
2. Install Python 3.8 and ensure pip is installed.
3. Install project dependencies using `pip install -r requirements.txt`.
4. Ensure Docker is installed if you intend to use containerization.

## Usage

### To directly run the complete Data ingestion, Model preparation and training and Model evaluation pipeline

run the command

```bash
dvc init
dvc repro
```

### To explicitly run each pipeline follow following commands-

#### Data Ingestion

To download and preprocess the dataset, run:

```bash
python src/KidneyDiseaseClassifier/pipeline/stage_01_data_ingestion.py
```

#### Model Preparation and Training

To train the model, execute:

```bash
python src/KidneyDiseaseClassifier/pipeline/stage_02_prepare_base_model.py
python src/KidneyDiseaseClassifier/pipeline/stage_03_training_model.py
```

#### Model Evaluation

To evaluate the trained model, run:

```bash
python src/KidneyDiseaseClassifier/pipeline/stage_04_evaluation.py
```

### To start the FastAPI server for making prediction :

Change the port to 8080 in the app.py file and then,

```bash
python app.py
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.

Please ensure that your contributions adhere to the project's coding standards and guidelines.
