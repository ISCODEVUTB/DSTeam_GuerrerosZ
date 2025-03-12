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

### 1. `Validable(ABC)` Class  

The `Validable` class is responsible for verifying whether the request parameters are correct. It utilizes the `typing` framework (List, Optional) and the `abc` module (ABC, abstractmethod), its method is:

- **`Validate(self) -> bool`**: This method returns `true` if the parameters fulfill the required conditions and `false` otherwise.  

### 2. `Person(ABC)` Class  

The `Person` class is responsible for initializing the common attributes of a person, such as ID, name, document type, phone, email, and address. It uses the `abc` module (ABC, abstractmethod), its method is: 

- **`get_information(self) -> str`**: This method returns the person's information as a formatted string.

### 3. `Operator(Person)` Class  

The `Operator` class represents an operator who has authentication credentials and inherits from the `Person` class.  

- **`__init__(self, user_token: str, password_token: str, client_id: int, name: str, document: str, phone: str, email: str, address: str, document_type: str) -> None`**:  
  Initializes the operator’s attributes, including authentication credentials (`user_token` and `password_token`), while inheriting personal details from the `Person` class.  


### 4. `Client(Person)` Class  

The `Client` class represents a client and inherits from the `Person` class and from `Validable`. It extends the base functionality by adding validation and retrieval of client-specific information.

- **`__init__(self, client_id: int, name: str, document: str, phone: str, email: str, address: str, document_type: str) -> None`**:  
  Initializes the client's attributes, calling the parent class constructor.

### 5. `PackageClassifier` Class  

The `PackageClassifier` class provides methods to classify packages based on weight and calculate their shipping costs, its methods are:

- **`classify(weight: float) -> Literal["basic", "standard", "oversized"]`**:  
  Determines the package category based on its weight:  
  - `"basic"`: Less than 1kg  
  - `"standard"`: Between 1kg and 5kg  
  - `"oversized"`: More than 5kg  

- **`calculate_cost(weight: float, package_type: str) -> float`**:  
  Computes the shipping cost using predefined base rates:  
  - `"basic"`: $5.00  
  - `"standard"`: $7.50 + additional weight-based cost  
  - `"oversized"`: $17.00 + additional weight-based cost  

### 6. `Package` Class  

The `Package` class represents a package with specific attributes such as dimensions, weight, type, approval status, and shipping cost. It integrates the `PackageClassifier` to determine the package category and cost, its methods are:

- **`__init__(self, package_id: int, dimensions: str, weight: float, observations: str) -> None`**:  
  Initializes a package, automatically classifies its type, and calculates the shipping cost. The package is not approved by default.  

- **`update_info(self, dimensions: str, weight: float, observations: str) -> None`**:  
  Updates the package's details (dimensions, weight, and observations) and recalculates its classification and shipping cost accordingly.  

- **`approve(self) -> None`**:  
  Marks the package as approved for shipment.

### 7. `Shipment` Class  

The `Shipment` class represents a shipment containing information about the sender, recipient, and associated packages, it inherits the methods of client and package its methods are:

- **`__init__(self, shipment_id: int, sender: Client, recipient: Client, packages: List[Package], observation: str) -> None`**:  
  Initializes a shipment, ensuring that all packages are approved before shipping. Also validates the recipient's address and calculates the total shipping cost. The shipment starts with an initial tracking status: `"Shipment created"`. 

- **`update_status(self, status: str) -> None`**:  
  Updates the shipment’s tracking with a new status.  

- **`update_tracking(self, status: str) -> None`**:  
  Adds a status update to the shipment’s tracking list.  

- **`track_shipment(self) -> List[str]`**:  
  Returns a list of all tracking status updates for the shipment.

### 8. `PaymentMethod(ABC)` Class  

The `PaymentMethod` class is an abstract base class that defines a structure for different payment methods. 

- **`process_payment(self, amount: float) -> str`**:  
  An abstract method that must be implemented by subclasses to process a payment of a given amount and return a confirmation message.  

### 9. `PayPalPayment(PaymentMethod)` Class  

The `PayPalPayment` class implements the `PaymentMethod` abstract class, providing functionality for processing payments via PayPal.  

- **`process_payment(self, amount: float) -> str`**:  
  Processes a payment of the specified amount and returns a confirmation message indicating that the payment was made using PayPal.  

### 10. `CashPayment(PaymentMethod)` Class  

The `CashPayment` class implements the `PaymentMethod` abstract class, allowing payments to be processed in cash at a branch location.  

