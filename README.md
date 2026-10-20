# Python Programming for Artificial Intelligence — Assignment 2

This project follows Parts A–G of the assignment. It is kept in one folder to make it easy to open in VS Code.

## Files

- `Part_A_Python.ipynb` — Problems 1–4: functions, student dictionaries, CSV validation, and `MLDataset`.
- `Part_B_NumPy.ipynb` — Problems 5–7: arrays, matrices, min-max normalization, and z-score standardization.
- `Part_C_Pandas_EDA.ipynb` — Problems 8–10: dataset inspection, cleaning, analysis, visualizations, correlations, and five observations.
- `Part_D_Machine_Learning.ipynb` — Problems 11–15: regression, classification, clustering, model tuning, and saved prediction pipeline.
- `Part_E_PyTorch.ipynb` — Problems 16–18: tensors, autograd, Fashion-MNIST classifier, two learning-rate experiments, plots, and saved weights.
- `Part_F_TensorFlow.ipynb` — Problems 19–20: Keras classifier, saved/reloaded model, and measured framework comparison.
- `predict_saved_model.py` — separate command-line program for Problem 15.
- `app.py` — Streamlit prediction dashboard for Problem 21 (Option C).
- `requirements.txt` — pinned Python packages.
- `REPORT.md` — report structure and results checklist.

The notebooks create the saved models, graphs, metrics JSON files, and comparison CSV files as they run. These generated artifacts are intentionally not pre-filled with invented results.

## 1. Set up in VS Code on Windows

Install Python 3.11 (64-bit) and the Python and Jupyter extensions in VS Code.

1. Extract the ZIP file to a normal folder, for example `Documents\AI_Python_Assignment`.
2. Open that folder in VS Code.
3. Open **Terminal → New Terminal** and run:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation, run this once in the same terminal and activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

4. In VS Code, open a notebook and select the `.venv` Python interpreter as its kernel.
5. Run cells from top to bottom. The first run may take time because dependencies and datasets need to download.

If package installation fails due to a platform-specific PyTorch wheel, use the official PyTorch installation selector at https://pytorch.org/get-started/locally/ and keep the other versions from `requirements.txt`.

## 2. Recommended run order

1. `Part_A_Python.ipynb`
2. `Part_B_NumPy.ipynb`
3. `Part_C_Pandas_EDA.ipynb` — downloads `student-mat.csv` from UCI if it is not already present.
4. `Part_D_Machine_Learning.ipynb` — saves `student_grade_model.joblib` and creates ML graphs/results.
5. `predict_saved_model.py` — run with `python predict_saved_model.py` after Part D.
6. `Part_E_PyTorch.ipynb` — downloads Fashion-MNIST automatically through `torchvision`; trains two small experiments.
7. `Part_F_TensorFlow.ipynb` — trains the Keras model and compares actual results with the saved PyTorch metrics.
8. `app.py` — after Part D has saved the model, run `streamlit run app.py`.

For the Streamlit application, enter `Ctrl+C` in the terminal to stop the local server.

## 3. Datasets and attribution

- **Student Performance:** UCI Machine Learning Repository, Student Performance dataset: https://archive.ics.uci.edu/dataset/320/student+performance. The Mathematics file (`student-mat.csv`) is downloaded by the notebook if absent. The source CSV uses semicolon separators.
- **Fashion-MNIST:** Zalando Research Fashion-MNIST: https://github.com/zalandoresearch/fashion-mnist. The PyTorch and Keras libraries download the data into their own local caches. The experiments use fixed subsets to keep runtime manageable.

Internet access is required for the first download of these datasets. The CSV is not bundled in this ZIP because this environment could not retrieve the original file; the notebook downloads it from the original source when run on a connected laptop.

## 4. Important notes

- The student grade model predicts `G3` (0–20). For classification, pass/fail is defined as `G3 >= 10`; grade columns are excluded from classification features.
- The grade prediction model uses `studytime`, `failures`, `absences`, `G1`, and `G2`. The prediction script and app use the same feature order as the saved pipeline.
- The deep-learning notebooks use 10,000 training samples, 2,000 validation samples, and 2,000 test samples to make the experiments more manageable on a laptop. Report the actual results generated on your computer.
- Training time depends on CPU/GPU, package builds, and system load. The notebooks measure it rather than assuming a value.
- Do not claim the model is highly accurate or that one framework is universally better. Discuss the observed metrics and the dataset/sample limitations.
- The notebooks print the requested outputs and save relevant graphs/tables. Keep the generated model and result files in the same folder when running the script or app.
