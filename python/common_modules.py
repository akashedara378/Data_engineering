import os

# Get current working directory
print(os.getcwd())

# List files and directories in the current directory
print(os.listdir('.'))

# Create a new directory
os.mkdir('new_directory')

# Remove a file or directory
os.remove('file.txt')  # Use os.rmdir('new_directory') to remove a directory

full_path = os.path.join('directory', 'file.txt')
os.getenv('HOME')



from datetime import datetime, timedelta

# Get the current date and time
now = datetime.now()
print(now)

# Create a specific date
specific_date = datetime(2024, 8, 3)
print(specific_date)

