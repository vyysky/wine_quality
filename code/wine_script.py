dataset = 'rajyellow46/wine-quality'

KAGGLE_USERNAME = os.environ.get('KAGGLE_USERNAME')  
KAGGLE_KEY = os.environ.get('KAGGLE_KEY')

api = KaggleApi() 
api.authenticate()

datafile = api.dataset_list_files(dataset).files

datafile_name = str(datafile[0])

api.dataset_download_file(dataset, datafile_name, force=True)

print(f'Датасет загружен. \nИмя файла для чтения: datafile_name')