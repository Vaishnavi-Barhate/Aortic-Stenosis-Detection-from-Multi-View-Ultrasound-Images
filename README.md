This repository presents an independent reproduction of a deep learning pipeline for detecting **Aortic Stenosis (AS)** from **multi-view echocardiogram (ultrasound) images**.

The project is inspired by the methodology introduced in the MLHC 2023 paper on **Supervised Attention-based Multiple Instance Learning (MIL)**. The focus of this work is on **reproducibility, dataset restructuring, and experimental analysis**, rather than exact numerical replication. This project was completed as part of **CS 598 – Deep Learning for Healthcare**.

---

Diagnosing aortic stenosis using echocardiography is challenging because:
- Each patient study contains multiple ultrasound images from different views
- Labels are available only at the study level, not per image
- Individual views contribute unequally to diagnosis

To address these challenges, this project applies **attention-based Multiple Instance Learning (MIL)** to learn which views are most relevant for study-level diagnosis.

---

## Results
We ran two full model runs:
- **[original_samil.ipynb](original_samil.ipynb)** runs the SAMIL model defined in the paper
- **[modified_samil.ipynb](modified_samil.ipynb)** runs SAMIL with added dropout layers

We also added the **balanced accuracy results**, **loss per epoch**, and the **model checkpoint at the best balanced accuracy** for each run.

---

## Running Experiments
To run SAMIL with study-level pretraining:
- Navigate to **[runs/SAMIL](runs/SAMIL/)**
- Run the experiment script:  
  **[launch_experiment.sh](runs/SAMIL/launch_experiment.sh)**  
- Or use the custom setup script:  
  **[setup.sh](setup.sh)**

---

## Prepare Datasets
1. Download TMED2 from: https://TMED.cs.tufts.edu
2. Navigate to the `view_and_diagnosis_labeled_set` directory
3. Run the dataset organization script:

```bash
bash organize_tmed2.sh <labeled_dir> <unlabeled_dir> <output_dir>
