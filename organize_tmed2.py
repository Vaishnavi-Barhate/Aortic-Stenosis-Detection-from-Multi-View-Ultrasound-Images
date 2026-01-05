#!/usr/bin/env python3
"""
Script to organize TMED2 dataset by putting labeled and unlabeled images 
for the same study under the same folder.

Usage:
    python organize_tmed2.py --labeled_dir <path_to_labeled_images> --unlabeled_dir <path_to_unlabeled_images> --output_dir <path_to_output>
"""

import os
import shutil
import argparse
import re
from pathlib import Path
from tqdm import tqdm

def extract_study_id(filename):
    """Extract study ID from filename (e.g., '1009s2_0.png' -> '1009s2')"""
    match = re.match(r'(.+?)_\d+\.png', filename)
    if match:
        return match.group(1)
    return None

def organize_dataset(labeled_dir, unlabeled_dir, output_dir):
    """
    Organize TMED2 dataset by putting labeled and unlabeled images 
    for the same study under the same folder.
    
    Args:
        labeled_dir: Directory containing labeled images
        unlabeled_dir: Directory containing unlabeled images
        output_dir: Output directory where organized dataset will be stored
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all labeled images and extract unique study IDs
    labeled_files = [f for f in os.listdir(labeled_dir) if f.endswith('.png')]
    study_ids = set()
    
    for filename in labeled_files:
        study_id = extract_study_id(filename)
        if study_id:
            study_ids.add(study_id)
    
    print(f"Found {len(study_ids)} unique studies in labeled dataset")
    
    # Create a directory for each study and copy labeled images
    for study_id in tqdm(study_ids, desc="Processing studies"):
        study_dir = os.path.join(output_dir, study_id)
        os.makedirs(study_dir, exist_ok=True)
        
        # Copy labeled images for this study
        for filename in labeled_files:
            if filename.startswith(f"{study_id}_"):
                src = os.path.join(labeled_dir, filename)
                dst = os.path.join(study_dir, filename)
                shutil.copy2(src, dst)
    
    # If unlabeled directory exists, copy unlabeled images to their respective study folders
    if os.path.exists(unlabeled_dir):
        unlabeled_files = [f for f in os.listdir(unlabeled_dir) if f.endswith('.png')]
        
        for filename in tqdm(unlabeled_files, desc="Processing unlabeled images"):
            study_id = extract_study_id(filename)
            if study_id and study_id in study_ids:
                study_dir = os.path.join(output_dir, study_id)
                src = os.path.join(unlabeled_dir, filename)
                dst = os.path.join(study_dir, filename)
                shutil.copy2(src, dst)
    else:
        print(f"Warning: Unlabeled directory '{unlabeled_dir}' not found")
    
    print(f"Dataset organization complete. Organized data saved to '{output_dir}'")

def main():
    parser = argparse.ArgumentParser(description='Organize TMED2 dataset')
    parser.add_argument('--labeled_dir', required=True, help='Directory containing labeled images')
    parser.add_argument('--unlabeled_dir', required=True, help='Directory containing unlabeled images')
    parser.add_argument('--output_dir', required=True, help='Output directory for organized dataset')
    
    args = parser.parse_args()
    
    organize_dataset(args.labeled_dir, args.unlabeled_dir, args.output_dir)

if __name__ == '__main__':
    main()
