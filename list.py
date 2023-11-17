import json
import os
from datetime import datetime

html_table = """
<table>
<tr>
    <th>Parameter Name</th>
    <th>File Name</th>
    <th>Creation Date</th>
</tr>
"""

for filename in os.listdir('s3_contents'):
    if filename.endswith('.json'):
        with open(f's3_contents/{filename}', 'r') as file:
            data = json.load(file)
            param_name = data.get('Name', 'N/A')
            creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Replace with actual creation date if available
            html_table += f"<tr><td>{param_name}</td><td>{filename}</td><td>{creation_date}</td></tr>"

html_table += "</table>"

with open("table.html", "w") as file:
    file.write(html_table)
