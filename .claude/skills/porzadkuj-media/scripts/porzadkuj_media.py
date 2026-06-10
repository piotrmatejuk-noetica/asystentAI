#!/usr/bin/env python3
"""
Skrypt do porządkowania mediów w workspace Obsidian.

Funkcje:
1. Grafiki linkowane we wpisach → zmiana nazwy na YYYY-MM-DD.png
2. PDFy → przeniesienie do Zasoby/dokumenty/ z logiem użycia
3. Raport osieroconych plików
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Konfiguracja ścieżek - używamy cwd() bo Claude Code uruchamia z workspace root
WORKSPACE = Path.cwd()
MEDIA_FOLDER = WORKSPACE / "Marketing" / "media"
WPISY_FOLDER = WORKSPACE / "Marketing" / "wpisy"
DOKUMENTY_FOLDER = WORKSPACE / "Zasoby" / "dokumenty"
ROOT_FOLDER = WORKSPACE

# Rozszerzenia
IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg'}
VIDEO_EXTENSIONS = {'.mp4', '.mov', '.webm', '.avi', '.mkv'}
PDF_EXTENSION = '.pdf'


def find_all_media_files():
    """Znajduje wszystkie pliki mediów w głównym folderze i Marketing/media/."""
    media_files = {
        'images': [],
        'videos': [],
        'pdfs': []
    }

    # Główny folder (tylko pliki, nie foldery)
    for file in ROOT_FOLDER.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            if ext in IMAGE_EXTENSIONS:
                media_files['images'].append(file)
            elif ext in VIDEO_EXTENSIONS:
                media_files['videos'].append(file)
            elif ext == PDF_EXTENSION:
                media_files['pdfs'].append(file)

    # Marketing/media/
    if MEDIA_FOLDER.exists():
        for file in MEDIA_FOLDER.iterdir():
            if file.is_file():
                ext = file.suffix.lower()
                if ext in IMAGE_EXTENSIONS:
                    media_files['images'].append(file)
                elif ext in VIDEO_EXTENSIONS:
                    media_files['videos'].append(file)
                elif ext == PDF_EXTENSION:
                    media_files['pdfs'].append(file)

    return media_files


def find_all_markdown_files():
    """Znajduje wszystkie pliki .md w workspace."""
    md_files = []
    excluded = ['.git', '.obsidian', '.claude']
    for md_file in WORKSPACE.rglob("*.md"):
        if not any(exc in str(md_file) for exc in excluded):
            md_files.append(md_file)
    return md_files


def find_media_usage(media_files, md_files):
    """
    Znajduje gdzie są używane pliki mediów.
    Zwraca dict: {media_path: [list of md_files using it]}
    """
    usage = defaultdict(list)

    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
        except Exception:
            continue

        for media_file in media_files:
            filename = media_file.name

            patterns = [
                rf'\!\[\[{re.escape(filename)}\]\]',  # ![[file]]
                rf'\[\[{re.escape(filename)}\]\]',    # [[file]]
                rf'\!\[.*?\]\([^)]*{re.escape(filename)}[^)]*\)',  # ![](path/file)
                rf'\[.*?\]\([^)]*{re.escape(filename)}[^)]*\)',    # [](path/file)
                re.escape(filename),  # sama nazwa pliku jako tekst
            ]

            for pattern in patterns:
                if re.search(pattern, content):
                    usage[media_file].append(md_file)
                    break

    return usage


def get_wpis_date_from_path(md_path):
    """Wyciąga datę z nazwy pliku wpisu (YYYY-MM-DD.md)."""
    match = re.match(r'(\d{4}-\d{2}-\d{2})\.md$', md_path.name)
    if match:
        return match.group(1)
    return None


def is_generic_filename(filename):
    """Sprawdza czy nazwa pliku jest generyczna (do zmiany)."""
    generic_patterns = [
        r'^Pasted image \d+\.',
        r'^\d{13,}-[a-z0-9]+\.',
        r'^Screen Capture .+\.',
        r'^Screenshot .+\.',
        r'^IMG_\d+\.',
        r'^image\d*\.',
    ]
    for pattern in generic_patterns:
        if re.match(pattern, filename, re.IGNORECASE):
            return True
    return False


def rename_media_for_wpis(media_path, wpis_path):
    """
    Zmienia nazwę pliku media na pasującą do wpisu.
    Zwraca (nowa_ścieżka, czy_zmieniono).
    """
    date_str = get_wpis_date_from_path(wpis_path)
    if not date_str:
        return media_path, False

    ext = media_path.suffix.lower()
    new_name = f"{date_str}{ext}"
    new_path = MEDIA_FOLDER / new_name

    # Jeśli już istnieje plik o tej nazwie, dodaj suffix
    counter = 1
    while new_path.exists() and new_path != media_path:
        new_name = f"{date_str}_{counter}{ext}"
        new_path = MEDIA_FOLDER / new_name
        counter += 1

    if new_path == media_path:
        return media_path, False

    MEDIA_FOLDER.mkdir(parents=True, exist_ok=True)
    shutil.move(str(media_path), str(new_path))

    return new_path, True


def update_links_in_file(md_path, old_name, new_name):
    """Aktualizuje linki w pliku markdown."""
    try:
        content = md_path.read_text(encoding='utf-8')
    except Exception:
        return False

    new_content = content.replace(f'![[{old_name}]]', f'![[{new_name}]]')
    new_content = new_content.replace(f'[[{old_name}]]', f'[[{new_name}]]')

    new_content = re.sub(
        rf'(\!\[.*?\]\([^)]*){re.escape(old_name)}([^)]*\))',
        rf'\1{new_name}\2',
        new_content
    )

    if new_content != content:
        md_path.write_text(new_content, encoding='utf-8')
        return True
    return False


def move_pdf_to_dokumenty(pdf_path, usage_info):
    """Przenosi PDF do Zasoby/dokumenty/."""
    new_path = DOKUMENTY_FOLDER / pdf_path.name

    counter = 1
    while new_path.exists():
        stem = pdf_path.stem
        new_path = DOKUMENTY_FOLDER / f"{stem}_{counter}.pdf"
        counter += 1

    DOKUMENTY_FOLDER.mkdir(parents=True, exist_ok=True)
    shutil.move(str(pdf_path), str(new_path))

    return new_path


def run_cleanup():
    """Główna funkcja porządkowania."""
    print("=" * 60)
    print("PORZĄDKOWANIE MEDIÓW")
    print(f"Workspace: {WORKSPACE}")
    print("=" * 60)
    print()

    # 1. Znajdź wszystkie pliki
    media_files = find_all_media_files()
    md_files = find_all_markdown_files()

    all_media = media_files['images'] + media_files['videos'] + media_files['pdfs']
    usage = find_media_usage(all_media, md_files)

    print(f"Znaleziono: {len(media_files['images'])} grafik, {len(media_files['videos'])} wideo, {len(media_files['pdfs'])} PDFów")
    print(f"Plików markdown: {len(md_files)}")
    print()

    stats = {
        'images_renamed': 0,
        'images_orphaned': 0,
        'videos_renamed': 0,
        'videos_orphaned': 0,
        'pdfs_moved': 0
    }

    # 2. Przetwórz grafiki
    print("-" * 40)
    print("GRAFIKI")
    print("-" * 40)

    for image in media_files['images']:
        used_in = usage.get(image, [])
        wpis_files = [f for f in used_in if 'wpisy' in str(f)]

        if wpis_files:
            if not is_generic_filename(image.name):
                continue

            wpis = wpis_files[0]
            old_name = image.name
            new_path, changed = rename_media_for_wpis(image, wpis)

            if changed:
                stats['images_renamed'] += 1
                print(f"✓ {old_name} → {new_path.name}")

                for md_file in used_in:
                    updated = update_links_in_file(md_file, old_name, new_path.name)
                    if updated:
                        print(f"  └─ Zaktualizowano link w: {md_file.name}")
        elif not used_in:
            stats['images_orphaned'] += 1
            print(f"⚠ Osierocona: {image.name}")

    print(f"\nZmieniono nazwy: {stats['images_renamed']} grafik")
    print()

    # 3. Przetwórz wideo
    print("-" * 40)
    print("WIDEO")
    print("-" * 40)

    for video in media_files['videos']:
        used_in = usage.get(video, [])
        wpis_files = [f for f in used_in if 'wpisy' in str(f)]

        if wpis_files:
            wpis = wpis_files[0]
            old_name = video.name
            new_path, changed = rename_media_for_wpis(video, wpis)

            if changed:
                stats['videos_renamed'] += 1
                print(f"✓ {old_name} → {new_path.name}")

                for md_file in used_in:
                    updated = update_links_in_file(md_file, old_name, new_path.name)
                    if updated:
                        print(f"  └─ Zaktualizowano link w: {md_file.name}")
            else:
                print(f"· {video.name} (już ma poprawną nazwę)")
        elif not used_in:
            stats['videos_orphaned'] += 1
            print(f"⚠ Osierocone: {video.name}")

    print(f"\nZmieniono nazwy: {stats['videos_renamed']} wideo")
    print()

    # 4. Przetwórz PDFy
    print("-" * 40)
    print("PDFy → Zasoby/dokumenty/")
    print("-" * 40)

    for pdf in media_files['pdfs']:
        used_in = usage.get(pdf, [])
        old_name = pdf.name
        new_path = move_pdf_to_dokumenty(pdf, used_in)
        stats['pdfs_moved'] += 1

        print(f"✓ {old_name} → {new_path.relative_to(WORKSPACE)}")
        if used_in:
            for md_file in used_in:
                print(f"  └─ Używany w: {md_file.relative_to(WORKSPACE)}")
                update_links_in_file(md_file, old_name, new_path.name)
        else:
            print(f"  └─ (nieużywany)")

    print(f"\nPrzeniesiono: {stats['pdfs_moved']} PDFów")
    print()

    # 5. Podsumowanie
    print("=" * 60)
    print("PODSUMOWANIE")
    print("=" * 60)
    print(f"📸 Grafiki: {stats['images_renamed']} przemianowane, {stats['images_orphaned']} osieroconych")
    print(f"🎬 Wideo: {stats['videos_renamed']} przemianowane, {stats['videos_orphaned']} osieroconych")
    print(f"📄 PDFy: {stats['pdfs_moved']} przeniesionych do Zasoby/dokumenty/")


if __name__ == "__main__":
    run_cleanup()