#!/bin/bash

models=('FCN' 'DCL' 'LSTM' 'Transformer')
datasets=('ucihar' 'shar' 'hhar')
rep=2
epochs=30
batch_size=128

for dataset in "${datasets[@]}"; do
    for model in "${models[@]}"; do
        echo "Running commands for dataset: $dataset, backbone: $model"
        
        python main.py --dataset "$dataset" --backbone "$model" --rep "$rep" --n_epoch "$epochs" --batch_size "$batch_size"

        echo "------------------------"
    done
done
