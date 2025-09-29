# Hotel Itemizer - Updated Requirements Summary

## Key Changes Based on Your Feedback

### 1. **Workflow Clarification**
- **Step 1**: File uploaded (primarily PDF hotel invoices)
- **Step 2**: AI model analyzes and extracts values/line items
- **Step 3**: User validates and categorizes the extracted information 
- **Step 4**: System creates consolidated expenses by category for MS Expense

### 2. **File Format Focus**
- Primary support for PDF hotel invoices
- Secondary support for image formats if needed

### 3. **Exact Categories for MS Expense Integration**
```json
[
  {"title": "Daily Room Rate", "value": "Daily Room Rate"},
  {"title": "Hotel Deposit", "value": "Hotel Deposit"},
  {"title": "Hotel Tax", "value": "Hotel Tax"}, 
  {"title": "Hotel Telephone", "value": "Hotel Telephone"},
  {"title": "Incidentals", "value": "Incidentals"},
  {"title": "Laundry", "value": "Laundry"},
  {"title": "Room Service & Meals etc", "value": "Room Service & Meals etc"},
  {"title": "Ignore", "value": "Ignore"}
]
```

### 4. **MS Expense Interface Integration**
Based on your screenshots, the system needs to populate:

- **Subcategory**: Dropdown selection from hotel categories above
- **Start date**: Check-in date (6/26/2025 in your example)
- **Daily rate**: Calculated amount per day for each category 
- **Quantity**: Number of days (0 in screenshot, needs calculation)

The interface shows:
- **Total**: 100.00 (original expense amount)
- **Itemised**: 0.00 (sum of all itemized entries) 
- **Remaining**: 100.00 (Total - Itemised, must equal 0 when complete)

### 5. **Consolidation Rules**
- Only consolidate duplicate categories **after** user validation
- Show user what will be consolidated before applying
- Must maintain total amount validation (itemized = original total)

### 6. **UI Visibility**
- Hotel itemization UI only appears when expense is detected/identified as hotel-related
- Integration with existing expense workflow and interface

## Technical Implementation Focus

### Core Modules to Create:
1. **`hotel_extractor.py`** - AI-powered PDF invoice extraction
2. **`hotel_categorizer.py`** - Category suggestion and validation logic  
3. **`daily_rate_calculator.py`** - Calculate daily rates and quantities
4. **`hotel_validator.py`** - Consolidation and total validation
5. **`models.py`** - Pydantic models for hotel data structures

### Frontend Components:
1. **Hotel validation interface** - Review extracted items and assign categories
2. **Consolidation preview** - Show what will be consolidated 
3. **MS Expense automation** - Playwright scripts to populate the itemization UI

### Key Integration Points:
1. **Existing expense workflow** - Detect hotel expenses and trigger itemization
2. **Playwright automation** - Populate MS Expense "Itemise expense" interface
3. **Category dropdown mapping** - Exact match with MS Expense subcategories
4. **Total validation** - Ensure itemized amounts equal original expense

## Ready for Agent Implementation

The requirements are now specific enough to begin implementation with the agent. The folder structure is in place and the technical specifications are clear.

**Next Steps:**
1. Confirm these updated requirements meet your needs
2. Begin implementation with GitHub Copilot agent mode
3. Start with core backend modules (extraction, categorization)
4. Build frontend validation interface 
5. Implement MS Expense integration via Playwright

Would you like to proceed with the agent implementation or need any clarifications on these requirements?