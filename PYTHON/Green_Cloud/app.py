from flask import Flask, render_template
import json
import os # <--- Added this to fix path issues
from logic import process_cloud_data

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Fix: Get the absolute path of the directory where app.py is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'mock_resources.json')

    # 1. Load Data using the fixed path
    try:
        with open(file_path, 'r') as file:
            raw_data = json.load(file)
    except FileNotFoundError:
        return "Error: mock_resources.json not found! Please check your folder structure."
    
    # 2. Process Data
    resources = process_cloud_data(raw_data)
    
    # 3. Calculate Aggregates
    total_cost = sum(r['cost'] for r in resources)
    total_carbon = sum(r['carbon'] for r in resources)
    
    return render_template('dashboard.html', 
                           resources=resources, 
                           total_cost=round(total_cost, 2), 
                           total_carbon=round(total_carbon, 2))

if __name__ == '__main__':
    app.run(debug=True, port=5000)