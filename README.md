# CROP_YEILD_PREDICTION

# Crop Yield Prediction Project

## Overview
This project is a comprehensive crop yield prediction system that leverages machine learning to help farmers and agricultural researchers predict crop yields based on various environmental and agricultural factors.

## Features
- Web-based prediction interface
- Interactive dashboard for crop yield analysis
- Machine learning model for yield prediction
- Supports multiple crops and regions

## Technology Stack
- Backend: Python
- Web Framework: Flask
- Data Visualization: Plotly, Streamlit
- Machine Learning: Scikit-learn
- Frontend: HTML, Bootstrap

## Project Structure
```
crop-yield-prediction/
│
├── app.py                  # Flask web application
├── dashboard.py            # Streamlit data visualization dashboard
├── index.html              # Frontend HTML template
├── dtr.pkl                 # Trained Decision Tree Regression model
├── preprocessor.pkl        # Data preprocessing pipeline
└── requirements.txt        # Project dependencies
```

## Prerequisites
- Python 3.8+
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/crop-yield-prediction.git
cd crop-yield-prediction
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Web Prediction Interface
```bash
python app.py
```
- Navigate to `http://localhost:5000` in your web browser

### Data Visualization Dashboard
```bash
streamlit run dashboard.py
```
- Dashboard will open in your default web browser

## Input Features
The prediction model considers the following features:
- Year
- Average Rainfall (mm/year)
- Pesticides Usage (tonnes)
- Average Temperature (°C)
- Area/Region
- Crop Type

## Model Details
- Algorithm: Decision Tree Regression
- Preprocessing: Custom preprocessor for feature transformation
- Trained on historical agricultural data

## Data Visualization
The Streamlit dashboard offers:
- Crop-wise yield analysis
- Region-wise yield treemap
- Time series yield analysis
- Hierarchical yield view by region and crop

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Pravinkumar A- Pravinkumar22005@gmail.com

Project Link: [https://github.com/yourusername/crop-yield-prediction](https://github.com/yourusername/crop-yield-prediction)
