import typer
import os
from typing import Optional

app = typer.Typer(help="A CLI tool to organize files in a directory.")


FILE_CATEGORIES = {
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".jpeg": "Images",

    ".avi": "Videos",
    ".mov": "Videos",

    ".pdf": "PDFs",
    ".txt": "Text",
    ".docx": "Word",
    ".xlsx": "Excel",
    ".pptx": "PowerPoint",
    ".ppt": "PowerPoint",
    ".csv": "CSV",

    ".mp3": "Music",
    ".wav": "Music",
    ".flac": "Music",

    ".mp4": "Videos",
    ".webm": "Videos",
    ".webp": "Videos",
    ".mov":"Videos",

    # Languages 
    ".py": "Python",
    ".java": "Java",
    ".c": "C",
    ".cpp": "C++",
    ".js": "WEB",
    ".html": "WEB",
    ".css": "WEB", 
    ".zip": "Archives",
    
    ".rar": "Archives",
    ".tar": "Archives",

    ".exe": "Executables",
    ".torrent": "Torrents",

    ".app": "Applications",
    ".apk": "Applications",


}

@app.command()
def organize(directory: str = typer.Argument(".", help="Directory to organize")):

    if not os.path.isdir(directory):
        typer.echo(f"Error: '{directory}' is not a valid directory.")
        raise typer.Exit(code=1)


    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            
            _, ext = os.path.splitext(filename)
            ext = ext.lower()
            
            target_folder = FILE_CATEGORIES.get(ext, "Others")
            target_path = os.path.join(directory, target_folder)
            
            os.makedirs(target_path, exist_ok=True)
            
            new_path = os.path.join(target_path, filename)
            try:
                os.rename(file_path, new_path)
                typer.echo(f"Moved '{filename}' to '{target_folder}'")
            except OSError as e:
                typer.echo(f"Error moving '{filename}': {e}")




@app.command()
def stats(directory: str = typer.Argument(".", help="Directory to analyze")):
    """Show statistics about files in the directory."""
    if not os.path.isdir(directory):
        typer.echo(f"Error: '{directory}' is not a valid directory.")
        raise typer.Exit(code=1)
    
    file_counts = {}
    total_size = 0
    total_files = 0
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            ext = ext.lower()
            category = FILE_CATEGORIES.get(ext, "Others")
            
            file_counts[category] = file_counts.get(category, 0) + 1
            total_size += os.path.getsize(file_path)
            total_files += 1
    
    typer.echo(f"\n📊 Directory Statistics for '{directory}':")
    typer.echo(f"Total files: {total_files}")
    typer.echo(f"Total size: {total_size / (1024*1024):.2f} MB")
    typer.echo("\nFiles by category:")
    for category, count in sorted(file_counts.items()):
        typer.echo(f"  {category}: {count} files")





@app.command()
def clean(directory: str = typer.Argument(".", help="Directory to clean empty folders from")):
    if not os.path.isdir(directory):
        typer.echo(f"Error: '{directory}' is not a valid directory.")
        raise typer.Exit(code=1)

    for root, dirs, _ in os.walk(directory, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            try:
                if not os.listdir(folder_path):  # Check if folder is empty
                    os.rmdir(folder_path)
                    typer.echo(f"Deleted empty folder: '{folder_path}'")
            except OSError as e:
                typer.echo(f"Error deleting '{folder_path}': {e}")





@app.command()
def list_categories():
    """List all file categories and their extensions."""
    categories = {}
    for ext, cat in FILE_CATEGORIES.items():
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(ext)
    
    typer.echo("📁 File Categories:")
    for category, extensions in sorted(categories.items()):
        typer.echo(f"  {category}: {', '.join(extensions)}")






@app.command()
def add_category(ext: str, category: str):
    """Add a new file category."""
    FILE_CATEGORIES[ext.lower()] = category
    typer.echo(f"Added category '{category}' for extension '{ext}'")





@app.command()
def remove_category(ext: str):
    """Remove a file category."""
    if ext in FILE_CATEGORIES:
        del FILE_CATEGORIES[ext]
        typer.echo(f"Removed category for extension '{ext}'")
    else:
        typer.echo(f"Error: No category found for extension '{ext}'")





@app.command()
def undoorganize(directory: str = typer.Argument(".", help="Directory to undo organize from")):
    if not os.path.isdir(directory):
        typer.echo(f"Error: '{directory}' is not a valid directory.")
        raise typer.Exit(code=1)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            ext = ext.lower()
            
            target_folder = FILE_CATEGORIES.get(ext, "Others")
            target_path = os.path.join(directory, target_folder)
            
            os.makedirs(target_path, exist_ok=True)
            
            new_path = os.path.join(target_path, filename)
            try:
                os.rename(file_path, new_path)
                typer.echo(f"Moved '{filename}' to '{target_folder}'")
            except OSError as e:
                typer.echo(f"Error moving '{filename}': {e}")





if __name__ == "__main__":
    app()