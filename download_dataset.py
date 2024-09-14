from datasets import get_dataset


dataset_list = [
    'NCI1',
    'PROTEINS',
    'DD',
    'COLLAB',
    'IMDB-BINARY',
    'REDDIT-BINARY',
    'REDDIT-MULTI-5K']

for dataset_name in dataset_list:
    dataset = get_dataset(dataset_name, sparse=True, feat_str='deg+odeg100', root='data')
    print(dataset)
