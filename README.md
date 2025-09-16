# Wiki Encyclopedia

A Django-based encyclopedia application that allows users to create, edit, and search through encyclopedia entries.

## Features

- **Entry Pages**: View encyclopedia entries at `/wiki/TITLE`
- **Search**: Search for entries with exact matches or partial substring matches
- **Create New Page**: Add new encyclopedia entries with Markdown support
- **Edit Page**: Edit existing entries
- **Random Page**: Navigate to a random encyclopedia entry
- **Markdown Support**: All entries support Markdown formatting with HTML conversion

## Installation

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

3. Open your browser and navigate to `http://127.0.0.1:8000`

## Usage

- **Home Page**: Lists all available encyclopedia entries
- **Search**: Use the search box in the sidebar to find entries
- **Create New Page**: Click "Create New Page" in the sidebar to add new entries
- **Edit Page**: Click "Edit Page" on any entry to modify its content
- **Random Page**: Click "Random Page" to view a random entry

## File Structure

- `encyclopedia/`: Main Django app
  - `views.py`: Contains all view functions
  - `urls.py`: URL routing configuration
  - `util.py`: Utility functions for file operations
  - `templates/`: HTML templates
  - `static/`: CSS styling
- `entries/`: Directory containing Markdown encyclopedia entries
- `wiki/`: Django project settings

## Dependencies

- Django >= 3.0.0
- markdown2 >= 2.4.0
