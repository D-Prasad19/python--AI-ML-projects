# FactFlow: AI-Powered Fake News Detection 🛡️

![logo](logo2.png)

<p align="center">
    <strong>A modernized Django web application for predicting the authenticity of news articles using Machine Learning.</strong>
</p>

---

## 👥 Authors
This project was developed and modernized by:
* **Divyanshu Prasad** 
* **Palak Dixit** 

## 💡 Motivation
In the information age, disinformation spreads faster than facts. **FactFlow** is a personal approach to fighting this problem, providing a transparent and accessible tool for everyday readers to verify the content they consume.

## ⚙️ How It Works
The application utilizes a **Passive Aggressive Classifier (PAC)**. Unlike traditional algorithms, the PAC remains passive for correct classifications but turns "aggressive" during miscalculations, updating its weights to improve future accuracy. This makes it ideal for the high-frequency nature of news cycles.



**Technical Highlights:**
* **TF-IDF Vectorization**: Analyzes word frequency and importance to convert text into mathematical input.
* **Django Backend**: A robust framework managing user sessions and real-time predictions.
* **Modern Migration**: Fully updated to support the latest Python 3.14 and Django 5.x standards.

## 📊 Datasets
The model was trained and validated using industry-standard Kaggle datasets:
* ['Fake News' InClass Prediction Competition](https://www.kaggle.com/c/fake-news/data)
* ['Fake and real news dataset' by Clément Bisaillon](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)

---
