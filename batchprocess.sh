#!/bin/bash

# set output and error output filenames, %j will be replaced by Slurm with the jobid
#SBATCH -o testing%j.out
#SBATCH -e testing%j.err

# single node in the "short or defq" partition
#SBATCH -N 1
#SBATCH -p gpu
#SBATCH -t 3-00:00:00
#SBATCH --mail-user=mmann1123@gwu.edu
#SBATCH --mail-type=ALL


module load git-lfs
module load git/1.8.3.1

source activate /groups/manngroup/anaconda3-5.2.0_envs

cd /groups/manngroup/PiCameraClassifier/

python retrain.py --image_dir /groups/manngroup/StreetCaptureUpdate --flip_left_right True --random_brightness=20 \
--model_dir=tf_files/models/ --summaries_dir=tf_files/training_summaries/exception --output_graph=tf_files/retrained_graph.pb \
--output_labels=tf_files/retrained_labels.txt --bottleneck_dir=tf_files/bottlenecks 

