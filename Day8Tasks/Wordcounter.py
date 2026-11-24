#Word counter program

try:
    with open("article.txt", "r") as f:
        content = f.read()

    lines = len(content.splitlines())
    words = len(content.split())
    characters = len(content)

    print("Lines      :", lines)
    print("Words      :", words)
    print("Characters :", characters)
except FileNotFoundError:
    print("article.txt not found.")
