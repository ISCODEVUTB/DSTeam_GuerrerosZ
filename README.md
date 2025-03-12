# Package management system (DSTeam_guerrerosZ)

## Description 

The **Package management system (DSTeam_guerrerosZ)** development is a Python-based package management system designed to comprehensively handle shipments at local, national, and international levels, offering scalable solutions. Built on Object-Oriented Programming, it provides key functionalities such as package management (insertion, classification, deletion, and updating), shipment management (tracking and traceability), and user management (authentication, billing, and payment processing).

## Project Status
The project is currently complete, featuring a functional Docker setup and utilizing SonarQube for code coverage and quality analysis.

## Installation  

The **Package Management System (DSTeam_guerrerosZ)** requires Python 3.10 or later. 

### **Implementation**
   
For the proper implementation of this development, you need to install the required dependencies listed in the requirements.txt file by running the following command:
    
    ```
    pip install -r requirements.tx
    ```
    
    This archive has to have the following libraries: 
    
    ```
    alembic==1.5.5                # Database migrations for SQLAlchemy  
    aniso8601==9.0.0              # Date and time parsing  
    click==7.1.2                  # Command-line interface creation  
    Flask==1.1.2                  # Web framework for building applications  
    flask-marshmallow==0.14.0     # Flask integration for Marshmallow (object serialization/deserialization)  
    Flask-Migrate==2.7.0          # Handling database migrations with Alembic  
    Flask-RESTful==0.3.8          # Extension for building REST APIs in Flask  
    Flask-SQLAlchemy==2.4.4       # SQLAlchemy integration for Flask  
    itsdangerous==1.1.0           # Provides cryptographic signing for secure data handling  
    Jinja2==2.11.3                # Templating engine for Flask  
    Mako==1.1.4                   # Alternative templating engine  
    MarkupSafe==1.1.1             # Provides string escaping for security  
    marshmallow==3.10.0           # Data validation and serialization/deserialization  
    marshmallow-sqlalchemy==0.24.2 # SQLAlchemy integration for Marshmallow  
    python-dateutil==2.8.1        # Extends datetime functionalities  
    python-editor==1.0.4          # Simple editor integration for Python  
    pytz==2021.1                  # Time zone handling  
    six==1.15.0                   # Compatibility between Python 2 and 3  
    SQLAlchemy==1.3.23            # Object-relational mapper (ORM) for databases  
    Werkzeug==1.0.1               # WSGI utility library for Flask  
    ```

### **Docker**

The development environment is configured through our `Dockerfile`, designed for use on Linux enviroment. It defines dependencies, configurations, and setup commands, ensuring a consistent and reproducible deployment. 

## 
