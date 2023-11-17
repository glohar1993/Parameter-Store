import json
import os
from datetime import datetime

# HTML table initialization
html_table = """
<html>
<body>
<table border='1'>
<tr>
    <th>Parameter Name</th>
    <th>File Name</th>
    <th>Creation Date</th>
</tr>
"""

# Iterate over files in the s3_contents directory
for filename in os.listdir('s3_contents'):
    if filename.endswith('.json'):
        with open(f's3_contents/{filename}', 'r') as file:
            data = json.load(file)
            param_name = data.get('Name', 'N/A')
            creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Replace with actual creation date if available

            # Add row to HTML table
            html_table += f"<tr><td>{param_name}</td><td>{filename}</td><td>{creation_date}</td></tr>"

            # Print details to console
            print(f"Parameter Name: {param_name}, File Name: {filename}, Creation Date: {creation_date}")

# Finalize HTML table
html_table += """
</table>
</body>
</html>
"""

# Write HTML table to file
with open("table.html", "w") as file:
    file.write(html_table)

print("HTML table generated.")
