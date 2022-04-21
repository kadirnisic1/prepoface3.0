# Face Detection with OpenCV and Python

This project concerns the creation of python scripts capable of detecting faces in images or in streaming through a Webcam. For the development of this project, the OpenCV library and the Python programming language were used.

![alt text](https://raw.githubusercontent.com/EstanislauFilho/Computer-Vision-Face-Detect-OpenCV/master/Imagens/faces_detected.png)


## Starting the Project

The following instructions will allow you to run, develop and contribute to the project in question. Follow all the steps below to run the Facial Detection project using the OpenCV library and the Python programming language.

### Prerequisites

To run the scripts in  python present in this project, you need to install the following components on your machine:

```
Python 3.0 or higher version.

OpenCV+Contrib.
```

## Execution and Testing

To run and test the face_detect_image.py and face_detect_webcam.py scripts, you should initially open them in your Python development environment.

### Running face_detect_image.py

This python script does the face detection of people in static image. For this experiment was used the image "scientists.jpg" present in the "Images" folder. For correct face detection, it was necessary to determine the parameters "scaleFactor", "minSize" and "minNeighbors" in the function "detectMultiScale". To test it just run it on the IDE.

Another way to execute the script is via terminal, by the following command:

```
sudo python3 face_detect_image.py
```

### Running face_detect_webcam.py

This script in python makes the facial detection in streming video through a webcam. To test it just run it in the IDE.


Another way to execute the script is via terminal, by the following command:

```
sudo python3 face_detect_webcam.py
```

## Developed with

* [OpenCV](https://opencv.org/) - Computer vision library developed by Intel in 1999;
* [Python Software Foundation](https://maven.apache.org/) - Language programming;
* [PyCharm](https://www.jetbrains.com/pycharm/) - IDE used for script development.

## Contributing

Please read Contributing.md for details on the process for submitting pull requests to the developer.

## Version

For the available versions, see the tags in this repository.

## Authors

* **Estanislau de Sena Filho** - *Computer Engineering Student at* [CEFET-MG](http://www.cefetmg.br/)

## License

This is not a licensed project. Its purpose is unique to studying and learning about computer vision.

## Special thanks

* Jones Granatyr e Gabriel Alves


