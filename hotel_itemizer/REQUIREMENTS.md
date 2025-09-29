# Hotel Itemizer Feature Requirements

## Overview
The Hotel Itemizer is a specialized feature within the EZ-Expense system that provides detailed itemization capabilities for hotel expenses. This feature extends the existing expense processing workflow with hotel-specific categorization, consolidation, and daily rate calculations.

## Feature Scope

### Primary Objectives
1. **Enhanced Hotel Expense Processing**: Automatically extract and categorize line items from hotel invoices
2. **Category Validation & Consolidation**: Allow users to validate and consolidate duplicate categories
3. **Daily Rate Calculation**: Break down multi-day hotel stays into daily rates and quantities
4. **Seamless Integration**: Work within the existing EZ-Expense workflow and UI

## Functional Requirements

### FR1: Hotel Expense Detection & Workflow
- **FR1.1**: Hotel expense itemization workflow shall follow this sequence:
  1. **File Upload**: User uploads hotel invoice (primarily PDF format)
  2. **AI Analysis**: AI model analyzes and extracts line items and values from the invoice
  3. **User Validation**: Present extracted information to user for validation and categorization
  4. **Consolidation**: Use validated categorization to create consolidated expenses by category
- **FR1.2**: Hotel itemization UI shall only appear when expense is detected/identified as hotel-related
- **FR1.3**: System shall use AI-based detection from invoice content to identify hotel expenses

### FR2: Invoice Processing & Extraction
- **FR2.1**: System shall primarily process hotel invoices in PDF format (with secondary support for images)
- **FR2.2**: System shall extract the following information using AI:
  - Line items with descriptions and amounts
  - Check-in and check-out dates
  - Hotel name and location
  - Total amount for validation
- **FR2.3**: System shall use Azure OpenAI to parse and suggest categorization for extracted items

### FR3: Hotel Category Management
- **FR3.1**: System shall support the following predefined hotel expense categories:
  - "Daily Room Rate"
  - "Hotel Deposit"
  - "Hotel Tax"
  - "Hotel Telephone"
  - "Incidentals"
  - "Laundry"
  - "Room Service & Meals etc"
  - "Ignore" (for items to be excluded from itemization - credits, personal expenses, etc.)
- **FR3.2**: Categories shall follow the exact naming convention as specified for MS Expense integration
- **FR3.3**: System shall suggest appropriate categories for extracted line items using AI analysis

### FR4: Category Validation & Consolidation
- **FR4.1**: System shall present extracted items with AI-suggested categories in a validation interface
- **FR4.2**: Users shall be able to:
  - Review and modify suggested categories via dropdown selection
  - Mark items as "Ignore" to exclude from itemization
  - Add manual line items if missing from extraction
  - Validate that total matches original hotel bill amount
- **FR4.3**: System shall consolidate duplicate categories only after user validation/approval
- **FR4.4**: System shall calculate consolidated amounts for same-category items (e.g., multiple Hotel Tax entries)
- **FR4.5**: Consolidated itemization must equal the original hotel expense total amount

### FR5: Daily Rate Calculation
- **FR5.1**: System shall calculate daily rates for multi-day hotel stays
- **FR5.2**: For each category, system shall determine:
  - **Daily items**: Room rate, daily taxes, daily fees
  - **One-time items**: Resort fees, parking (if applicable), incidentals
- **FR5.3**: System shall calculate:
  - Daily amount per category
  - Number of days (quantity)
  - Total amount validation
- **FR5.4**: First expense entry date shall match the check-in date from the invoice

### FR6: Data Validation & Error Handling
- **FR6.1**: System shall validate that itemized amounts sum to the original expense total
- **FR6.2**: System shall flag discrepancies for user review
- **FR6.3**: System shall prevent submission if validation fails
- **FR6.4**: System shall handle missing or unclear invoice data gracefully

### FR7: MS Expense Integration & UI Population
- **FR7.1**: Hotel Itemizer shall integrate with existing expense import workflow
- **FR7.2**: System shall populate the MS Expense "Itemise expense" interface using Playwright automation
- **FR7.3**: For each consolidated category, system shall create entries with:
  - **Subcategory**: Selected from dropdown (Daily Room Rate, Hotel Tax, etc.)
  - **Start date**: Check-in date from invoice
  - **Daily rate**: Calculated amount per day for the category
  - **Quantity**: Number of days (calculated from check-in/check-out dates)
- **FR7.4**: System shall ensure total itemized amount equals original expense total (100.00 in example)
- **FR7.5**: System shall handle the "Total/Itemised/Remaining" validation in MS Expense interface
- **FR7.6**: System shall use existing browser automation patterns for consistent integration

## Technical Requirements

### TR1: Architecture & Integration
- **TR1.1**: Follow existing project patterns and conventions
- **TR1.2**: Use existing technology stack (Python, Quart, Playwright, Azure OpenAI)
- **TR1.3**: Maintain async/await architecture consistency
- **TR1.4**: Integrate with existing playwright_manager and expense_importer modules

### TR2: Data Models
- **TR2.1**: Define Pydantic models for:
  - Hotel invoice details
  - Itemized line items
  - Category mappings
  - Daily rate calculations
