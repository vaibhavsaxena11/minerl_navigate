# MineRL Navigate Video Dataset

A dataset for long-term video prediction. It shows human players traversing
worlds of the video game Minecraft, which include forests, mountains, oceans,
and islands. The dataset contains 961 train videos and 255 test videos. Each
video contains 500 images of size 64x64x3.

## Citation

The dataset was originally crowd-sourced by Guss et al. and preprocessed for
video prediction by Saxena et al. If you use this dataset, please reference:

```
@article{saxena2021clockworkvae,
  title={Clockwork Variational Autoencoders},
  author={Saxena, Vaibhav and Ba, Jimmy and Hafner, Danijar},
  journal={arXiv preprint arXiv:2102.09532},
  year={2021},
}
```

```
@article{guss2019minerl,
  title={Mine{RL}: A Large-Scale Dataset of {M}inecraft Demonstrations},
  author={William H. Guss and Houghton, Brandon and Topin, Nicholay and Wang, Phillip and Codel, Cayden and Veloso, Manuela and Salakhutdinov, Ruslan},
  journal={International Joint Conference on Artificial Intelligence},
  year={2019},
}
```

## Instructions

Installation:

```sh
pip3 install minerl-navigate
```

Usage example:

```python
import tensorflow as tf
import tensorflow_datasets as tfds
import minerl_navigate

dataset = tfds.load('minerl_navigate', shuffle_files=True)

test = dataset['test']

train = dataset['train'].repeat()
train = train.flat_map(lambda x: tf.data.Dataset.from_tensor_slices(
    tf.reshape(x['video'], (5, 100, 64, 64, 3))))
train = train.shuffle(5000).batch(50).prefetch(1)

for batch in train:
  assert batch.shape == (50, 100, 64, 64, 3)
  assert batch.dtype == tf.uint8
  break
```

## Creation

The video dataset was created by combining the *Navigate* and *Navigate
Extreme* tasks, splitting them into non-overlapping sequences of length 500,
splitting them into train and test sets, and storing the videos as MP4 files.
Optionally, the action sequences are available in JSON format. Instead of using
the data loader, the data can also be [downloaded][download] manually.

[download]: https://archive.org/details/minerl_navigate
