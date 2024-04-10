# Invoice_generator

King Hardware Invoice Generator
This project generates invoices for King Hardware, a fictional hardware store. It uses the Questionary library to gather user input, such as the client's name and the items purchased, and generates a PDF invoice using the FPDF library.
Requirements

    Python 3.x
    Questionary library
    FPDF library

Usage

    Install the required libraries using pip:

    pip install questionary fpdf

Run the script using the following command:

python invoice_generator.py

    Follow the prompts to enter the client's name and the items purchased, including the quantity and unit price.
    The script will generate a PDF invoice with the client's name, address, and the items purchased, including the subtotal, discount, VAT, and total.

Structure

    invoice_generator.py: The main script that generates the invoice.
    icons8-hardware-64.png: An icon used in the invoice's header.

Limitations

    The project assumes that the client's address is "Default" and does not prompt the user to enter it.
    The project does not validate the user input, such as the client's name or the items purchased.

Future Work

    Add validation for the user input.
    Allow the user to enter the client's address.
    Add more options for the items purchased, such as different types of steel beams or planks.

Contributors

    [Your Name]

Acknowledgements

    Questionary library: https://github.com/tmbo/questionary
    FPDF library: https://github.com/reingart/fpdf



