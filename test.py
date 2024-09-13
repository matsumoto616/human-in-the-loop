#%%
import json
import os
import sys
import shutil
from pathlib import Path

# %%
coco_path = Path(__file__).parent / "datasets" / "coco-2017"
annotation_path = coco_path / "annotations"

# %%
with open(annotation_path / "instances_train2017.json") as f:
    train_annotation = json.load(f)

with open(annotation_path / "instances_val2017.json") as f:
    val_annotation = json.load(f)

# %%
train_category_id2name = {
    cat["id"]: cat["name"]
    for cat in train_annotation["categories"]
}

train_category_id2supercategory = {
    cat["id"]: cat["supercategory"]
    for cat in train_annotation["categories"]
}

val_category_id2name = {
    cat["id"]: cat["name"]
    for cat in val_annotation["categories"]
}

val_category_id2supercategory = {
    cat["id"]: cat["supercategory"]
    for cat in val_annotation["categories"]
}

# %%
train_image_id2name = {
    img["id"]: img["file_name"]
    for img in train_annotation["images"]
}

val_image_id2name = {
    img["id"]: img["file_name"]
    for img in val_annotation["images"]
}

# %%
train_filename2category = {
    train_image_id2name[anno["image_id"]]: 
        train_category_id2name[anno["category_id"]]
    for anno in train_annotation["annotations"]
}

train_filename2supercategory = {
    train_image_id2name[anno["image_id"]]: 
        train_category_id2supercategory[anno["category_id"]]
    for anno in train_annotation["annotations"]   
}

val_filename2category = {
    val_image_id2name[anno["image_id"]]: 
        val_category_id2name[anno["category_id"]]
    for anno in val_annotation["annotations"]
}

val_filename2supercategory = {
    val_image_id2name[anno["image_id"]]: 
        val_category_id2supercategory[anno["category_id"]]
    for anno in val_annotation["annotations"]   
}
#%%
for cat in set(train_category_id2name.values()):
    os.makedirs(coco_path / "train" / cat)
    os.makedirs(coco_path / "val" / cat)

# for cat in set(category_id2supercategory.values()):
#     os.makedirs(coco_path / "train" / cat)
#     os.makedirs(coco_path / "val" / cat)

# %%
for filename in list(train_filename2category.keys()):
    if train_filename2category[filename] in ["airplane", "boat"]:
        path_src = coco_path / "train" / filename
        path_dst = coco_path / "train" / train_filename2category[filename] / filename
        shutil.move(path_src, path_dst)

# %%
for filename in list(val_filename2category.keys()):
    if val_filename2category[filename] in ["airplane", "boat"]:
        path_src = coco_path / "val" / filename
        path_dst = coco_path / "val" / val_filename2category[filename] / filename
        shutil.move(path_src, path_dst)
# %%
