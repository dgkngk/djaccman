# System Design
## System units
To satisfy functional requirements, the system should have the following high level units:
- User Login
- Database Models
- Accounts Page
- Account Details Page
- Create account modal
- PRDC (Payment, Receivable, Debt, Collection) modal
- Reminder TBD

## General specifics
- System will be composed of two containers, one will carry the backend logic, and the other will carry the database.
- Above units will be defined in a django framework application to ensure fast development of the project.
- System architecture will follow the Django framework's MVC Pattern
- Deployment specifics will be determined during deployment

## Unit Design
### User Login
- This unit will handle access to the application
- Unit will handle user login data 

## Database Models
### Model Specifics
- User:
    - Std Django User
- Account:
  - Id int
  - Name text
  - Category enum
  - LastTransaction date
  - Balance int
  - IsActive bool
- Transaction:
  - Id int
  - account_id
  - Date date
  - Type enum
  - Description text
  - Amount int
  - AccountAfter int

### Relationships
- account 1 - m transaction

### Enums
- Account.Category:
  - TBD
- Transaction.Type:
  - TBD

## Accounts Page
- This page will be contained in the home.html template
- Datatable containing accounts in the database
- Datatable accounts will contain account details link
- Will be contained in home view

## Account Details Page
- This page will be contained in the details.html template
- Datatable containing accounts in the database
- Will be contained in details view
