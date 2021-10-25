import pandas as pd
import os


files = os.listdir('../Data_files/Scraped_data/Individual_Files/')

combined_csv = pd.concat([pd.read_csv('../Data_files/Scraped_data/Individual_Files/' + f) for f in files])
combined_csv.to_csv('../Data_files/Scraped_data/all_professions.csv', index=False, encoding='utf-8')
