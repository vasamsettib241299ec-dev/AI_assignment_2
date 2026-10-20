# Assignment-2 python programmes


## Files

- `part_A.ipynb` — Problems 1–4: functions, student dictionaries, CSV validation, and `MLDataset`.
- `part_B_NumPy.ipynb` — Problems 5–7: arrays, matrices, min-max normalization, and z-score standardization.
- `part_C_Pandas_EDA.ipynb` — Problems 8–10: dataset inspection, cleaning, analysis, visualizations, correlations, and five observations.
- `part_D_Machine_Learning.ipynb` — Problems 11–15: regression, classification, clustering, model tuning, and saved prediction pipeline.
- `part_E_PyTorch.ipynb` — Problems 16–18: tensors, autograd, Fashion-MNIST classifier, two learning-rate experiments, plots, and saved weights.
- `part_F_TensorFlow.ipynb` — Problems 19–20: Keras classifier, saved/reloaded model, and measured framework comparison.
- `predicted_model.py` — separate command-line program for Problem 15.
- `app.py` — Streamlit prediction dashboard for Problem 21 (Option C).
- `requirements.txt` — pinned Python packages.
- `Report.md` — report structure and results checklist.

The notebooks create the saved models, graphs, metrics JSON files, and comparison CSV files as they run. These generated artifacts are intentionally not pre-filled with invented results.


# Datasets and attribution

- **Student Performance:** UCI Machine Learning Repository, Student Performance dataset: https://archive.ics.uci.edu/dataset/320/student+performance. The Mathematics file (`student-mat.csv`) is downloaded by the notebook if absent. The source CSV uses semicolon separators.
- **Fashion-MNIST:** Zalando Research Fashion-MNIST: https://github.com/zalandoresearch/fashion-mnist. The PyTorch and Keras libraries download the data into their own local caches. The experiments use fixed subsets to keep runtime manageable.

Internet access is required for the first download of these datasets. The CSV is not bundled in this ZIP because this environment could not retrieve the original file; the notebook downloads it from the original source when run on a connected laptop.
