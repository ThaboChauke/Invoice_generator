# Invoice Generator


## Overview

The Invoice Generator is a Python script designed to streamline the process of creating invoices for businesses. This script allows users to input client information, select products, apply discounts if necessary, and generate PDF invoices.

## Features

- **Client Information**: Input client details such as name and address.
- **Product Selection**: Choose from a list of available products.
- **Discount Application**: Apply discounts to the total invoice amount.
- **VAT Calculation**: Automatically calculate VAT based on the invoice total.
- **PDF Generation**: Generate a PDF invoice with all relevant details.

## Installation

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine:

   - git clone https://github.com/your-username/king-hardware-invoice-generator.git

## Requirements

    - Questionary library
    - FPDF library

- Install the required dependencies using pip:
    - pip install -r requirements.txt

## Usage

1. Run the invoice_generator.py script:

    - python invoice_generator.py

2. Follow the prompts to input client information, select products, and apply discounts.

3. Once all information has been provided, the script will generate a PDF invoice in the current directory.

## Acknowledgements

    Questionary library: https://github.com/tmbo/questionary
    FPDF library: https://github.com/reingart/fpdf
