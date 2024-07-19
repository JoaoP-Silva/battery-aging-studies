import pickle
from loadData import loadData

def main():
    b3_path = '../../data/2018-04-12_batchdata_updated_struct_errorcorrect.mat'
    batch3 = loadData(b3_path, 3)

    with open('../data/batch3.pkl','wb') as fp:
            pickle.dump(batch3, fp)

if __name__ == '__main__':
      main()