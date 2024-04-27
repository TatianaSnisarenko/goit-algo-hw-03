from pathlib import Path
from error_handling import error_handler
import os


def copy_file(source: Path, dist: Path) -> str:
    if not has_access(source):
        raise ValueError(f'До файлу {source} немає доступу')
    extention = source.name.split('.')[-1]
    dist_path = dist / extention
    dist_path.mkdir(parents=True, exist_ok=True)
    with open(source, 'rb') as src_file, open(dist_path / source.name, 'wb') as dst_file:
        byte_content = src_file.read()
        dst_file.write(byte_content)
    return f'Файл {source} скопійовано'


def copy_folder(source: Path, dist: Path) -> str:
    if not source.exists():
        return f'папка {source} не існує'
    if not has_access(source):
        raise ValueError(f'До папки {source} немає доступу')
    if source.is_file():
        return copy_file(source, dist)
    for child in source.iterdir():
        copy_folder(child, dist)
    return f'Всі доступні файли папки {source} скопійовані в папку {dist}'


def get_paths(source, dist):
    if not source or not source.strip():
        raise ValueError('Шлях до папки, що має бути скопійована не надано')
    source_path = Path(source.strip())
    if not dist or not dist.strip():
        output_path = Path('dist')
    else:
        output_path = Path(dist.strip())
    return source_path, output_path


def has_access(file_path: Path) -> bool:
    if os.access(file_path, os.R_OK):
        return True
    return False


@error_handler
def copy(source: str, dist: str) -> str:
    source_path, output_path = get_paths(source, dist)
    return copy_folder(source_path, output_path)
