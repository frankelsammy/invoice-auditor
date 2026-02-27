import requests
import pdfplumber

from dataclasses import dataclass

@dataclass
class ChargeInfo:
    base_charge: float
    extra_charges: float

invoice_url = "https://wmezpay.wm.com/WMI5000_DirectInvoice.aspx?id=hbaCf0KKicrEqAu6D6ed1zd2BnO4IyDq-aaDL2gGHpoqNsu-0mKCb4yKLB5UWBxYjG5WVXrYs9uhSnnd8RVa9QT6vyQQgfQGXypTwAsYVICVoQTMUXvZRBAiOTN6KV1IdB7uOnL1MoH6N0o7IhHxJq4d8wrnerhWBcn_4KY88ouNwP6k0quP_TRV1WNya_VZ"



def extract_invoice_data(pdf_path):
    # first build the full text from all pages
    full_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"

    # find the section between the two markers
    start_marker = "Description Date Ticket Quantity Amount"
    end_marker = "TotalCurrentCharges"

    start_idx = full_text.find(start_marker)
    end_idx = full_text.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        print("Could not find markers in text")
        return

    # extract just that section (excluding the markers themselves)
    section = full_text[start_idx + len(start_marker):end_idx]
    charges = ChargeInfo(base_charge=0.0, extra_charges=0.0)
    # print each line
    for line in section.strip().splitlines():
        if line.strip():  # skip blank lines
            split_line = line.split()
            description = split_line[0]
            amount = split_line[-1]
            if "offset" in description.lower():
                charges.extra_charges += float(amount)
            else:
                charges.base_charge += float(amount)
    print(charges)

if __name__ == "__main__":
    extract_invoice_data("invoice2.pdf")