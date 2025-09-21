# CORD-19 Research Dataset Explorer

Explore COVID-19 research data from the CORD-19 metadata via interactive charts and dataset previews.

---

## 🔗 Live Demo

Check out the live app here:  
[CORD-19 Research Dataset Explorer](https://frameworkassignment-dgqnb5hhdwydwp9pzfaaqw.streamlit.app/)

---

## 📋 What It Does

- Loads and cleans data from `metadata.csv`  
- Displays a preview of the dataset (titles, authors, publication time, etc.)  
- Shows number of papers published per year  
- Highlights the top 10 journals by number of papers  

---

## 🧰 Getting Started

These instructions will help you run this project locally.

### Prerequisites

- Python 3.7+  
- Git  

### Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/kevinndede2000/Framework_assignment.git
   cd Framework_assignment
Install required libraries:

bash
Copy code
pip install streamlit pandas matplotlib seaborn
▶️ Running Locally
From the project folder, run:

bash
Copy code
streamlit run app.py
Then open the URL shown in your terminal (usually http://localhost:8501) in a browser.

🗂 Project Structure
bash
Copy code
Framework_assignment/
├── app.py            # Streamlit app
├── data/
│   └── metadata.csv  # Dataset file
├── README.md         # This documentation
└── requirements.txt  # Dependencies (if provided)
🤝 Contributing
Feel free to open issues or pull requests to improve the project! Suggestions of new visualizations, search functionalities, or performance improvements are welcome.

📄 Author
Kevin Ndede
Frameworks Assignment — CORD-19 Research Dataset Explorer

⚠️ Notes
The data file (metadata.csv) used here is large; working with a smaller sample can improve loading and performance during development.

Column names in the dataset aren’t always consistent; the app includes logic to map and rename fields by their column positions where needed.

yaml
Copy code

---

If you want, I can also generate a **short version** or one with screenshots included for your GitHub profile.
::contentReference[oaicite:0]{index=0}
