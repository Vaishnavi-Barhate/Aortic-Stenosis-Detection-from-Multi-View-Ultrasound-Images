export ROOT_DIR=$PWD
echo "Root Dir: $ROOT_DIR"
export DATA_INFO_DIR="$ROOT_DIR/data_info/"
echo "Data Info Dir: $DATA_INFO_DIR"
export DATA_DIR="$ROOT_DIR/data/"
echo "Data Dir: $DATA_DIR"
export CHECKPOINT_DIR="$ROOT_DIR/model_checkpoints/"
echo "Checkpoint Dir: $CHECKPOINT_DIR"

# Export Python Path so it can find the src module
export PYTHONPATH=$PYTHONPATH:$ROOT_DIR/src
echo "Python Path: $PYTHONPATH"

bash $ROOT_DIR/runs/SAMIL/launch_experiment.sh run_here