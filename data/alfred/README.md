### Prepare Alfred Data for Indoor Detection

1. Download the alfred data and save the raw data in the directory `json_2.1.0`

2. Save the corresponding path of train, val and test data in the directory `meta_data`

3. Enter the project root directory, generate train, val and test data by running:

```python
python tools/create_data.py alfred --root-path ./data/alfred --out-dir ./data/alfred --extra-tag alfred
```

#### Structure
The directory structure after pre-processing should be as below

```
alfred
├── alfred_infos_test.pkl
├── alfred_infos_train.pkl
├── alfred_infos_val.pkl
├── alfred_instance_data
│   ├── xxxxx_bbox.npy
│   ├── xxxxx_label.npy
│   ├── xxxxx_vert.npy
├── alfred_pc.py
├── batch_load_alfred_data.py
├── batch_load.sh
├── json_2.1.0
├── load_alfred_data.py
├── meta_data
│   ├── train.txt
│   ├── valid_seen.txt
│   ├── valid_unseen.txt
│   ├── tests_seen.txt
│   ├── tests_unseen.txt
├── points
│   ├── xxxxx.bin
├── read_demo.py
├── README.md
```
