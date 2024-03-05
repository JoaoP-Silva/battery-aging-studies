import pickle
from loadData import loadData

def main():
    b1_path = '../data/2017-05-12_batchdata_updated_struct_errorcorrect.mat'
    batch1 = loadData(b1_path, 1)

    with open('../data/batch1.pkl','wb') as fp:
            pickle.dump(batch1, fp)

if __name__ == '__main__':
      main()