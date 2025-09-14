Workshop1 package - Quick start and step-by-step instructions
=============================================================

Files included in this zip (relative to workshop1/):
  app/
    requirements.txt
    manage.py
    nc_tutorials/ (Django project)
      settings.py
      urls.py
      wsgi.py
    tutorials/ (app)
      models.py, views.py, serializers.py, urls.py, admin.py
    users/ (app)
      views.py, urls.py
    Dockerfile
    .dockerignore
    .env.example
  docker-compose.yml
  data/misc/django_init.sql

There are also two extra zip files included at the archive root:
  - tutorials.zip  (contains the tutorials/ app contents)
  - users.zip      (contains the users/ app contents)

------------------------------------------------------------------
Before you begin (requirements)
------------------------------------------------------------------
- Install Python 3.9+ and ensure 'python' or 'python3' is on your PATH.
- Install Docker Desktop (Docker Engine + Docker Compose).
- Install VS Code (optional but recommended).
- Install Insomnia (or Postman) for API tests.
- (Optional) Install Git if you will use version control.

------------------------------------------------------------------
1) Extract the zip
------------------------------------------------------------------
Windows: Right-click the zip and choose 'Extract All', or use PowerShell:
  Expand-Archive -Path workshop1_full.zip -DestinationPath .\workshop1

macOS/Linux:
  unzip workshop1_full.zip -d workshop1

You will have a 'workshop1' folder (same structure as described above).

------------------------------------------------------------------
2) Create and activate the Python virtual environment (inside workshop1)
------------------------------------------------------------------
Open a terminal in the `workshop1/app` folder (or in VS Code open that folder).

Windows (PowerShell):
  cd workshop1\app
  python -m venv ..\venv
  ..\venv\Scripts\Activate.ps1   # or use activate.bat for cmd.exe

macOS / Linux:
  cd workshop1/app
  python3 -m venv ../venv
  source ../venv/bin/activate

You should see (venv) in your prompt.

Upgrade pip to the specified version (lab requires pip 21.1.2):
  pip install --upgrade pip==21.1.2
  pip --version

------------------------------------------------------------------
3) Install Python dependencies
------------------------------------------------------------------
  cd workshop1/app
  pip install -r requirements.txt
  pip list   # verify packages

------------------------------------------------------------------
4) Task 2 - Scaffold check (already scaffolded in this zip) & run dev server
------------------------------------------------------------------
For Task 1 the lab asked you to comment out DATABASES in settings.py for the initial test.
The provided settings.py has the DATABASES block commented. You can run the server without DB:

  python manage.py runserver 8000

Open http://127.0.0.1:8000 in your browser to see the app (you may see a 404 at the root until apps are included).
Stop server with Ctrl+C.

------------------------------------------------------------------
5) Build Docker image and run container (Task 3)
------------------------------------------------------------------
From workshop1/ (NOT app):
  docker build -t nc_tutorials_image ./app
  docker run --name nc_tutorials_container -p 8000:8000 nc_tutorials_image

Visit http://127.0.0.1:8000 to verify. Stop and remove the container when done:
  docker stop nc_tutorials_container
  docker rm nc_tutorials_container

------------------------------------------------------------------
6) Docker Compose with Postgres and pgAdmin (Task 4 & 5)
------------------------------------------------------------------
1) Ensure no existing containers conflict: docker ps -a and stop/remove as needed.
2) Edit app/.env.example -> copy to app/.env and set DB_HOST=pg (important for compose).
3) From workshop1/ run:
     docker compose up -d
   (or `docker-compose up -d` if your docker is older)

4) Confirm services running:
     docker compose ps

5) Open pgAdmin at http://127.0.0.1:5433
   Login: admin@example.com / admin123
   Add a new server (Connection -> Host: pg, Password: admin123). Expand Databases to see nc_tutorials_db.

------------------------------------------------------------------
7) Use python-decouple and .env (Task 5)
------------------------------------------------------------------
Edit workshop1/app/nc_tutorials/settings.py:
  - Uncomment or add: from decouple import config
  - Replace DATABASES with the postgres config using config('DB_NAME') etc.
Example shown in the file comments.

After updating settings, rebuild the images and bring compose up again:
  docker compose down --rmi all
  docker compose up -d --build

------------------------------------------------------------------
8) Run migrations inside the web container (Task 6 & 8)
------------------------------------------------------------------
Create default tables and tutorials table:
  docker compose exec web python manage.py makemigrations --noinput
  docker compose exec web python manage.py migrate --noinput

Confirm tables in pgAdmin (look under Schemas -> public -> Tables). You should see django_ and auth_ tables.
After creating the tutorials model and running makemigrations/migrate the tutorials_tutorial table will appear.

------------------------------------------------------------------
9) Test API with Insomnia / Postman (Task 9)
------------------------------------------------------------------
POST to: http://127.0.0.1:8000/api/tutorials/
JSON example:
  {
    "title": "Introduction to Django",
    "tutorial_url": "https://www.djangoproject.com",
    "image_path": "../static/images/tutorials/introDjango.png",
    "description": "A tutorial about Django",
    "published": true
  }

You should receive 201 Created and see the new record at http://127.0.0.1:8000/api/tutorials/

------------------------------------------------------------------
10) Run the autograder (Task 10)
------------------------------------------------------------------
Download the autograder.py file from your course page and place it in the 3-DevOps folder (one level up from workshop1).
Then run:
  cd /path/to/3-DevOps
  python autograder.py
Follow the prompts; save the results.json file for submission.

------------------------------------------------------------------
Troubleshooting
------------------------------------------------------------------
- If psycopg2 fails during pip install, ensure the Dockerfile includes libpq-dev / build-essential (this repo's Dockerfile already does).
- If web can't connect to pg when using docker compose, verify DB_HOST=pg in the app .env and in docker-compose environment.
- If ports 8000/5432/5433 are in use, stop conflicting containers or change the ports in docker-compose.yml.

------------------------------------------------------------------
Note
------------------------------------------------------------------
This package is a minimal starter that follows your lab instructions. Before submitting, follow the lab precisely: comment/uncomment DATABASES per task, run the migrations inside the container, and take the required Insomnia screenshots.
# workshop2
# workshop2
