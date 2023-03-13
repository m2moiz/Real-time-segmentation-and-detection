# Real Time Segmentation and Detection

This is a project that uses [pixellib](https://github.com/ayoolaolafenwa/PixelLib)  library, a wrapper for [Detectron2](https://github.com/facebookresearch/detectron2) , to perform real-time instance segmentation on video captured from a webcam.
## Requirements
- Python 3.7 or higher
- PyTorch 1.8.0
- Torchvision 0.9.0
- Torchaudio 0.8.0
- Cuda Toolkit 11.1
- pycocotools
- pixellib
- Numpy 1.18.0
- mkl

You can install these dependencies using the following commands:

```bash
conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.1 -c pytorch -c conda-forge
pip install pycocotools
pip install pixellib
pip install numpy==1.18.0
conda install -c anaconda mkl
```


## Running the application

Once you have installed the dependencies, you can start the program by running the `detect.py` file. This will capture video from the webcam and perform instance segmentation in real-time.

```bash
python detect.py
```


## To do 
- **Containerize the application using Docker** 
- **Attach a requirements.txt file for easier installation of dependencies**
## Want to contribute?

Please feel free to fork this repository and submit a pull request. We'd love to see what you come up with!
## License

This project is licensed under the MIT License
