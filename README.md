# 🎬 MovieStore

A Django-based **Movie Store Web Application** where users can browse movies, add them to their cart, purchase, and leave reviews. The project includes user authentication, shopping cart functionality, and an organized movie review system with a responsive interface.

---

## 📖 Description

**MovieStore** is a modular Django application consisting of apps like:

- `accounts` → Handles user authentication (signup, login, orders).
- `movies` → Manages movies and reviews.
- `cart` → Shopping cart and purchase flow.
- `home` → Static pages like home and about.

It is built using Django best practices with a clean separation of apps, templates, and static files.

---

## ⚙️ Installation & Run

### 1. Clone the repository
```bash
git clone https......
cd moviestore
```

### 2. Create a virtual environment
```bash
python -m venv venv
# On Linux/Mac
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (optional but recommended)
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

Visit 👉 `http://127.0.0.1:8000/`

---

## 🚀 Usage

- Browse movies on the homepage.  
- Sign up or log in to write reviews and place orders.  
- Add movies to your cart and purchase them.  
- Admin users can manage movies, reviews, and users via `/admin/`.  

---

## 🧰 Tech Stack

- **Backend:** Django (Python 3.12)  
- **Frontend:** HTML5, CSS3 (`static/css/style.css`)  
- **Database:** SQLite (default, easy to switch to PostgreSQL/MySQL)  
- **Templating Engine:** Django Templates  
- **Media Handling:** Stored in `media/movie_images/`  
- **Authentication:** Django built-in auth system  
- **Deployment:** Localhost (can be deployed on Heroku, Render, or any VPS)  

---

## ✨ Features

- ✅ User authentication (signup, login, logout)  
- ✅ Browse movies and view details  
- ✅ Add/Edit/Delete reviews  
- ✅ Shopping cart with purchase option  
- ✅ Order history for users  
- ✅ Admin dashboard for managing movies & users  
- ✅ Responsive UI with organized templates  

---

## 👤 Author

**Kaushal Sakhareliya**  
🔗 GitHub: [@KAUSHAL-0922](https://github.com/KAUSHAL-0922) 
