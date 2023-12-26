from pathlib import Path

# some wonderful directories exist
# using them we can automate our task
path = Path()

python_count = 0
for file in path.glob('*.py'):
    python_count += 1
    print(file)

print(f'total number of python files: {python_count}')
