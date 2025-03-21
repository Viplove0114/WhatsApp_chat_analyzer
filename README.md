# 📊 WhatsApp Chat Analyzer

### **Overview**
The **WhatsApp Chat Analyzer** is a Streamlit-based web application that provides detailed insights and visualizations of WhatsApp chat data. It allows users to analyze both **individual and group chats** by displaying statistics, timelines, activity maps, and emoji usage.

---

### 🚀 **Features**
✅ Upload WhatsApp chat files and visualize insights.  
✅ Works with **both individual and group chats**.  
✅ View **total messages, words, media shared, and links**.  
✅ Display **monthly and daily timelines**.  
✅ Activity heatmaps showing message patterns by day and hour.  
✅ **Most busy users** and most common words analysis.  
✅ Generate **Word Clouds** and perform emoji analysis.  

---

### 🛠️ **Tech Stack**
- **Backend:** Python (Pandas, NumPy)  
- **Frontend:** Streamlit  
- **Visualization:** Matplotlib, Seaborn, WordCloud  
- **Data Processing:** Regex, URL Extractor, and Emoji library  

---

### ⚠️ **Python Version Requirement**
✅ Use **Python 3.7 or lower** to run this project.  
❗ This is necessary because the `WordCloud` library version used in the project has compatibility issues with **Python 3.8 and higher**, which may lead to unexpected errors.  

---

### 🔧 **How to Export Your WhatsApp Chat**
To use this app, you need to **export your own WhatsApp chat** (either individual or group chat).  
1. **Open WhatsApp** → Go to the chat you want to export.  
2. Tap the **three dots** (⋮) → Select **More** → **Export chat**.  
3. Choose whether to include or exclude media (both will work).  
4. Send or save the exported `.txt` file.  
5. Upload it into the app to analyze your chat data.  

✅ **Privacy Note:** I am not uploading my personal chats for privacy reasons. This project is designed for users to analyze their own exported WhatsApp chats securely.  

---

### 🔧 **How to Run**
1. Install the dependencies:
```
pip install streamlit pandas matplotlib seaborn wordcloud urlextract emoji
```

2. Run the Streamlit app:
```
streamlit run app.py
```

3. Upload your **WhatsApp chat file** (exported as `.txt`) and explore the insights.

---

### 📁 **File Structure**
```
/app.py          → Main Streamlit application  
/preprocessor.py → Preprocessing chat data (parsing, cleaning)  
/helper.py       → Functions for analysis and visualization  
/stop_hinglish.txt → Stopwords file for WordCloud (if applicable)  
```

---

### 📊 **Usage**
1. Upload the **WhatsApp chat export file**.  
2. Select the user or analyze the entire chat.  
3. View detailed statistics, visualizations, and emoji analysis.  

---

### 🚦 **Future Improvements**
- Add **Sentiment Analysis**.  
- Improve **interactive visualizations**.  
- Include **language detection** for multilingual chats.  

---

✨ **Contributors:**  
[Viplove]  
📧 Contact: [viplovethakran4@gmail.com]  

---

✅ Happy Analyzing! 🎯
