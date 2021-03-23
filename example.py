import resource
low, high = resource.getrlimit(resource.RLIMIT_NOFILE)
resource.setrlimit(resource.RLIMIT_NOFILE, (high, high))

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
