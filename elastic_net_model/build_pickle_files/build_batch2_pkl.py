import pickle
from loadData import loadData

def main():
    b2_path = '../../data/2017-06-30_batchdata_updated_struct_errorcorrect.mat'
    batch2 = loadData(b2_path, 2)

    with open('../data/batch2.pkl','wb') as fp:
            pickle.dump(batch2, fp)

if __name__ == '__main__':
      main()