# AI CITY 2023: Tracked-Vehicle Retrieval by Natural Language Descriptions

This repository contains the 6th place submission to the AI City Challenge 2023, Challenge Track 2: Tracked-Vehicle Retrieval by Natural Language Descriptions.


## Prepare
1. Update the data path in the code by searching for 'your-path-to-data'.
2. Preprocess the dataset to generate `frames`, `motion maps`, and perform `NLP augmentation` by running::
```
bash prepare.sh
```
3. The directory structures in `data2023` and `checkpoints` are as follows：
```
.
├── checkpoints
│   ├── {MODEL_NAME}.pth
│   └── ...
├── extracted_feats
│   ├── img_lang_feat_{MODEL_NAME}.pth
│   └── ...
├── data2023
│   ├── train-tracks.json
│   ├── train-tracks_nlpaug.json    # Subject augmentation (Refer to scripts/deal_nlpaug.py)
│   ├── train-tracks_nlpaug_2.json  # Motion augmentation (Refer to scripts/deal_nlpaug_2.py)
│   ├── train-tracks_nlpaug_3.json  # Location augmentation (Refer to scripts/deal_nlpaug_3.py)
│   └── ...
└── spatial_feat
    ├── query_lang_embeds.pkl
    └── track_car_embeds.pkl
```

## Train

The configuration files can be found in the `configs` directory. To train different models, first set up the correct data path and then run:

```
bash train.sh
```

## Ensemble and Submit  
Copy or move the best model from the `logs` directory to the `checkpoints` directory by running:
```
cp ./logs/{MODEL_NAME}_{args}/checkpoint_best.pth ./checkpoints/{MODEL_NAME}.pth
```

Then run the following command to generate the submission file:
```
bash run/submit.sh
```

## Acknowledgement
Our approach is partially based on [AICITY2022_Track2_SSM](https://github.com/hbchen121/AICITY2022_Track2_SSM). We would like to express our gratitude for their outstanding work!