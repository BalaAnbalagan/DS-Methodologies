#!/usr/bin/env python3
"""Fix syntax errors in Jupyter notebooks"""
import json
import re
from pathlib import Path

def fix_print_statements(code):
    """Fix broken print statements with newlines"""
    # Fix print('Confusion matrix:\n', ... ) patterns
    code = re.sub(r"print\('([^']*)\n([^']*)',\s*", r"print('\1\\n\2', ", code)
    code = re.sub(r"print\('([^']*)\n([^']*)',\s*", r"print('\1\\n\2', ", code)  # Run twice for nested

    # Fix print statements with literal newlines in the middle
    lines = code.split('\n')
    fixed_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Check if this line has an unclosed print statement
        if "print('" in line and line.count("'") % 2 == 1 and not line.strip().endswith(')'):
            # Merge with next line
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                # Combine lines and escape the newline
                combined = line.rstrip() + '\\n' + next_line
                fixed_lines.append(combined)
                i += 2
                continue
        fixed_lines.append(line)
        i += 1

    return '\n'.join(fixed_lines)

def fix_notebook(notebook_path):
    """Fix syntax errors in a Jupyter notebook"""
    print(f"Fixing {notebook_path}...")

    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # Fix each code cell
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            source = cell.get('source', [])
            if isinstance(source, list):
                # Join lines and fix
                code = ''.join(source)
                fixed_code = fix_print_statements(code)
                # Split back into lines
                cell['source'] = fixed_code
            elif isinstance(source, str):
                fixed_code = fix_print_statements(source)
                cell['source'] = fixed_code

    # Save fixed notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    print(f"✅ Fixed {notebook_path}")

if __name__ == '__main__':
    notebooks = [
        'CRISP_DM/crisp_dm_walmart_sales.ipynb',
        'SEMMA/semma_student_performance.ipynb',
        'KDD/kdd_credit_fraud.ipynb'
    ]

    for nb_path in notebooks:
        if Path(nb_path).exists():
            fix_notebook(nb_path)
        else:
            print(f"⚠️  Not found: {nb_path}")

    print("\n✅ All notebooks fixed!")
