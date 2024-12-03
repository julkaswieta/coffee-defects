To run the training on a machine with an Nvidia GPU, it's best to set up a conda environemnt and run the following commands:
- make sure Python 3.9 or above is installed in the env: conda install Python=3.9
- conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
- conda install conda-forge::ultralytics

For running the app, just a Python environment with Ultralytics installed should be enough

## To run the app: 
Run the app.py script in the app folder