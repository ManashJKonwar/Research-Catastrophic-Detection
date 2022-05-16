# Research-Catastrophic-Detection
The sole purpose of this research work is to predict catastrophic events such as heavy rainfall, floods, etc using state of the art technique which includes time series forecasting, CNN, RNN, etc  

Important definitions:  
1. **Time Series Analysis (TSA):** A time series is nothing but a sequence of various data points that occurred in a successive order for a given period of time.  
**Objectives:**  
* To understand how time series works, what factors are affecting a certain variable(s) at different points of time.  
* Time series analysis will provide the consequences and insights of features of the given dataset that changes over time.  
* Supporting to derive the predicting the future values of the time series variable.  
**Assumptions:**  
There is one and the only assumption that is “stationary”, which means that the origin of time, does not affect the properties of the process under the statistical factor.  

2. **Significance of TSA:** TSA is the backbone for prediction and forecasting analysis, specific to the time-based problem statements.  
* Analyzing the historical dataset and its patterns.  
* Understanding and matching the current situation with patterns derived from the previous stage.  
* Understanding the factor or factors influencing certain variable(s) in different periods.  

3. **Components of TSA:** 
* Trend
* Seasonality  
* Cyclical  
* Irregularity  

4. **Stationary or Non-Stationary:**  
* **Stationary:** Date where the mean, variance and Covariance are constant with time can be classified as stationary data.
* **Non-Stationary:** Opposite of Stationary. Most of the real time TSA data is in non stationary form.

> Live demo [_here_](https://www.example.com). <!-- If you have the project hosted somewhere, include the link here. -->

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Dataset Utilized](#dataset-utilized)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [References](#references)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->

## General Information
- The aim of this repository is to perform rainfall prediction using time series based algorithms on real time rainfall station data.  
- Research on possible frameworks to achieve rainfall prediction for time series based data.  
- Develop a dashboard for exploring the dataset in process and also draw statistical insights on the same.

## Technologies Used
- Time Series
- Dash 

## Features
List the ready features here:
- Training and Inferencing Time Series based Framework - Done

## Screenshots
![Pointnet Classifier Frontend](./repo_assets/Pointnet_Classifier_Frontend.jpeg)

## Setup
- git clone https://github.com/ManashJKonwar/IP-Pointnet.git (Clone the repository)
- python3 -m venv IPPointnetVenv (Create virtual environment from existing python3)
- activate the "IPPointnetVenv" (Activating the virtual environment)
- pip install -r requirements.txt (Install all required python modules)

## Dataset Utilized
- The daily dataset is based on data extracted from a rainfall station at [jennings](https://www.ncdc.noaa.gov/cdo-web/datasets), louisiana, USA.  

## Usage
### For Training PointNet
- python rainfall_prediction/train.py
### For Running Web Application
- python smart_weather/index.py

## Project Status
Project is: __in progress_ 
<!-- / _complete_ / _no longer being worked on_. If you are no longer working on it, provide reasons why._ -->

## Room for Improvement
- 

To do
- 

## References
[1] PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation; Charles R. Qi, Hao Su, Kaichun Mo, Leonidas J. Guibas;
CVPR 2017; https://arxiv.org/abs/1612.00593.

## Acknowledgements

## Contact
Created by [@ManashJKonwar](https://github.com/ManashJKonwar) - feel free to contact me!

<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->