# Lung Cancer Prediction System

# Team 
- [https://github.com/tims-exe]
- [https://github.com/anupa00]
- [https://github.com/sreenandharamesh]
- [https://github.com/NandanaMohan1501]

## Overview

The **Lung Cancer Prediction System** is an advanced full-stack web application built using Django that aims to assist healthcare providers in diagnosing lung cancer. This system utilizes cutting-edge machine learning techniques to analyze patient data and CT scan images, providing accurate predictions regarding the presence of lung cancer.

### Key Components

The application integrates two distinct predictive models, each designed to analyze different types of data:

1. **CSV Model**:
   - **Description**: This model is trained on structured data sourced from a CSV file, which contains a comprehensive set of features related to patient health. These features include demographic information (age, gender, smoking history), clinical symptoms (coughing, chest pain, weight loss), and other relevant health indicators.
   - **Machine Learning Techniques**: The model employs various machine learning algorithms (such as logistic regression, decision trees, or random forests) to discern patterns in the data that correlate with lung cancer diagnoses. This approach allows for the identification of high-risk individuals based on their symptomatology and medical history.
   - **Benefits**: The CSV model offers a straightforward way to assess the risk of lung cancer based on non-imaging data, making it an accessible tool for initial screenings and consultations.

2. **CT Scan Model**:
   - **Description**: In contrast, the CT Scan Model leverages a convolutional neural network (CNN) that is specifically designed for image classification tasks. This model is trained on a large dataset of annotated CT scan images, enabling it to learn complex visual features associated with lung cancer.
   - **Machine Learning Techniques**: The CNN processes the images through multiple layers, extracting hierarchical features that help distinguish between healthy and malignant lung tissue. The model can detect subtle visual cues that may not be apparent to the human eye, enhancing diagnostic accuracy.
   - **Benefits**: This model provides a powerful tool for radiologists and oncologists, allowing them to make informed decisions based on visual data. It can significantly reduce diagnostic errors and facilitate earlier interventions for patients diagnosed with lung cancer.

### Application Workflow

Users of the Lung Cancer Prediction System can interact with both models through an intuitive web interface. They can input patient data for the CSV model or upload CT scan images for the CT Scan model. Upon submission, the application processes the input through the respective machine learning model and delivers predictive results, including a probability score and relevant insights.

By combining these two approaches, the Lung Cancer Prediction System aims to enhance diagnostic efficiency, improve patient outcomes, and contribute to the ongoing battle against lung cancer.

## Features

- User-friendly web interface for inputting patient data.
- Integration of two distinct machine learning models for comprehensive predictions.
- Detailed prediction results with confidence scores.

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: Python, scikit-learn, TensorFlow/Keras for model training


