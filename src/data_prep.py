# Daten aus Kaggle laden
%pip install kagglehub
# Imports

import os
import kagglehub
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

download_path = kagglehub.dataset_download("gokulraja84/emails-dataset-for-spam-detection")
csv_file_path = os.path.join(download_path, 'Emails.csv')
raw_df = pd.read_csv(csv_file_path)

# doppelte Daten entfernen
raw_unique_df = raw_df.drop_duplicates(subset=['text'], keep='first').copy()
print(f"Größe raw_df: {len(raw_df)} Zeilen")
print(f"Größe raw_unique_df: {len(raw_unique_df)} Zeilen")

# Konvertierung der label zu 0 und 1
all_df = raw_unique_df.copy()
all_df['label'] = (all_df['spam']).astype(int)
all_df = all_df.drop('spam', axis=1)
display(all_df)

# Aufteilung in train_df und validation_df

RANDOM_SEED = 42 # für Reproduzierbarkeit
SHARE_TEST = 0.2

# train- und Testdaten aufteilen
train_full_df, test_df = train_test_split(
    all_df,
    test_size = 0.2, # 20 prozent
    random_state=RANDOM_SEED,
    stratify=all_df['label']
)

# train und validation aus train full aufteilen
train_df, validation_df = train_test_split(
    train_full_df,
    test_size = 0.25, #also 20 prozent, da 25% von 80%
    random_state=RANDOM_SEED,
    stratify=train_full_df['label']
)

# index reset
train_df.reset_index(drop=True, inplace=True)
validation_df.reset_index(drop=True, inplace=True)
test_df.reset_index(drop=True, inplace=True)


print(f"Größe von train_df: {len(train_df)} Zeilen")
print(f"Größe von validation_df: {len(validation_df)} Zeilen")
print(f"Größe von test_df: {len(test_df)} Zeilen")

# Trainingsdaten und Validationdaten ausgeben
print('Trainingsdaten')
display(train_df)
print('Validationdaten')
display(validation_df)

# EDA

sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))
ax = sns.countplot(x='label', data=all_df, hue='label', palette='viridis')

# Balkenbeschriftung
plt.title('Verteilung der E-Mails')
plt.xlabel('Klasse')
plt.ylabel('Anzahl E-Mails')
plt.xticks([0,1],

            ['Nicht-Spam', 'Spam'] )

plt.show()



