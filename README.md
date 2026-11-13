# Kun.uz Clone (Django)

**Kun.uz Clone** — Django framework yordamida yaratilgan yangiliklar sayti. Loyiha Kun.uz yangiliklar portalining dizayni va funksiyalaridan ilhomlangan.

## Imkoniyatlar

- Yangiliklar ro'yxati va batafsil sahifalari
- Rasmli yangiliklar
- Kategoriyalar bo'yicha yangiliklar
- Ommabop yangiliklar va bosh sahifa slideri
- Django Admin orqali yangiliklarni boshqarish
- Responsive dizayn

## Texnologiyalar

- Python
- Django
- HTML5, CSS3, Bootstrap
- SQLite
- Pillow

## O'rnatish

1. Repozitoriyani yuklab oling:

   ```bash
   git clone https://github.com/umidjon3455/KunUzClone_6.git
   cd KunUzClone_6
   ```

2. Virtual muhit yarating:

   **Windows (PowerShell):**
   ```powershell
   py -m venv venv
   venv\Scripts\Activate.ps1
   ```

   **macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Bog'liqliklarni o'rnating:

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Migratsiyalar va server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

Sayt: http://127.0.0.1:8000/

## Admin panel

Admin foydalanuvchi yaratish:

```bash
python manage.py createsuperuser
```

Admin panel: http://127.0.0.1:8000/admin/

## Muallif

**Umidjon Abdullayev**  
GitHub: https://github.com/umidjon3455
