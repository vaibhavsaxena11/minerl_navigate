# MineRL Navigate Video Dataset

## Working with this dataset

### Install

To install using pip, run:
```
$ python3.7 -m pip install minerl-navigate
```

Alternatively, to install from source: Clone the git repository and, from its root, run:
```
minerl_navigate$ python3.7 -m pip install .
```

**Note:** This package installs tensorflow and tensorflow-datasets as dependencies. If upgrading these will affect any of your current installations, we recommend installing minerl-navigate in a virtual environment.

### How to use?

```
import tensorflow_datasets as tfds
import minerl_navigate

# Load dataset.
dataset = tfds.load("minerl_navigate", data_dir='/path/for/data/download/', shuffle_files=True)
# Data will be downloaded to provided data_dir (first-time only).
...
```
`dataset` has the following structure:
```
{
    'test': <PrefetchDataset shapes: {video: (None, 64, 64, 3)}, types: {video: tf.uint8}>,
    'train': <PrefetchDataset shapes: {video: (None, 64, 64, 3)}, types: {video: tf.uint8}>
}
```

## About

The MineRL dataset was crowd sourced by Guss et al. (2019) for reinforcement learning applications. The dataset shows human players traveling to goal coordinates in procedurally generated 3D worlds of the video game Minecraft, traversing forests, mountains, villages, and oceans.

To create a video prediction dataset, we combined the human demonstrations for the `Navigate` and `Navigate Extreme` tasks and split them into non-overlapping sequences of length 500. The dataset contains 961 training videos and 225 test videos as individual MP4 files. Additional metadata is stored in JSON format and contains the actions taken by the players in the game and the angle between the forward direction and the direction to the goal.

**References:**

```
@misc{saxena2021clockworkvae,
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
