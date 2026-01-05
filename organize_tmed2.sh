#!/bin/bash
# Script to organize TMED2 dataset by putting labeled and unlabeled images 
# for the same study under the same folder.

# Check if required arguments are provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <labeled_dir> <unlabeled_dir> <output_dir>"
    echo "Example: $0 /path/to/view_and_diagnosis_labeled_set /path/to/unlabeled_set /path/to/organized_tmed2"
    exit 1
fi

LABELED_DIR="$1"
UNLABELED_DIR="$2"
OUTPUT_DIR="$3"

# Check if directories exist
if [ ! -d "$LABELED_DIR" ]; then
    echo "Error: Labeled directory '$LABELED_DIR' does not exist"
    exit 1
fi

if [ ! -d "$UNLABELED_DIR" ]; then
    echo "Warning: Unlabeled directory '$UNLABELED_DIR' does not exist"
fi

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

echo "Organizing TMED2 dataset..."
echo "Labeled directory: $LABELED_DIR"
echo "Unlabeled directory: $UNLABELED_DIR"
echo "Output directory: $OUTPUT_DIR"

# Run the Python script
python organize_tmed2.py --labeled_dir "$LABELED_DIR" --unlabeled_dir "$UNLABELED_DIR" --output_dir "$OUTPUT_DIR"

echo "Done!"
