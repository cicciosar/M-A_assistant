import PyPDF2

# Open the PDF file and read its contents
with open('balance_sheet.pdf', 'rb') as f:
    pdf_reader = PyPDF2.PdfFileReader(f)
    text = ''
    for i in range(pdf_reader.getNumPages()):
        text += pdf_reader.getPage(i).extractText()

# Define a dictionary of financial variables to search for
variables = {
    'Total Assets': ['total assets', 'assets'],
    'Total Liabilities': ['total liabilities', 'liabilities'],
    'Total Equity': ['total equity', 'equity'],
    'Current Assets': ['current assets'],
    'Cash and Cash Equivalents': ['cash and cash equivalents'],
    'Accounts Receivable': ['accounts receivable', 'trade receivables'],
    'Inventories': ['inventories'],
    'Property, Plant, and Equipment': ['property, plant, and equipment', 'ppe'],
    'Goodwill': ['goodwill'],
    'Intangible Assets': ['intangible assets'],
    'Current Liabilities': ['current liabilities'],
    'Accounts Payable': ['accounts payable', 'trade payables'],
    'Accrued Expenses': ['accrued expenses'],
    'Long-Term Liabilities': ['long-term liabilities'],
    'Long-Term Debt': ['long-term debt'],
    'Deferred Taxes': ['deferred taxes'],
    'Net Income': ['net income', 'income'],
    'Gross Profit': ['gross profit'],
    'Operating Income': ['operating income', 'earnings before interest and taxes', 'ebit'],
    'Net Operating Income': ['net operating income', 'operating profit'],
    'EBITDA': ['ebitda'],
    'Interest Expense': ['interest expense'],
    'Income Tax Expense': ['income tax expense'],
    'Depreciation and Amortization': ['depreciation and amortization', 'depreciation expense', 'amortization expense'],
}

# Search the text for each financial variable
results = {}
for var_name, var_keywords in variables.items():
    for keyword in var_keywords:
        if keyword.lower() in text.lower():
            # Extract the numerical value associated with the variable
            value = extract_value(text, keyword)
            results[var_name] = value
            break

# Calculate financial multiples based on the extracted variables
if 'Total Assets' in results and 'Total Equity' in results:
    results['Return on Equity'] = results['Net Income'] / results['Total Equity']
    results['Asset Turnover'] = results['Net Income'] / results['Total Assets']

# Print the results
for var_name, value in results.items():
    print(f'{var_name}: {value}')

# Define a function to extract the numerical value associated with a keyword
def extract_value(text, keyword):
    value = ''
    for char in text[text.lower().index(keyword.lower()) + len(keyword):]:
        if char.isdigit() or char == '.':
            value += char
        elif value:
            break
    return float(value)