- **TR2.2**: Extend existing expense data structures as needed

### TR3: API & Routes
- **TR3.1**: Create new Quart routes under `/api/hotel/` prefix
- **TR3.2**: Maintain RESTful API conventions
- **TR3.3**: Follow existing error handling and response patterns

### TR4: User Interface
- **TR4.1**: Create responsive web interface components
- **TR4.2**: Follow existing UI patterns and styling
- **TR4.3**: Integrate with existing JavaScript frameworks and utilities
- **TR4.4**: Provide real-time validation and feedback

### TR5: Configuration & Environment
- **TR5.1**: Use existing configuration management (config.py)
- **TR5.2**: Support hotel categories configuration via environment or config file
- **TR5.3**: Maintain existing logging and debugging capabilities

## User Experience Requirements

### UX1: Workflow Integration
- **UX1.1**: Hotel itemization shall be accessible from the main expense processing interface
- **UX1.2**: Users shall be able to toggle between standard and hotel itemization modes
- **UX1.3**: Process shall provide clear step-by-step guidance

### UX2: Validation Interface
- **UX2.1**: Present extracted items in a clear, editable table format
- **UX2.2**: Highlight category conflicts and consolidation opportunities
- **UX2.3**: Provide drag-and-drop or intuitive interaction for category assignment
- **UX2.4**: Show real-time calculation updates as users make changes

### UX3: Error Handling & Feedback
- **UX3.1**: Provide clear error messages for validation failures
- **UX3.2**: Highlight problematic fields and suggest corrections
- **UX3.3**: Allow users to override validations with confirmation when necessary

## File Structure

```
hotel_itemizer/
├── __init__.py
├── REQUIREMENTS.md
├── hotel_extractor.py          # AI-powered hotel invoice extraction
├── hotel_categorizer.py        # Category management and mapping
├── daily_rate_calculator.py    # Daily rate calculation logic
├── hotel_validator.py          # Validation and consolidation logic
├── models.py                   # Pydantic models for hotel data
└── config.py                   # Hotel-specific configuration

front_end/routes/hotel/
├── __init__.py
├── hotel_routes.py             # Hotel-specific API routes

front_end/templates/hotel/
├── hotel_itemizer.html         # Main hotel itemization interface
├── category_validation.html    # Category validation modal/component
└── daily_rate_preview.html     # Daily rate calculation preview

front_end/static/css/hotel/
└── hotel-itemizer.css          # Hotel-specific styles

front_end/static/js/hotel/
├── hotel-itemizer.js           # Main hotel itemization logic
├── category-validator.js       # Category validation interface
└── daily-rate-calculator.js    # Daily rate calculation UI

tests/hotel/
├── test_hotel_extractor.py
├── test_hotel_categorizer.py
├── test_daily_rate_calculator.py
└── test_hotel_integration.py
```

## Success Criteria

### SC1: Functional Success
- [ ] Successfully processes hotel invoices with >90% accuracy in line item extraction
- [ ] Correctly categorizes common hotel charges with >85% accuracy
- [ ] Accurately calculates daily rates for multi-day stays
- [ ] Integrates seamlessly with existing expense workflow

### SC2: Technical Success
- [ ] Maintains existing system performance
- [ ] Follows established code quality standards
- [ ] Includes comprehensive test coverage (>80%)
- [ ] Passes all existing regression tests

### SC3: User Experience Success
- [ ] Users can complete hotel itemization in <5 minutes for typical invoices
- [ ] Interface is intuitive and requires minimal training
- [ ] Error messages are clear and actionable
- [ ] Process integrates smoothly with existing workflow

## Questions for Clarification

### High Priority Questions
1. **Hotel Categories**: Should we start with the categories listed above, or do you have a specific list?
2. **Daily vs. One-time Items**: How should we determine which items are daily vs. one-time charges?
3. **MS Expense Output**: Should each itemized category become a separate expense line in MS Expense?
4. **Invoice Date Handling**: What if check-in/check-out dates span different expense reporting periods?

### Medium Priority Questions
5. **Category Customization**: Should users be able to create custom categories?
6. **Multi-currency Support**: How should we handle foreign currency hotel bills?
7. **Corporate Discounts**: Should we handle corporate rate breakdowns differently?
8. **Chain-specific Logic**: Should we have special handling for major hotel chains?

### Low Priority Questions
9. **Audit Trail**: Should we maintain detailed logs of itemization decisions?
10. **Bulk Processing**: Should we support batch processing of multiple hotel invoices?
11. **Integration Testing**: Do you have access to sample hotel invoices for testing?
12. **Rollback Capability**: Should users be able to revert from itemized back to simple expense?

## Next Steps

1. **Requirements Review**: Review and refine these requirements based on your feedback
2. **Technical Design**: Create detailed technical specifications
3. **Implementation Plan**: Break down development into manageable phases
4. **Agent Development**: Use GitHub Copilot agent mode to implement the feature
5. **Testing & Integration**: Comprehensive testing and integration with existing system

---

*This requirements document will be updated as clarifications are provided and the feature evolves during development.*