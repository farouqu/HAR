#!/bin/bash

models=('FCN' 'DCL')
datasets=('ucihar' 'shar' 'hhar')
rep=1
epochs=60
batch_size=128

for dataset in "${datasets[@]}"; do
    for model in "${models[@]}"; do
        echo "Running commands for dataset: $dataset, backbone: $model"
        
        python main.py --dataset "$dataset" --backbone "$model" --rep "$rep" --n_epoch "$epochs" --batch_size "$batch_size"

        echo "------------------------"
    done
done
