echo "split1"
python main_same_model.py --hidden_dim 512 --n_encoder_layer 4 --n_decoder_layer 2 \
    --n_query 20 --seg --task long --pos_emb --anticipate \
    --max_pos_len 3100 --sample_rate 6  --predict --mode=train --mamba True --split=$1 