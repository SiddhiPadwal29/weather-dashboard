HOW TO USE:

1. Replace YOUR_API_KEY in app.py with your OpenWeatherMap API key.
2. Open terminal or CMD in this folder.
3. Run: pip install flask requests
4. Then run: python app.py
5. Your browser will automatically open: http://127.0.0.1:5000

To create .exe:
Run this command:
pyinstaller --noconfirm --onefile --add-data "templates;templates" --add-data "static;static" app.py
