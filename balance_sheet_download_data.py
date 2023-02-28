import PyPDF2
# Define a function to extract the numerical value associated with a keyword
def extract_value(text, keyword):
    value = ''
    for char in text[text.lower().index(keyword.lower()) + len(keyword):]:
        if char.isdigit() or char == '.':
            value += char
        elif char == ',' or char == ' ':
            continue
        elif value:
            break
    return float(value)

# Open the PDF file and read its contents
with open('balance_sheet_example.pdf', 'rb') as f:
    pdf_reader = PyPDF2.PdfReader(f)
    text = ''
    for i in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[i].extract_text()

balance_sheet_variables = {
    'Total Assets': ['total assets', 'assets'],
    'Total Liabilities': ['total liabilities', 'liabilities'],
    'Total Equity': ['total equity', 'equity'],
    'Total Current Assets': ['total current assets'],
    'Total Non-Current Assets': ['total non-current assets'],
    'Cash and Cash Equivalents': ['cash and cash equivalents'],
    'Accounts Receivable': ['accounts receivable', 'trade receivables'],
    'Inventories': ['inventories'],
    'Property, Plant, and Equipment': ['property, plant, and equipment', 'ppe'],
    'Goodwill': ['goodwill'],
    'Intangible Assets': ['intangible assets'],
    'Total Current Liabilities': ['total current liabilities'],
    'Total Non-Current Liabilities': ['total non-current liabilities'],
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
with open('income_statement_download_data.pdf', 'rb') as f:
    pdf_reader = PyPDF2.PdfReader(f)
    text = ''
    for i in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[i].extract_text()

income_statement_variables = {
    'Net Sales': ['net sales', 'sales'],
    'Cost of Goods Sold': ['cost of goods sold', 'cost of sales'],
    'Gross Profit': ['gross profit'],
    'Operating Expenses': ['operating expenses'],
    'Operating Income': ['operating income', 'earnings before interest and taxes', 'ebit'],
    'Net Operating Income': ['net operating income', 'operating profit'],
    'EBITDA': ['ebitda'],
    'Interest Expense': ['interest expense'],
    'Income Tax Expense': ['income tax expense'],
    'Net Income': ['net income', 'income'],
}
income_statement_results = {}
for var_name, var_keywords in income_statement_variables.items():
    for keyword in var_keywords:
        if keyword.lower() in text.lower():
            value = extract_value(text, keyword)
            income_statement_results[var_name] = value
            break


balance_sheet_results = {}
for var_name, var_keywords in balance_sheet_variables.items():
    for keyword in var_keywords:
        if keyword.lower() in text.lower():
            value = extract_value(text, keyword)
            balance_sheet_results[var_name] = value
            break

# Calculate financial multiples based on the extracted variables
if 'Total Assets' in results and 'Total Equity' in results and 'Net Income'in results:
    results['Return on Equity'] = results['Net Income'] / results['Total Equity']
    results['Asset Turnover'] = results['Net Income'] / results['Total Assets']
results['Total Liabilities and Equity']= results['Total Liabilities']+results['Total Equity']
# Print the results
for var_name, value in results.items():
    print(f'{var_name}: {value}')

