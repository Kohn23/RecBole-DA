# replace_imports.py
import os
import re


def replace_in_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 替换导入语句
                new_content = re.sub(r'from recbole\.', 'from recbole_da.', content)
                new_content = re.sub(r'import recbole_da', 'import recbole_da_da', new_content)

                if content != new_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"修改了: {file_path}")


if __name__ == "__main__":
    directory = r"C:\Users\Kohn\Cache\Python\RecBole-DA"
    replace_in_files(directory)