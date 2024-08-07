import h5pickle as h5py
import numpy as np
import pandas as pd
import pickle


path = '../../data/2017-05-12_batchdata_updated_struct_errorcorrect.mat'
f = h5py.File(path) 

batch = f['batch']
num_cells = batch['summary'].shape[0]

bat_dict = {}
for i in range(num_cells):
    cl = f[batch['cycle_life'][i,0]]
    summary_IR = np.hstack(f[batch['summary'][i,0]]['IR'][0,:].tolist())
    summary_QC = np.hstack(f[batch['summary'][i,0]]['QCharge'][0,:].tolist())
    summary_QD = np.hstack(f[batch['summary'][i,0]]['QDischarge'][0,:].tolist())
    summary_TA = np.hstack(f[batch['summary'][i,0]]['Tavg'][0,:].tolist())
    summary_TM = np.hstack(f[batch['summary'][i,0]]['Tmin'][0,:].tolist())
    summary_TX = np.hstack(f[batch['summary'][i,0]]['Tmax'][0,:].tolist())
    summary_CT = np.hstack(f[batch['summary'][i,0]]['chargetime'][0,:].tolist())
    summary_CY = np.hstack(f[batch['summary'][i,0]]['cycle'][0,:].tolist())
    summary = {'IR': summary_IR, 'QC': summary_QC, 'QD': summary_QD, 'Tavg':
                summary_TA, 'Tmin': summary_TM, 'Tmax': summary_TX, 'chargetime': summary_CT,
                'cycle': summary_CY}
    cycles = f[batch['cycles'][i,0]]
    cycle_dict = {}
    for j in range(cycles['I'].shape[0]):
        I = np.hstack((f[cycles['I'][j,0]]))
        Qc = np.hstack((f[cycles['Qc'][j,0]]))
        Qd = np.hstack((f[cycles['Qd'][j,0]]))
        Qdlin = np.hstack((f[cycles['Qdlin'][j,0]]))
        T = np.hstack((f[cycles['T'][j,0]]))
        Tdlin = np.hstack((f[cycles['Tdlin'][j,0]]))
        V = np.hstack((f[cycles['V'][j,0]]))
        dQdV = np.hstack((f[cycles['discharge_dQdV'][j,0]]))
        t = np.hstack((f[cycles['t'][j,0]]))
        cd = {'I': I, 'Qc': Qc, 'Qd': Qd, 'Qdlin': Qdlin, 'T': T, 'Tdlin': Tdlin, 'V':V, 'dQdV': dQdV, 't':t}
        cycle_dict[str(j)] = cd
    
    cell_dict = {'cycle_life': cl, 'summary': summary, 'cycles': cycle_dict}
    key = f'b1c' + str(i)
    bat_dict[key] = cell_dict

with open('batch1.pkl','wb') as fp:
    pickle.dump(bat_dict, fp)