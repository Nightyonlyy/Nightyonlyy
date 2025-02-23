from datetime import date

birth_date = date(2003, 8, 30)
today = date.today()
age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

readme_path = "README.md"

with open(readme_path, "r", encoding="utf-8") as file:
    content = file.read()

updated_content = content.replace("{{AGE}}", str(age))

with open(readme_path, "w", encoding="utf-8") as file:
    file.write(updated_content)
