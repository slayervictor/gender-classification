# Required:

Python 3.9

## Packages

* keras - v2.11.0
* tensorflow - v2.11.0
* Pillow - v9.4.0
* scipy - v1.9.3

# Model trainer

To train a model, you must prepare the data environment.
The data environment should have the tree structure as follows:

```
Path/To/Folder/
|-- Training/
|   |-- male
|       |  img1.jpg
|       |  img2.jpg
|       |  img3.jpg
|   |-- female
|      |  img5.jpg
|      |  img6.jpg
|      |  img7.jpg
|-- Validation/
    |-- male
        |  img10.jpg
        |  img20.jpg
        |  img30.jpg
    |-- female
       |  img50.jpg
       |  img60.jpg
       |  img70.jpg
```

Now copy the absolute path to the folder containing the Training and Validation folders and
replace in **model_trainer.py**

```python
dir_path = r'<insert_here>'
```

Example:

```python
dir_path = r'C:\Users\Lucas\Pictures\02461 Pictures'
```

Run the **model_trainer.py** and the model will be trained.

# Use trained model

To use a trained model to sort a directory of images into subfolders "male" and "female" please copy the absolute path
to the folder and replace the value in the use_model.py file

```python
dir_path = r'<insert_here>'
```

Example:

```python
dir_path = r'C:\Users\Lucas\Pictures\02461 Pictures\AI_Test'
```

To specify which model to use, copy the absolute path and filename to the model and replace the string value here

```python
model = load_model(r'<absolute_path_including_filename>')
```

Example:

```python
model = load_model(
    r'C:\Users\Lucas\Documents\02631 3-Week-Project\trained_models\model_saved_6400_train_1600_validate.h5')
```

## Getting accuracy of result

Use the **compare.py** file to compare the true classification with the result that the AI model has sorted.\
Copy the absolute path to the true classification folder and the AI sorted folder and insert into the compare.py
variables.

```python
true_classification_path = r'<insert_path_here>'
ai_classified_path = r'<insert_path_here>'
```

Example:

```python
true_classification_path = r'C:\Users\Lucas\Pictures\02461 Pictures\Testing'
ai_classified_path = r'C:\Users\Lucas\Pictures\02461 Pictures\AI_Test'
```