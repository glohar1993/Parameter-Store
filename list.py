import json
import os

html_table = """
<html>
<body>
<table border='1'>
<tr>
    <th>Parameter Name</th>
    <th>File Name</th>
</tr>
"""

for filename in os.listdir('s3_contents'):
    if filename.endswith('.json'):
        with open(f's3_contents/{filename}', 'r') as file:
            data = json.load(file)
            param_name = data.get('Name', 'N/A')
            html_table += f"<tr><td>{param_name}</td><td>{filename}</td></tr>"

html_table += """
</table>
</body>
</html>
"""

with open("table.html", "w") as file:
    file.write(html_table)

print("HTML table generated.")
