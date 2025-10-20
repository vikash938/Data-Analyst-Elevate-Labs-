import nbformat as nbf

# Create a Jupyter notebook
nb = nbf.v4.new_notebook()

# Add Markdown and Code cells describing and executing the cleaning process
cells = [
    nbf.v4.new_markdown_cell("""# Data Cleaning and Preprocessing Notebook

This notebook performs common data preprocessing operations:

1. Identify and handle missing values
2. Remove duplicates
3. Standardize text and categorical values
4. Convert date formats
5. Rename column headers
6. Fix data types"""),
    
    nbf.v4.new_code_cell("""import pandas as pd\nimport numpy as np\n\n# Step 1: Create a sample dataset with issues\ndata = {\n    'ID ': [1, 2, 3, 4, 4, 5, None, 7, 8, 9],\n    'Name ': ['Alice', 'Bob', 'Charlie', 'David', 'David', 'Eve', None, 'Frank', 'Grace', 'Henry'],\n    'Gender ': ['F', 'Male', 'M', 'male', 'Male', 'FEMALE', 'f', 'M', 'F', None],\n    'Country ': ['USA', 'usa', 'INDIA', 'India', 'UK', 'U.K.', 'Canada', None, 'canada', 'INDIA'],\n    'Age ': [25, 30, np.nan, 45, 45, 28, 33, 'Forty', 29, 31],\n    'Join Date ': ['2021-05-20', '15/06/2020', '2020.07.01', '2021/08/10', '2021/08/10', '9-5-2021', None, '2022-01-02', '03-02-2020', '2020-03-11']\n}\n\nraw_df = pd.DataFrame(data)\nraw_df.head()"""),
    
    nbf.v4.new_code_cell("""# Step 2: Handle missing values\nclean_df = raw_df.copy()\nclean_df = clean_df.dropna(subset=['Name '])\nclean_df['Age '] = clean_df['Age '].replace('Forty', np.nan)\nclean_df['Age '] = clean_df['Age '].astype(float)"""),
    
    nbf.v4.new_code_cell("""# Step 3: Remove duplicates\nclean_df = clean_df.drop_duplicates()"""),
    
    nbf.v4.new_code_cell("""# Step 4: Standardize text values\nclean_df['Gender '] = clean_df['Gender '].str.strip().str.lower().replace({'f': 'female', 'm': 'male'})\nclean_df['Country '] = clean_df['Country '].str.replace('.', '', regex=False).str.strip().str.title()"""),
    
    nbf.v4.new_code_cell("""# Step 5: Convert date formats\nclean_df['Join Date '] = pd.to_datetime(clean_df['Join Date '], errors='coerce', dayfirst=True)"""),
    
    nbf.v4.new_code_cell("""# Step 6: Rename columns\nclean_df.columns = clean_df.columns.str.strip().str.lower().str.replace(' ', '_')"""),
    
    nbf.v4.new_code_cell("""# Step 7: Fix data types\nclean_df['age'] = clean_df['age'].astype('Int64')"""),
    
    nbf.v4.new_code_cell("""# Save cleaned dataset\nclean_df.to_csv('cleaned_dataset.csv', index=False)\n\nclean_summary = {\n    'initial_rows': len(raw_df),\n    'after_cleaning_rows': len(clean_df),\n    'missing_values_handled': raw_df.isnull().sum().to_dict(),\n    'final_columns': clean_df.dtypes.to_dict()\n}\n\nclean_summary""")
]

# Add all the cells to the notebook
nb['cells'] = cells

# Save the notebook file
with open('data_cleaning_notebook.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

'Notebook saved as data_cleaning_notebook.ipynb'