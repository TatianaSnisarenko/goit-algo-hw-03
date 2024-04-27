from copy_folder import copy

if __name__ == "__main__":

    source_path = None
    while not source_path:
        source_path = input(
            'Введіть шлях до папки, що має бути скопійована у форматі parent_folder/folder_to_copy  >>>  ')
    dist_path = input(
        'Введіть шлях до папки, куди має бути скопійована інформація parent_folder/output_folder  >>>  ')

    print(copy(source_path, dist_path))
