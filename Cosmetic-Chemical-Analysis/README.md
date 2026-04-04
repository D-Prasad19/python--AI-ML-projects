# Cosmetic Chemical Component Analysis 🧴🧪

An AI-driven approach to analyzing cosmetic ingredients using Natural Language Processing (NLP) and Machine Learning, developed during my tenure with **MedTourEasy**.

## 🎯 Project Objective
Choosing skincare products is often a "trial and error" process. This project uses data science to move beyond marketing claims, using chemical similarities to predict which products are best suited for specific skin types (specifically targeting dry skin moisturizers).

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn (t-SNE), Bokeh (Interactive Visualization)
- **Techniques:** NLP Tokenization, Bag of Words (BoW), Dimensionality Reduction

## 📊 Methodology
1. **Data Collection:** Analyzed a dataset of 1,472 cosmetic products from Sephora.
2. **Preprocessing:** Tokenized raw ingredient lists into a document-term matrix.
3. **Dimensionality Reduction:** Applied **t-SNE** to map complex chemical relationships into a 2D space.
4. **Visualization:** Created an interactive map where users can identify "ingredient neighbors" to find alternatives to their favorite products.

## 📈 Key Insights
- Successfully clustered products based on actual chemical composition rather than brand marketing.
- Identified high-similarity overlaps between luxury and budget-friendly moisturizers.

## 📂 Files
- `Analysis_of_Chemical_Components.ipynb`: Full data pipeline and ML model.
- `cosmetics.csv`: The processed dataset.
- `Project_Report_Analysis.pdf`: Comprehensive internship project report.
