# USK-Coffe Segmentasi  > 2024-11-07 10:41am
https://universe.roboflow.com/coffee-vhnrv/usk-coffe-segmentasi-4os02

Provided by a Roboflow user
License: BY-NC-SA 4.0

**Dataset Annotation** is a critical stage in the development of object detection systems, especially when working with datasets like [USK-Coffee](https://comvis.unsyiah.ac.id/usk-coffee/), which focuses on green Arabica coffee beans. Annotation is carried out to provide crucial information to the object detection model, enabling it to recognize and classify coffee beans based on their varieties. The following is a description of the [USK-Coffee](https://comvis.unsyiah.ac.id/usk-coffee/) dataset annotation:

**Annotation Types:**
1. **Bounding Box:** Each coffee seed in the image will be annotated with a bounding box surrounding it. This includes peaberry, longberry, premium, and defective beans.
2. **Class Labels:** Each bounding box will be assigned a class label corresponding to the type of coffee bean it represents, such as *defect, longberry, peaberry, premium*.

**Annotation Process:**
1. **Manual Annotation:** Annotation will be carried out manually by competent annotators, namely *[Imam Sayuti](https://pddikti.kemdikbud.go.id/data_mahasiswa/RjgxQkNENjAtNzMxMC00QUQ4LTg4QjctNThGNjRGMDkyRTNE)* and *[Patimah Lubis](https://pddikti.kemdikbud.go.id/data_mahasiswa/N0M1QTJFQjUtQUJFNi00MzlBLTk2MDYtODM1M0UwOEQxRkM2)*. They will mark the position of each coffee bean in the image and assign the appropriate class label.
2. **Quality Control:** The annotation process will involve quality control by *[Imam Sayuti](https://pddikti.kemdikbud.go.id/data_mahasiswa/RjgxQkNENjAtNzMxMC00QUQ4LTg4QjctNThGNjRGMDkyRTNE)*, *[Patimah Lubis](https://pddikti.kemdikbud.go.id/data_mahasiswa/N0M1QTJFQjUtQUJFNi00MzlBLTk2MDYtODM1M0UwOEQxRkM2)*, and *[Kahlil Muchtar](https://ieeexplore.ieee.org/author/38547014400)* (as the project's supervising lecturer) to ensure that each coffee bean is correctly identified and labeled.

**Dataset File Framework:**
USK-Coffee
|-- test
|   |-- defect   (400 Images)
|   |-- longberry (400 Images)
|   |-- peaberry  (400 Images)
|   |-- premium   (400 Images)

|-- train
|   |-- defect   (1200 Images)
|   |-- longberry (1200 Images)
|   |-- peaberry  (1200 Images)
|   |-- premium   (1200 Images)

|-- val
|   |-- defect   (400 Images)
|   |-- longberry (400 Images)
|   |-- peaberry  (400 Images)
|   |-- premium   (400 Images)

**Dataset Source Citation:**
The [USK-Coffee dataset](https://comvis.unsyiah.ac.id/usk-coffee/) was announced at the [IEEE International Conference](https://ieeexplore.ieee.org/document/9865489) on Cybernetics and Computational Intelligence (CyberneticsCom) in 2022 by Febriana, A., Muchtar, K., Dawood, R., and Lin, CY. This dataset has made a valuable contribution, allowing for further research in deep learning and the development of object detection systems using YOLO. The dataset source citation is as follows:

*A. Febriana, K. Muchtar, R. Dawood and C. -Y. Lin, "USK-COFFEE Dataset: A Multi-Class Green Arabica Coffee Bean Dataset for Deep Learning," 2022 IEEE International Conference on Cybernetics and Computational Intelligence (CyberneticsCom), Malang, Indonesia, 2022, pp. 469-473, doi: 10.1109/CyberneticsCom55287.2022.9865489.* [(pdf)](https://drive.google.com/file/d/1cQLhXG38EARRJy-4ZlGkXHL_SUKoFJpQ/view)

With meticulous dataset annotation by *[Imam Sayuti](https://pddikti.kemdikbud.go.id/data_mahasiswa/RjgxQkNENjAtNzMxMC00QUQ4LTg4QjctNThGNjRGMDkyRTNE)*, *[Patimah Lubis](https://pddikti.kemdikbud.go.id/data_mahasiswa/N0M1QTJFQjUtQUJFNi00MzlBLTk2MDYtODM1M0UwOEQxRkM2)*, and oversight by *[Kahlil Muchtar](https://ieeexplore.ieee.org/author/38547014400)*, it is expected that research utilizing this dataset can achieve accurate and high-performance object detection.