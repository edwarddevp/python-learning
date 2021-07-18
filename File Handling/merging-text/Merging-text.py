import datetime
import glob2

files_with_text_to_merge = glob2.glob('files-to-merge/*.txt')

fileName = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')

with open(fileName + '.txt', 'w') as file_result:
    for item in files_with_text_to_merge:
        with open(item, 'r') as file:
            file_result.write(file.read() + "\n")
