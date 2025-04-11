import kagglehub
import os

# Download latest version of FER2013 dataset
dataset_path = kagglehub.dataset_download("msambare/fer2013")
print("Path to dataset files:", dataset_path)

# Now extract and prepare data for training (if needed)
import pandas as pd

csv_file = os.path.join(dataset_path, "fer2013.csv")
df = pd.read_csv(csv_file)

print("Dataset loaded with shape:", df.shape)
