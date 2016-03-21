# Musique et Activité Cérébrale

## Papers
This project is based on the papers contained in this folder

## Data
Summary of the dataset:
- each recording is 40 min long
- which is composed of 2 recordings of 20 min
- 10 songs of 2 min make one recording

The data is of the [h5 format](http://docs.h5py.org/en/latest/quick.html)

| Left Recording | Zone           | Meaning          |
| -------------- |:--------------:| ----------------:|
| signal_0       | T3             | auditoral cortex |
| signal_1       | C3             | motor cortex     |
| signal_2       | CZ             | Vertex           |
| signal_3       | nothing        | nothing          |
| signal_4       | nothing        | nothing          |

| Right Recording| Zone           | Meaning          |
| -------------- |:--------------:| ----------------:|
| signal_0       | T4             | auditoral cortex |
| signal_1       | C4             | motor cortex     |
| signal_2       | F4             | frontal cortex   |
| signal_3       | E2             | Eyes             |
| signal_4       | nothing        | nothing          |

## Data Processing in dataset_generator.py
We manually find with script.py the beginning of the music in the data
Start of music for Louis = 34532
Start of music for Charles = 21189

Then dataset_generator.py cuts the 40 min recordings into the 20 songs.
Each 20 min recording is an array of 10 songs.
Each song is a dictionary of the signals. The keys are the zones.

You can access the recordings later by calling
```python
from dataset_generator import *
```

## Frequency analysis
Our choice was to use multitapering for the FFT of the signals.
For more details ask [Charles Masson](https://github.com/CharlesMasson)

## Unsupervised study
See the scripts unsupervised.py and unsupervised_rythmic.py
The frequency powers of the 10 songs are plotted in order to look patterns in the data.
The resulting plots are in the folder images.

## Supervised study
Sklearn is used to try to see if we can predict if a song is rythmic or not.
The script is also interactive in the command prompt.
