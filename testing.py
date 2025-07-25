import os

directory ="test"
for root, dirs, _ in os.walk("/home/polo"):
    if directory in dirs:
        print(os.path.join(root,directory))