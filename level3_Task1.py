from bs4 import BeautifulSoup

file_path = "response.html"

with open(file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

print("----- HEADINGS -----")
for i in range(1, 7):
    for h in soup.find_all(f"h{i}"):
        print(f"h{i}:", h.text.strip())

print("\n----- PARAGRAPHS -----")
for p in soup.find_all("p"):
    print(p.text.strip())

print("\n----- IMAGES -----")
for img in soup.find_all("img"):
    print("Image URL:", img.get("src"))

print("\n----- LINKS -----")
for a in soup.find_all("a", href=True):
    print("Link:", a["href"])
