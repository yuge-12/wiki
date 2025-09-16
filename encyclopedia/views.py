from django.shortcuts import render
from django.http import HttpResponse
import markdown2
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    """Display an encyclopedia entry by title."""
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": f"Requested page '{title}' was not found."
        })
    
    # Convert Markdown to HTML
    html_content = markdown2.markdown(content)
    
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })


def search(request):
    """Handle search functionality."""
    query = request.GET.get('q', '').strip()
    if not query:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })
    
    # Check if query matches an exact entry name
    entries = util.list_entries()
    if query in entries:
        return entry(request, query)
    
    # Search for partial matches
    matches = [entry for entry in entries if query.lower() in entry.lower()]
    
    return render(request, "encyclopedia/search.html", {
        "query": query,
        "matches": matches
    })


def new_page(request):
    """Handle new page creation."""
    if request.method == "POST":
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        
        # Check if entry already exists
        if util.get_entry(title):
            return render(request, "encyclopedia/new_page.html", {
                "error": "An encyclopedia entry with this title already exists.",
                "title": title,
                "content": content
            })
        
        # Save the new entry
        util.save_entry(title, content)
        return entry(request, title)
    
    return render(request, "encyclopedia/new_page.html")


def edit_page(request, title):
    """Handle editing an existing page."""
    if request.method == "POST":
        content = request.POST.get('content', '')
        util.save_entry(title, content)
        return entry(request, title)
    
    # Get existing content
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": f"Requested page '{title}' was not found."
        })
    
    return render(request, "encyclopedia/edit_page.html", {
        "title": title,
        "content": content
    })


def random_page(request):
    """Redirect to a random encyclopedia entry."""
    entries = util.list_entries()
    if not entries:
        return render(request, "encyclopedia/error.html", {
            "message": "No encyclopedia entries found."
        })
    
    random_title = random.choice(entries)
    return entry(request, random_title)

