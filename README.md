# Cobex

Cobex is a Digitized Cooperative Society Management System that aims to streamline and automate cooperative society activities. It provides a digital platform for managing members, tracking savings, loans, and transactions, and generating reports, while ensuring secure access and ease of use for cooperatives.

## Features

- [x] Member Management: Add, edit, and view members of the cooperative society. Track each member's savings, loan status, and account history.

- [x] Savings Management: Easily record member savings, track cumulative contributions, and view historical data.

- [x] Loan Management: Manage loan applications, approvals, disbursements, and repayments. Track outstanding loans and calculate interest automatically.

- [x] Transaction History: Keep a detailed record of all financial transactions, including deposits, withdrawals, and loan payments.

- [x] Reports: Generate reports on savings, loans, and overall financial health of the cooperative society.

- [x] Access Control: Different user roles with customizable access levels (e.g., Admin, Manager, Member).

- [x] Dashboard: An interactive dashboard that provides a high-level overview of key metrics like total savings, outstanding loans, and active members.

## Getting Started

Follow these instructions to get a copy of Cobex up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.10 or higher
- Flask
- PostgreSQL database
- Node.js (for React frontend)
- React.js (Frontend framework)

### Installation

Backend (Flask API)

#### Clone the Repository

```bash Copy code
git clone https://github.com/yourusername/cobex.git
```

```bash Copy code
cd cobex
```

#### Create a Virtual Environment

##### For Linux

```bash Copy code
python3 -m venv venv
source venv/bin/activate
```

##### For Linux (alternative)

```bash Copy code
virtualenv venv
source venv/bin/activate
```

##### For Windows

```bash Copy code
python3 -m venv venv
source venv/scripts/activate
```

##### For Windows (alternative)

```bash Copy code
virtualenv venv
source venv/scripts/activate
```

#### Install Dependencies

```bash Copy code
pip install -r requirements.txt
```

#### Configure Environment Variables

Create a .env file in the root directory with the following environment variables:

```bash Copy code
DATABASE_URL=postgresql://username:password@localhost/cobexdb
SECRET_KEY=your_secret_key
```

#### Initialize the Database

```bash Copy code
flask db upgrade
```

#### Run the Application

##### For linux
```bash Copy code
set flask_app=src/server.py
set flask_debug=true
python src/server.py
```

##### For windows
```bash Copy code
export flask_app=src/server.py
export flask_debug=true
python src/server.py
```

The API will be available at http://127.0.0.1:5000/.

### Frontend (React)

Navigate to the Frontend Directory

```bash Copy code
cd client
```

Install Dependencies

```bash Copy code
npm i
```
#### Configure Environment Variables

Create a .env file in the frontend directory:

```arduino Copy code
REACT_APP_API_URL=http://127.0.0.1:5000
````

#### Run the Frontend

```bash Copy code
npm run dev
```

The frontend will be available at http://localhost:3000/.

## Usage

- **Login**: Use the provided credentials to log in as an Admin, Manager, or Member. Different roles will have different access rights to the system.

- **Dashboard**: The dashboard provides a summary of key statistics such as total savings, loans, and member activities.

- **Manage Members**: Admins and Managers can add new members, edit existing ones, or view their savings and loan details.

- **Savings**: Record member savings and track the total contributions. Generate savings reports for any given period.

- **Loans**: Submit loan applications, process loan approvals, and disburse funds. Monitor repayment progress and issue loan statements.

- **Reports**: Generate detailed financial reports, savings logs, loan summaries, and transaction histories. Filter data based on date ranges or members.

## API Documentation

Cobex also provides a REST API for easy integration with other systems or applications.

#### Example Endpoints

- Login: POST /api/auth/login
- Get All Members: GET /api/members
- Add Member: POST /api/members
- Update Member: PUT /api/members/{id}
- Get All Loans: GET /api/loans
- Create Loan: POST /api/loans
- Record Savings: POST /api/savings

## Technologies Used

### Backend

- Flask: Python web framework for handling API and business logic
- SQLAlchemy: ORM for database management
- Alembic: Database migrations
- PostgreSQL: Relational database for storing data

### Frontend

- React.js: JavaScript library for building user interfaces
- Axios: HTTP client for API requests
- React Router: Navigation between different views
- Flowbite: React UI components for rapid development
- Tailwind CSS
- React Query

## License

This project is licensed under the MIT License - see the LICENSE file for details.
