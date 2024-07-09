import os
import zipfile
import gdown
import shutil
from sklearn.model_selection import train_test_split
from KidneyDiseaseClassifier import logger
from KidneyDiseaseClassifier.utils.common import get_size
from KidneyDiseaseClassifier.entity.config_entity import DataIngestionConfig
from KidneyDiseaseClassifier.utils.common import create_directories


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_file(self)-> str:
        '''
        Fetch data from the url
        '''

        try: 
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            
            gdown.download(prefix+file_id,zip_download_dir)
            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")
        except Exception as e:
            raise e
        
    

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            
            
    def split_data(self, test_size=0.2):
        """
        Split data into training and testing sets
        """
        data_dir = os.path.join(self.config.unzip_dir, "CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone")
        train_dir = os.path.join(self.config.unzip_dir, 'train')
        test_dir = os.path.join(self.config.unzip_dir, 'test')

        create_directories([train_dir, test_dir])

        for category in ['Stone', 'Cyst', 'Tumor', 'Normal']:
            category_path = os.path.join(data_dir, category)
            images = os.listdir(category_path)

            train_images, test_images = train_test_split(images, test_size=test_size, random_state=42)

            # Copy images to train and test directory
            train_category_path = os.path.join(train_dir, category)
            test_category_path = os.path.join(test_dir, category)
            create_directories([train_category_path, test_category_path])
            
            for img in train_images:
                shutil.move(os.path.join(category_path, img), os.path.join(train_category_path, img))

            for img in test_images:
                shutil.move(os.path.join(category_path, img), os.path.join(test_category_path, img))
