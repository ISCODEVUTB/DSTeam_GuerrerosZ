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
For executing the application we will use:

    ```
    python app.py
    ```
    
### **Docker**

The development environment is configured through our `Dockerfile`, designed for use on Linux enviroment. It defines dependencies, configurations, and setup commands, ensuring a consistent and reproducible deployment. 

## Classes descriptions and funtions

## **1. Base and Validation Classes**  
These classes provide core functionalities such as validation and structure for other classes.  

### **`Validable(ABC)`** class
The `Validable` class is responsible for verifying whether request parameters are correct.  

- **`Validate(self) -> bool`**  
  Returns `true` if the parameters meet the required conditions, otherwise `false`.  

### **`Person(ABC)`**  class
The `Person` class initializes common attributes for a person, such as ID, name, document type, phone, email, and address.  

- **`get_information(self) -> str`**  
  Returns the person's information as a formatted string.  

---

## **2. User and Authentication Classes**  
These classes represent individuals interacting with the system.  

### **`Operator(Person)`** class  
The `Operator` class represents an operator with authentication credentials.  

- **`__init__(self, user_token: str, password_token: str, client_id: int, name: str, document: str, phone: str, email: str, address: str, document_type: str) -> None`**  
  Initializes an operator’s attributes, including authentication credentials (`user_token`, `password_token`), while inheriting personal details from `Person`.  

### **`Client(Person, Validable)`** class
The `Client` class represents a client, inheriting from `Person` and `Validable`.  

- **`__init__(self, client_id: int, name: str, document: str, phone: str, email: str, address: str, document_type: str) -> None`**  
  Initializes a client’s attributes and calls the parent class constructor.  

---

## **3. Package Management Classes**  
These classes handle package classification, validation, and storage.  

### **`PackageClassifier`**  class
Provides methods for package classification and cost calculation.  

- **`classify(weight: float) -> Literal["basic", "standard", "oversized"]`**  
  Determines the package category based on weight:  
  - `"basic"`: Less than 1kg  
  - `"standard"`: Between 1kg and 5kg  
  - `"oversized"`: More than 5kg  

- **`calculate_cost(weight: float, package_type: str) -> float`**  
  Computes shipping cost using predefined base rates:  
  - `"basic"`: $5.00  
  - `"standard"`: $7.50 + additional weight-based cost  
  - `"oversized"`: $17.00 + additional weight-based cost  

### **`Package`** class  
Represents a package with attributes like dimensions, weight, type, approval status, and cost.  

- **`__init__(self, package_id: int, dimensions: str, weight: float, observations: str) -> None`**  
  Initializes a package, classifies it, and calculates its shipping cost.  

- **`update_info(self, dimensions: str, weight: float, observations: str) -> None`**  
  Updates package details and recalculates classification and cost.  

- **`approve(self) -> None`**  
  Marks the package as approved for shipment.  

---

## **4. Shipment Management Classes**  
These classes handle shipment tracking, updates, and management.  

### **`Shipment`** class 
Represents a shipment containing sender, recipient, and package information.  

- **`__init__(self, shipment_id: int, sender: Client, recipient: Client, packages: List[Package], observation: str) -> None`**  
  Initializes a shipment, ensuring all packages are approved before shipping.  

- **`update_status(self, status: str) -> None`**  
  Updates the shipment’s tracking status.  

- **`update_tracking(self, status: str) -> None`**  
  Adds a status update to the shipment’s tracking list.  

- **`track_shipment(self) -> List[str]`**  
  Returns a list of all tracking status updates.  

---

## **5. Payment and Invoice Management Classes**  
These classes handle different payment methods and invoice generation.  

### **`PaymentMethod(ABC)`** class  
Abstract class defining the structure for payment methods.  

- **`process_payment(self, amount: float) -> str`**  
  Must be implemented by subclasses to process a payment and return a confirmation message.  

### **`PayPalPayment(PaymentMethod)`** class 
Implements the `PaymentMethod` abstract class for PayPal payments.  

- **`process_payment(self, amount: float) -> str`**  
  Processes a PayPal payment and returns a confirmation message.  

### **`CashPayment(PaymentMethod)`** class 
Implements `PaymentMethod` for cash payments at a branch.  

- **`process_payment(self, amount: float) -> str`**  
  Processes a cash payment and returns a confirmation message.  

### **`CardPayment(PaymentMethod)`**  class
Implements `PaymentMethod` for credit card payments.  

- **`process_payment(self, amount: float) -> str`**  
  Processes a credit card payment and returns a confirmation message.  

### **`Invoice`** class  
Represents an invoice generated from one or more shipments.  

- **`generate_invoice(self) -> str`**  
  Generates an invoice message with the invoice ID and total amount.  

- **`process_payment(self, payment_method: PaymentMethod) -> str`**  
  Processes the invoice payment and returns a confirmation message.  

---

## **6. System Management Classes**  
These classes manage clients, shipments, packages, invoices, and general system operations.  

### **`ManagementSystem`** class 
Handles clients, packages, shipments, and billing.  

- **`register_client(self, client: Client) -> None`**  
  Adds a new client to the system.  

- **`add_package(self, package: Package) -> None`**  
  Approves and adds a package to the system.  

- **`update_package(self, package_id: int, dimensions: str, weight: float, observations: str) -> bool`**  
  Updates package details and returns `True` if successful, otherwise `False`.  

- **`approve_package(self, package_id: int) -> bool`**  
  Approves a package by ID.  

- **`create_shipment(self, shipment_id: int, sender: Client, recipient: Client, packages: List[int], observation: str) -> None`**  
  Creates a shipment with the selected packages.  

- **`track_shipment(self, shipment_id: int) -> Optional[List[str]]`**  
  Retrieves tracking details of a shipment.  

- **`generate_invoice(self, invoice_id: int, shipment_ids: List[int]) -> str`**  
  Generates an invoice for specified shipments.  

---

## **7. Terminal and User Interface Classes**  
These classes handle interaction between users and the system.  

### **`Terminal`** class
Represents the main interface of the package management system.  

#### **Authentication**  
- **`show_main_message(self) -> None`**  
  Displays a welcome message.  

- **`authenticate_credentials(self, user_token: str, password_token: str) -> bool`**  
  Verifies operator credentials.  

#### **Client Management**  
- **`request_sender_info(self) -> Client`**  
  Requests sender's information.  

- **`request_recipient_info(self) -> Client`**  
  Requests recipient's information.  

- **`__request_client_info(self, type: str) -> Client`**  
  Private method to request client information.  

#### **Package Management**  
- **`request_package_info(self, n: int, package_id: int) -> List[Package]`**  
  Requests package details and returns a list of packages.  

#### **Shipment Management**  
- **`create_shipment(self) -> str`**  
  Creates a shipment and registers it in the system.  

#### **Invoicing and Payments**  
- **`create_invoice(self) -> None`**  
  Generates an invoice and processes payment.  

- **`select_payment_method(self) -> Optional[PaymentMethod]`**  
  Allows the user to choose a payment method.  

#### **Search and Filtering**  
- **`search_client(self) -> None`**  
  Searches clients by name or document number.  

- **`search_shipment(self) -> None`**  
  Searches shipments by ID or tracking status.  

---

## Team
* Mario Alberto Julio Wilches- _Code quality_
* Andrés Felipe Rubiano Marrugo-_CL/CD_
* Alejandro Pedro Steinman Cuesta-_Developer_
* Amaury Enrique Bula Salas- _CI/CD_
