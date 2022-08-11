#!/usr/bin/python

import scanpy as sc
import anndata as ad
import numpy as np
import pandas as pd
import scipy.io as sci
import scipy as ss
import episcanpy.api as epi

#Commented out the functions that use epi.pp.lazy as I have now extrapolated the commands that combines and individually run them to remove tsne bottleneck

#from MulticoreTSNE import MulticoreTSNE as TSNE

mat = sci.mmread("mmtx/filtered_window_bc_matrix.mmtx.gz")
trans_mat = mat.transpose()
df = pd.DataFrame(trans_mat.toarray())
region_names = pd.read_table("mmtx/regions.names", header = None)
cell_names = pd.read_table("mmtx/cell.names", header = None)
df.columns=region_names[0]
df.index=cell_names[0]
adata = sc.AnnData(df)
adata.X = ss.sparse.csr_matrix(adata.X)
adata.var.index.name = 'region_names'
adata.obs.index.name = 'cell_names'
#tsne = TSNE(n_jobs=1)
#epi.pp.lazy(adata)
epi.pp.pca(adata)
epi.pp.neighbors(adata, method="umap")
epi.tl.umap(adata)
epi.pp.normalize_total(adata)
epi.pp.cal_var(adata, save='calculate_variability.pdf')
min_score_value = 0.515
nb_feature_selected = 120000
epi.pl.variability_features(adata,log=None, min_score=min_score_value, nb_features=nb_feature_selected, save='variability_features_plot.pdf')
epi.pl.variability_features(adata,log='log10', min_score=min_score_value, nb_features=nb_feature_selected, save='log_variability_features_plot.pdf')
adata = epi.pp.select_var_feature(adata, nb_features=nb_feature_selected, show=False, copy=True)
epi.tl.louvain(adata)
epi.tl.getNClusters(adata, n_cluster=14)
epi.tl.leiden(adata)
epi.tl.getNClusters(adata, n_cluster=14, method='leiden')
# umap has to be saved as .png as .pdf produces empty pdf files
epi.pl.umap(adata, color=['louvain', 'leiden'], wspace=0.4, save='.png')
adata.write("adata.h5ad", compression='gzip')
pd.DataFrame(adata.obs['louvain']).to_csv('Louvain.tsv', sep="\t", header=False)
pd.DataFrame(adata.obs['leiden']).to_csv('Leiden.tsv', sep="\t", header=False)
