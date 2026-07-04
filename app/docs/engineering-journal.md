# Engineering Journal

## Session 2 - Layered Architecture

### Problem

Business logic placed directly inside API endpoints becomes difficult to maintain.

### Decision

Introduce a Service Layer and Repository Layer.

### Reason

- Separation of concerns
- Better testing
- Easier maintenance
- Reusable business logic

### Relation to Frappe

In Frappe, business logic is often mixed inside @frappe.whitelist() methods.
This project separates HTTP handling, business rules, and persistence.

### Interview Note

Explain that the Service Layer encapsulates business logic while repositories handle persistence.