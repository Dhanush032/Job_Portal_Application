```markdown
# Job Portal Project

A full-stack job portal web application built with Django and Django REST Framework.

## Features
- User authentication with JWT
- Role-based access (Admin, Employer, Job Seeker)
- Job posting and management
- Job application system with resume upload
- Admin dashboard
- Search and filter jobs

## Tech Stack
- **Backend**: Django 5.x, Django REST Framework
- **Authentication**: JWT (Simple JWT)
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Frontend**: HTML, CSS, JavaScript

## Installation

1. Clone the repository
```bash
git clone 
cd job_portal
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create folders
```bash
mkdir -p templates static media/resumes media/profiles
```

5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create superuser
```bash
python manage.py createsuperuser
```

7. Run development server
```bash
python manage.py runserver
```

8. Access the application
- Homepage: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## API Endpoints

### Authentication
- `POST /api/accounts/register/` - Register user
- `POST /api/accounts/login/` - Login (get JWT token)
- `GET /api/accounts/profile/` - Get user profile
- `PATCH /api/accounts/profile/` - Update profile

### Jobs
- `GET /api/jobs/` - List all jobs
- `GET /api/jobs/<id>/` - Job details
- `POST /api/jobs/create/` - Create job (Employer only)
- `PATCH /api/jobs/<id>/update/` - Update job
- `DELETE /api/jobs/<id>/delete/` - Delete job

### Applications
- `POST /api/applications/apply/` - Apply for job
- `GET /api/applications/my-applications/` - View my applications
- `GET /api/applications/job/<job_id>/` - View job applications (Employer)
- `PATCH /api/applications/<id>/status/` - Update application status

## Project Structure
```
job_portal/
├── accounts/           # User authentication
├── jobs/              # Job management
├── applications/      # Application system
├── templates/         # HTML templates
├── static/           # CSS, JS files
├── media/            # Uploaded files
├── job_portal/       # Project settings
└── manage.py
```

## Usage

### As Job Seeker
1. Register with role "Job Seeker"
2. Browse jobs at /jobs
3. Apply for jobs with resume
4. Track applications at /my-applications

### As Employer
1. Register with role "Employer"
2. Post jobs at /post-job
3. View applications for your jobs
4. Accept/Reject applications

### As Admin
1. Access admin panel at /admin/
2. Manage users, jobs, and applications
3. Use admin dashboard at /admin-dashboard/

## Future Enhancements
- Email notifications
- Advanced search
- Payment integration
- Chat system
- Resume parser
- Analytics dashboard



##  manage.py Helper Commands

Create a file: `management_commands.md`

```markdown
# Useful Django Management Commands

## Database
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset database (WARNING: Deletes all data)
python manage.py flush

# Show migrations
python manage.py showmigrations
```

## Users
```bash
# Create superuser
python manage.py createsuperuser

# Change user password
python manage.py changepassword 
```

## Development
```bash
# Run development server
python manage.py runserver

# Run on specific port
python manage.py runserver 8080

# Run on all interfaces
python manage.py runserver 0.0.0.0:8000

# Open Django shell
python manage.py shell
```

## Static Files
```bash
# Collect static files (for production)
python manage.py collectstatic
```

## Testing
```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test accounts

# Run with verbose output
python manage.py test --verbosity=2
```

## Database Inspection
```bash
# Show SQL for migrations
python manage.py sqlmigrate accounts 0001

# Open database shell
python manage.py dbshell
```
```

##  Quick Setup Script (setup.sh for Linux/Mac)

```bash
#!/bin/bash

echo "Setting up Job Portal Project..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create necessary folders
mkdir -p templates static media/resumes media/profiles

# Run migrations
python manage.py makemigrations
python manage.py migrate

echo "Setup complete!"
echo "Next steps:"
echo "1. Run: python manage.py createsuperuser"
echo "2. Run: python manage.py runserver"
echo "3. Visit: http://127.0.0.1:8000/"
```

##  Quick Setup Script (setup.bat for Windows)

```batch
@echo off
echo Setting up Job Portal Project...

:: Create virtual environment
python -m venv venv
call venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt

:: Create necessary folders
if not exist "templates" mkdir templates
if not exist "static" mkdir static
if not exist "media" mkdir media
if not exist "media\resumes" mkdir media\resumes
if not exist "media\profiles" mkdir media\profiles

:: Run migrations
python manage.py makemigrations
python manage.py migrate

echo Setup complete!
echo Next steps:
echo 1. Run: python manage.py createsuperuser
echo 2. Run: python manage.py runserver
echo 3. Visit: http://127.0.0.1:8000/
pause
```