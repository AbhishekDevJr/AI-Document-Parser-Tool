import json
import os

from typing import List, Optional
from pydantic import BaseModel, Field
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

class LineItem(BaseModel):
    description: str = Field(description="Description of the Product or Service")
    quantity: Optional[float] = Field(default=None, description="Quantity Purchased of the Product or Service")
    unit_price: Optional[float] = Field(default=None, description="Price Per Unit")
    amount: float = Field(description="Total Price of this Line Item")
    
class InvoiceData(BaseModel):
    vendor_name: str = Field(description="Name of the Company/Vendor Issuing the Invoice")
    invoice_number: str = Field(description="Unique Identifier Number of the Invoice")
    invoice_date: str = Field(description="Invoice Issue Date (DD-MM-YYYY)")
    due_date: Optional[str] = Field(default=None, description="Payment Due Date of the Invoice (DD-MM-YYYY)")
    currency: str = Field(default="INR", description="Currency Symbol or 3 Letter Code")
    line_items: List[LineItem] = Field(description="List of all Product or Service Line Items in the Invoice")
    subtotal: Optional[float] = Field(default=None, description="Subtotal of the Invoice Amount")
    tax_amount: Optional[float] = Field(default=None, description="Total Tax Amount on Invoice Amount")
    total_amount: float = Field(description="Final Total Amount of the Invoice")


def parse_invoice_pdf(invoice_file_path):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    print(f"Uploading Invoice File: {invoice_file_path}")
    uploaded_file = client.files.upload(file=invoice_file_path)
    
    llm_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            uploaded_file,
            "Extract all relevant invoice data accurately matching the requested schema."
        ],
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=InvoiceData,
            temperature=0.0
        )
    )
    
    return llm_response

result = parse_invoice_pdf("invoice.pdf")
print(result)