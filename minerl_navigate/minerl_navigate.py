"""minerl_navigate dataset."""

import tensorflow as tf
import tensorflow_datasets as tfds

import numpy as np

_DESCRIPTION = """
# MineRL Navigate Video Dataset

The MineRL dataset was crowd sourced by Guss et al. (2019) for reinforcement learning applications. The dataset shows human players traveling to goal coordinates in procedurally generated 3D worlds of the video game Minecraft, traversing forests, mountains, villages, and oceans.

To create a video prediction dataset, we combined the human demonstrations for the `Navigate` and `Navigate Extreme` tasks and split them into non-overlapping sequences of length 500. The dataset contains 961 training videos and 225 test videos as individual MP4 files. Additional metadata is stored in JSON format and contains the actions taken by the players in the game and the angle between the forward direction and the direction to the goal.

References:

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
"""

_CITATION = """
@misc{saxena2021clockwork,
      title={Clockwork Variational Autoencoders}, 
      author={Vaibhav Saxena and Jimmy Ba and Danijar Hafner},
      year={2021},
      eprint={2102.09532},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
"""

_DOWNLOAD_URL = "https://archive.org/download/minerl_navigate/minerl_navigate.zip"


class MinerlNavigate(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for minerl_navigate dataset."""

    VERSION = tfds.core.Version("1.0.0")
    RELEASE_NOTES = {
        "1.0.0": "Initial release.",
    }

    def _info(self) -> tfds.core.DatasetInfo:
        """Returns the dataset metadata."""
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict(
                {
                    "video": tfds.features.Video(shape=(None, 64, 64, 3)),
                }
            ),
            supervised_keys=None,
            homepage="https://archive.org/details/minerl_navigate",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        """Returns SplitGenerators."""
        path = dl_manager.download_and_extract(_DOWNLOAD_URL)

        return {
            "train": self._generate_examples(path / "minerl_navigate" / "train"),
            "test": self._generate_examples(path / "minerl_navigate" / "test"),
        }

    def _generate_examples(self, path):
        """Yields examples."""
        for f in path.glob("*.mp4"):
            yield str(f), {
                "video": str(f.resolve()),
            }