- **`process_payment(self, amount: float) -> str`**:  
  Processes a payment of the specified amount and returns a confirmation message indicating that the payment was made in cash at a branch.  

### 11. `CardPayment(PaymentMethod)` Class  

The `CardPayment` class implements the `PaymentMethod` abstract class, enabling payments to be processed using a credit card.  

- **`process_payment(self, amount: float) -> str`**:  
  Processes a payment of the specified amount and returns a confirmation message indicating that the payment was made using a credit card.  

### 12. `Invoice` Class  

The `Invoice` class represents an invoice generated from one or more shipments, calculating the total cost and allowing payment processing.  

- **`generate_invoice(self) -> str`**:  
  Generates an invoice message indicating the invoice ID and the total amount to be paid.  

- **`process_payment(self, payment_method: PaymentMethod) -> str`**:  
  Processes the invoice payment using the specified payment method and returns a confirmation message.  

### 13. `ManagementSystem` Class  

The `ManagementSystem` class is responsible for managing clients, packages, shipments, and billing within the system. It provides methods for registering clients, handling packages, tracking shipments, and generating invoices.  

- **`register_client(self, client: Client) -> None`**: Adds a new client to the system.  

- **`add_package(self, package: Package) -> None`**: Approves and adds a package to the system.  

- **`update_package(self, package_id: int, dimensions: str, weight: float, observations: str) -> bool`**: Updates the information of an existing package if found. Returns `True` if the update is successful, otherwise `False`.  

- **`approve_package(self, package_id: int) -> bool`**: Approves a package by its ID. Returns `True` if successful, otherwise `False`.  

- **`create_shipment(self, shipment_id: int, sender: Client, recipient: Client, packages: List[int], observation: str) -> None`**: Creates a new shipment with the selected packages and adds it to the system. Each package requires approval before inclusion.  

- **`track_shipment(self, shipment_id: int) -> Optional[List[str]]`**: Retrieves the tracking details of a shipment by its ID. Returns a list of tracking updates if found, otherwise `None`.  

- **`generate_invoice(self, invoice_id: int, shipment_ids: List[int]) -> str`**: Generates an invoice for the specified shipments. Returns the invoice details if shipments are found, otherwise returns `"No shipments found to invoice"`.  

### 14. **`Terminal` Class**  

The `Terminal` class represents the main interface of the package management system.  
It allows operator authentication, client, package, and shipment management, as well as invoicing and payment processing.  

---

##### **Attributes**  

- **`__management_system: ManagementSystem`**  
  An instance of the management system that handles clients, packages, and shipments.  

- **`__operator_credentials_set: list[tuple[str, str]]`**  
  A set of credentials for registered operators in the system.  

---

#### **Methods**  

##### **Authentication**  

- **`show_main_message(self) -> None`**  
  Displays a welcome message on the terminal.  

- **`authenticate_credentials(self, user_token: str, password_token: str) -> bool`**  
  Verifies if the entered credentials correspond to a registered operator.  

---

##### **Client Management**  

- **`request_sender_info(self) -> Client`**  
  Requests and returns the sender's information.  

- **`request_recipient_info(self) -> Client`**  
  Requests and returns the recipient's information.  

- **`__request_client_info(self, type: str) -> Client`**  
  (Private) Requests the information of a client (sender or recipient) with data validation.  

---

##### **Package Management**  

- **`request_package_info(self, n: int, package_id: int) -> List[Package]`**  
  Requests the information of `n` packages and returns them as a list of `Package` objects.  

---

##### **Shipment Management**  

- **`create_shipment(self) -> str`**  
  Creates a new shipment with user-entered data and registers it in the system.  

---

##### **Invoicing and Payments**  

- **`create_invoice(self) -> None`**  
  Generates an invoice based on the shipments selected by the user and processes the payment.  

- **`select_payment_method(self) -> Optional[PaymentMethod]`**  
  Allows the user to choose a payment method and returns an instance of `PaymentMethod`.  

---

##### **Search and Filtering**  

- **`search_and_filter(self) -> None`**  
  Allows searching and filtering clients, shipments, or packages in the system.  

- **`search_client(self) -> None`**  
  Searches clients by name or document number.  

- **`search_shipment(self) -> None`**  
  Searches shipments by ID or tracking status.  

---

## Team
* Mario Alberto Julio Wilches.
* Andrés Felipe Rubiano Marrugo.
* Alejandro Pedro Steinman Cuesta.
* Amaury Enrique Bula Salas.
