import pytest
import os
import shutil

# Пример чистых функций
def test_calculate_sum():
    from my_account import calculate_sum
    assert calculate_sum(1, 2) == 3
    assert calculate_sum(-1, 1) == 0
    assert calculate_sum(0, 0) == 0

def test_quiz_score():
    from quiz import calculate_score
    assert calculate_score([True, False, True]) == 2
    assert calculate_score([False, False, False]) == 0
    assert calculate_score([True, True, True]) == 3

# Пример грязных функций
def test_copy_file(tmp_path):
    src = tmp_path / "source.txt"
    dest = tmp_path / "destination.txt"
    src.write_text("Hello, world!")
    
    shutil.copy(src, dest)
    
    assert dest.read_text() == "Hello, world!"

def test_copy_directory(tmp_path):
    src_dir = tmp_path / "src"
    dest_dir = tmp_path / "dest"
    src_dir.mkdir()
    (src_dir / "file.txt").write_text("Hello, world!")
    
    shutil.copytree(src_dir, dest_dir)
    
    assert (dest_dir / "file.txt").read_text() == "Hello, world!"
