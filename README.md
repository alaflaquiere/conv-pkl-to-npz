# conv-pkl-to-npz

Script to convert a dictionary of numpy arrays saved as a .pkl file to a .npz file.

#### Arguments:
1. folder to convert (including subfolders)
2. template to match the files against (ex: dataset*.pkl)

#### Example
```bash
python conv-pkl-to-npz ./mydata *_data*.pkl
```
