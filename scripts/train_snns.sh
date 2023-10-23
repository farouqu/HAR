#!/bin/bash

models=('SFCN' 'SDCL' )
datasets=('ucihar' 'shar' 'hhar')
rep=2
epochs=60
batch_size=128

for dataset in "${datasets[@]}"; do
    for model in "${models[@]}"; do
        echo "Running commands for dataset: $dataset, backbone: $model"
        
        python main.py --dataset "$dataset" --backbone "$model" --n_epoch "$epochs" --batch_size "$batch_size" --lr "1e-3" --tau "0.75" --thresh "0.5"

        echo "------------------------"
    done
done
