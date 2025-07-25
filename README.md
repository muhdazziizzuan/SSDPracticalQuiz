# Flask Web Application with CI/CD Pipeline

This is a secure Flask web application with comprehensive CI/CD pipeline using GitHub Actions.

## Features

- **Security**: XSS and SQL injection protection
- **Input Validation**: Sanitized user inputs
- **Session Management**: Secure session handling
- **Docker Support**: Multi-container setup with Nginx, Git server, and Flask

## CI/CD Pipeline

The project includes two GitHub Actions workflows:

### 1. CI/CD Pipeline (`ci-cd.yml`)

Runs on every push and pull request:

- **Dependency Check**: Security vulnerability scanning with Safety and Bandit
- **Integration Tests**: Comprehensive Flask application testing
- **UI Testing**: Selenium-based browser testing over HTTP
- **ESLint Security Scan**: JavaScript security analysis with ESLint security plugin
- **Docker Build Test**: Validates Docker Compose setup
- **Security Scan**: Trivy vulnerability scanner

### 2. Security Monitoring (`security-monitoring.yml`)

Runs daily for continuous monitoring:

- **Dependency Updates**: Checks for outdated packages
- **Vulnerability Scanning**: Regular security assessments
- **Code Quality**: Linting and formatting checks

## Local Development

### Prerequisites

- Python 3.11+
- Docker and Docker Compose
- Git

### Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Or use Docker Compose:
   ```bash
   docker-compose up
   ```

### Testing

Run tests locally:

```bash
# Install test dependencies
pip install -r requirements-test.txt

# Run integration tests
pytest test_app.py -v

# Run UI tests (requires Chrome/ChromeDriver)
pytest test_ui.py -v

# Security checks
safety check
bandit -r .
```

### JavaScript Development

For frontend JavaScript development:

```bash
# Install Node.js dependencies
npm install

# Run ESLint security scan
npm run lint:security

# Run standard ESLint
npm run lint
```

## Services

- **Flask App**: http://localhost:5000
- **Nginx**: http://localhost:80
- **Git Server**: http://localhost:3000

## Security Features

- Input validation against XSS attacks
- SQL injection pattern detection
- Secure session management
- Regular dependency vulnerability scanning
- Code security analysis with Bandit
- JavaScript security scanning with ESLint security plugin
- Client-side input validation and sanitization

## Git Configuration

- Username: Muhammad Azzi Izzuan Bin Azahar
- Email: 2301955@sit.singaporetech.edu.sg