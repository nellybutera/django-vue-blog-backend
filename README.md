## Django + Vue Blog Backend

### Setup

1. Clone repo: `git clone <repo_url>`
2. Create virtual environment: `python -m venv venv`
3. Activate: `source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Start server: `python manage.py runserver`

### Tech Stack
- Django
- Django REST Framework
- PostgreSQL (optional)


Commit and push it to GitHub:

git add README.md
git commit -m "Add project README"
git push

11. Recommended Next Steps

Set up users app for authentication.

Plan models for posts and comments.

Begin writing tests (unit tests for models first).

Prepare requirements.txt for dependency tracking:

```bash
pip freeze > requirements.txt