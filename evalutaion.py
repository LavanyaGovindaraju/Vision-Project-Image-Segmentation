from sklearn import metrics
import torch
import numpy as np


#Calculating Confusion Matrix

	
#Calculating F1-score and jacard score
def evaluation_metrics(truth, pred):
	pred= torch.flatten(pred, start_dim=0, end_dim=1).detach().cpu().numpy()
	truth= torch.flatten(truth, start_dim=0, end_dim=1).detach().cpu().numpy()
	acc= metrics.accuracy_score(truth, pred)
	f1  = metrics.f1_score(truth, pred,average = 'micro')
	jacc = metrics.jaccard_score(truth ,pred, average = 'micro')
	sens = metrics.recall_score(truth ,pred, average = 'weighted')
	return acc,f1,jacc,sens
