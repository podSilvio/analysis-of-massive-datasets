# analysis-of-massive-datasets

This repository contains laboratory exercises for a course of the same name in the Faculty of Electrical Engineering and Computing, Zagreb. 

---

* The first exercise is the implementation of the *SimHash* algorithm used for the detection of near-duplicate (textual) documents. In `SimHash.py`, the identification of similar texts is be done by a sequential search of hashes of all texts, while In the `LSH.py`, the Locality Sensitive Hashing (LSH) technique is used

* The second exercise is the implementation of the *Park Chen Yu* algorithm used for finding frequent itemsets. Algorithm PCY is an upgrade of the Apriori algorithm and uses one more iteration through the dataset to find similar *candidates*. The implementation is located in `PCY.py`

* Other laboratory exercises which cannot be uploaded before the course is finished. That includes *collaborative filtering* and *node rank*
