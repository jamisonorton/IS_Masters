CREATE SCHEMA Lab001;
GO

DROP TABLE IF EXISTS Lab001.OrderLine;
DROP TABLE IF EXISTS Lab001.Product;
DROP TABLE IF EXISTS Lab001.OrderHeader;
DROP TABLE IF EXISTS Lab001.Customer;

CREATE TABLE Lab001.Customer (
  CustomerID INT NOT NULL,
  FirstName VARCHAR(210) NOT NULL,
  LastName VARCHAR(210) NOT NULL,
  AddressLine1 VARCHAR(100),
  City VARCHAR(20),
  RegionAbbr CHAR(2),
  PostalCode VARCHAR(10),
  CONSTRAINT Customer_PK PRIMARY KEY (CustomerID)
);

CREATE TABLE Lab001.OrderHeader (
  OrderID INT NOT NULL,
  OrderDate DATE,
  CustomerID INT,
  CONSTRAINT Order_PK PRIMARY KEY (OrderID),
  CONSTRAINT Order_FK FOREIGN KEY (CustomerID) REFERENCES Lab001.Customer(CustomerID)
);

CREATE TABLE Lab001.Product (
  ProductID INT NOT NULL,
  ProductName VARCHAR(100),
  ProductPrice MONEY,
  CONSTRAINT Product_PK PRIMARY KEY (ProductID)
);

CREATE TABLE Lab001.OrderLine (
  OrderID INT NOT NULL,
  ProductID INT NOT NULL,
  Quantity INT,
  CONSTRAINT OrderLine_PK PRIMARY KEY (OrderID, ProductID),
  CONSTRAINT OrderLine_FK1 FOREIGN KEY (OrderID) REFERENCES Lab001.OrderHeader(OrderID),
  CONSTRAINT OrderLine_FK2 FOREIGN KEY (ProductID) REFERENCES Lab001.Product(ProductID)
);
