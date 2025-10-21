
def update_html(user_input):
    # Read the existing HTML file
    file_path = "templates/index.html"
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    separator = "<br><br><label"
    split_index = html.find(separator)

    # Split, inject the user input, and concatenate
    before = html[:split_index]
    after = html[split_index:]
    injected = f'<br>{user_input}\n'
    new_html = before + injected + after

    # Overwrite the HTML file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_html)

