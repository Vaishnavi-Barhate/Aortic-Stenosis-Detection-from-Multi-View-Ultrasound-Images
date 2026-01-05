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
We ran two full model runs. The (original_samil.ipynb) runs the SAMIL model defined in the paper. The modified_samil.ipynb runs SAMIL with added drop out layers.

We also added the balanced accuracy results and loss per epoch for each model run as well as the model checkpoint at the best balanced accurracy in here.

---

Running SAMIL with study-level pretraining, go to runs/SAMIL bash launch_experiment.sh run_here or use the custom setup.sh script provided

---

### Prepare Datasets
1. Download TMED2 from: https://TMED.cs.tufts.edu
2. Navigate to the `view_and_diagnosis_labeled_set` directory
3. Run the dataset organization script:

```bash
bash organize_tmed2.sh <labeled_dir> <unlabeled_dir> <output_dir>
