# System Design
## System units
To satisfy functional requirements, the system should have the following high level units:
- User Login
- Database Models
- Accounts Page
- Account Details Page
- Payment, Receivable, Debt, Collection modals
- Reminder

## General specifics
- System will be composed of two containers, one will carry the backend logic, and the other will carry the database.
- Above units will be defined in a django framework application to ensure fast development of the project.
- System architecture will follow the Django framework's MVC Pattern
- Deployment specifics will be determined during deployment

## Unit Design
### User Login
- This unit will handle access to the application
- Unit will handle user login data 