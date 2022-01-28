# testing_episcanpy
Testing Episcanpy clustering for potential pipeline use

Singularity file could not be stored in repo due to size however can be recreated from Dockerfile using:
https://stackoverflow.com/questions/60314664/how-to-build-singularity-container-from-dockerfile

The script tests the speed and memory usage of episcanpy when running a conventional RNA seq pipeline.
Steps include:
       
       Reading in data and manipulating it.
       Converting data to anndata.
       Normalising data.
       Calculating variability of features.
       Clustering.
       Visualising.
       Multicore processing 
       (tsne function is used as an underlying feature in epi.pp.lazy even setting value to 1 increases speed).
 
 
The clustering data is saved to tsv and variability plots outputted as pdfs.
