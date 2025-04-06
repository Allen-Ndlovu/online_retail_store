# Online Retail Store

An e-commerce platform for managing product listings, customer orders, inventory, and transactions.  
**Tech Stack:** Python, Django, PostgreSQL, Bootstrap

## Features
- Product catalog management.
- Order processing and inventory tracking.
- Responsive design with Bootstrap.
- External configuration for database settings.

## Installation & Setup
1. **Clone the repository:**  
   `git clone https://github.com/Allen-Ndlovu/online_retail_store.git`
2. **Set up a virtual environment:**  
   `python -m venv venv`  
   Activate it (`venv\Scripts\activate` on Windows or `source venv/bin/activate` on Unix).
3. **Install dependencies:**  
   `pip install -r requirements.txt`
4. **Configure Database:**  
   - In the project root, copy `online_retail_store/local_settings.py.sample` to `online_retail_store/local_settings.py` and update the database settings.
5. **Run Migrations & Server:**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
