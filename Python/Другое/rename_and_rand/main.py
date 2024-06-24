import os
from random import choice

folder_path = 'files/'
count_files = len(
    [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
)
prefixes = [str(el) + '. ' for el in range(1, count_files + 1)]
for filename in os.listdir(folder_path):
    current_prefix = choice(prefixes)
    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, current_prefix + filename))
    prefixes.remove(current_prefix)

    
