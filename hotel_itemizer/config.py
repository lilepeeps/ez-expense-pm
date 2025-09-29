"""
Hotel Itemizer Configuration

This module contains configuration constants and data structures
specific to the Hotel Itemizer feature.
"""

# Hotel expense categories that align with MS Expense system subcategories
HOTEL_CATEGORIES = [
    {
        "title": "Daily Room Rate",
        "value": "Daily Room Rate",
        "description": "Base room rate charged per night",
        "is_daily": True
    },
    {
        "title": "Hotel Deposit", 
        "value": "Hotel Deposit",
        "description": "Security deposit or advance payment",
        "is_daily": False
    },
    {
        "title": "Hotel Tax",
        "value": "Hotel Tax", 
        "description": "All taxes (occupancy, city, VAT, etc.)",
        "is_daily": True
    },
    {
        "title": "Hotel Telephone",
        "value": "Hotel Telephone",
        "description": "Phone charges and communication fees", 
        "is_daily": False
    },
    {
        "title": "Incidentals",
        "value": "Incidentals",
        "description": "Miscellaneous charges and fees",
        "is_daily": False
    },
    {
        "title": "Laundry", 
        "value": "Laundry",
        "description": "Laundry and valet services",
        "is_daily": False
    },
    {
        "title": "Room Service & Meals etc",
        "value": "Room Service & Meals etc", 
        "description": "Food, beverage, and room service charges",
        "is_daily": False
    },
    {
        "title": "Ignore",
        "value": "Ignore",
        "description": "Items to exclude from itemization (credits, personal expenses)",
        "is_daily": False
    }
]

# Categories that should be calculated as daily rates vs one-time charges
DAILY_RATE_CATEGORIES = ["Daily Room Rate", "Hotel Tax"]
ONE_TIME_CATEGORIES = ["Hotel Deposit", "Hotel Telephone", "Incidentals", "Laundry", "Room Service & Meals etc"]
EXCLUDE_CATEGORIES = ["Ignore"]

# AI prompts for hotel invoice extraction
HOTEL_EXTRACTION_PROMPT = """
You are analyzing a hotel invoice. Extract all line items with their descriptions and amounts.
Look for the following types of charges and categorize them appropriately:

- Room rates (nightly charges)
- Taxes (occupancy tax, city tax, VAT, sales tax, etc.)
- Deposits or advance payments
- Telephone or communication charges  
- Incidental charges or miscellaneous fees
- Laundry or valet services
- Food, beverage, or room service charges

Also extract:
- Check-in date
- Check-out date  
- Hotel name and location
- Total invoice amount

Return the data in a structured format that can be used for expense itemization.
"""

HOTEL_CATEGORIZATION_PROMPT = """
Based on the extracted hotel invoice line items, suggest the most appropriate category 
from this list for each item:

- Daily Room Rate: Base room rate charged per night
- Hotel Deposit: Security deposit or advance payment  
- Hotel Tax: All taxes (occupancy, city, VAT, etc.)
- Hotel Telephone: Phone charges and communication fees
- Incidentals: Miscellaneous charges and fees
- Laundry: Laundry and valet services  
- Room Service & Meals etc: Food, beverage, and room service charges
- Ignore: Items to exclude (credits, personal expenses)

Consider the description and amount to make the best categorization suggestion.
"""