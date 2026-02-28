-- Guided Exersize

-- 1 List the IDs and names of products that have been ordered. Each ID appears exactly once in the result. Sort the result by the product name in ascending order.
SELECT ProductID, ProductName FROM [Lab001].[Product]
WHERE ProductID IN (SELECT DISTINCT ProductID FROM [Lab001].[OrderLine])
ORDER BY ProductName ASC

-- 2 List the IDs of customers that have placed orders some time after Oct. 27, 2022.  Each ID appears exactly once in the result. Sort the result by the customer ID in descending order.
SELECT CustomerID FROM [Lab001].[OrderHeader]
WHERE OrderDate > '2022-10-27'
ORDER BY CustomerID DESC

-- 3 List all customers who are from Salt Lake City and whose first name starts with the letter ‘J’.
SELECT * FROM [Lab001].[Customer]
WHERE FirstName LIKE 'J%' AND City = 'Salt Lake City'

-- 4 List the product name, product price and product price after 10% discount.
SELECT ProductName, ProductPrice, ProductPrice * .9 ProductPrice10PercentOff
FROM [Lab001].[Product]

-- 5 List the number of products with a price higher than $200.
SELECT COUNT(*) from [Lab001].[Product]
WHERE ProductPrice > 200

-- 6 List name and price for all products that have been purchased in order 1001. Use IN to implement this query.
SELECT ProductName, ProductPrice FROM [Lab001].[Product]
WHERE ProductID IN (SELECT ProductID FROM [Lab001].[OrderLine]
WHERE OrderID = 1001) 

-- 7 Use an equijoin to implement the previous query.
SELECT ProductName, ProductPrice
FROM [Lab001].[OrderLine], [Lab001].[Product]
WHERE [Lab001].[OrderLine].ProductID = [Lab001].[Product].ProductID
AND OrderID = 1001

SELECT * FROM[Lab001].[OrderLine]
    JOIN [Lab001].[Product] ON [Lab001].[OrderLine].ProductID = [Lab001].[Product].ProductID
WHERE OrderID = 1001

-- 8 List the order id and the total quantity of items for each order. Sort the result by the total quantity descending.
SELECT OrderID, SUM(Quantity) TotalQuantityOrdered
FROM [Lab001].[OrderLine]
GROUP BY OrderID
;

-- 9 List the order id, date and total dollar amount for each order. Sort the result by the date ascending and then the total amount descending.
SELECT oh.OrderID, OrderDate, SUM(Quantity * ProductPrice) AS Total FROM [Lab001].[OrderHeader] oh
    JOIN [Lab001].[OrderLine] ol ON oh.OrderID = ol.OrderID
	JOIN [Lab001].[Product] p ON ol.ProductID = p.ProductID
GROUP BY oh.OrderID, OrderDate
HAVING SUM(Quantity * ProductPrice) > 1000
ORDER BY OrderDate ASC, SUM(Quantity * ProductPrice) DESC


-- Challenge Exercise – Part 1

-- 1 Select all rows from the customer table, but add a column called IsPlacedOrder where 1 indicates customers who have placed at least one order and 0 indicates customers who have not placed any orders.
SELECT CustomerID, FirstName, LastName, AddressLine1, City, RegionAbbr, PostalCode, 1 as IsPlacedOrder FROM [Lab001].[Customer]
where CustomerID in (select distinct CustomerID from Lab001.OrderHeader)
union all

SELECT CustomerID, FirstName, LastName, AddressLine1, City, RegionAbbr, PostalCode, 0 as IsPlacedOrder FROM [Lab001].[Customer]
where CustomerID not in (select distinct CustomerID from Lab001.OrderHeader)
;

-- 2 Remove customer Tom Borg from the database.
delete from [Lab001].[Customer] where FirstName = 'Tom' and LastName = 'Borg';

--3 Remove customer Carl Smith from the database using only three (3) separate delete statements none of which can include the cust_id for Carl Smith.
--3.1 - delete reference in OrderLine first
delete from [Lab001].[OrderLine]
where OrderID IN (select OrderID from [Lab001].[OrderHeader] oh 
	JOIN [Lab001].[Customer] cu ON oh.CustomerID = cu.CustomerID 
WHERE cu.FirstName = 'Carl' and cu.Lastname = 'Smith')
--3.2 - now we can delete the reference in OrderHeader
delete from [Lab001].[OrderHeader] 
where OrderID IN (select OrderID from [Lab001].[OrderHeader] oh 
	JOIN [Lab001].[Customer] cu ON oh.CustomerID = cu.CustomerID 
WHERE cu.FirstName = 'Carl' and cu.Lastname = 'Smith')
--3.3 - finally we are able to directly delete the record in the Customer table
delete from [Lab001].[Customer] where FirstName = 'Carl' and LastName = 'Smith'


-- Challenge Exercise – Part 2

-- 1 Delete the customer John Doe from the customer table, followed by his order_header records, followed by his order_line records.
-- look up the details of the foreign key constraints
select * from sys.tables st
JOIN sys.foreign_keys fk on st.[object_id] = fk.[parent_object_id];

-- drop the FK constraint on OrderHeader to Customer
alter table Lab001.OrderHeader drop constraint Order_FK;

-- drop the FK constratin on OrderLine to OrderHeader
alter table Lab001.OrderLine drop constraint OrderLine_FK1;

select OrderID from Lab001.OrderHeader where CustomerID = 1;
-- 1001
-- 1010

select * from Lab001.OrderLine where OrderID in (1001, 1010);

-- with the contraints dropped above, we can delete "top-down" from
-- Customer to OrderHeader to OrderLine
delete from Lab001.Customer where FirstName = 'John' and LastName = 'Doe';

delete from Lab001.OrderHeader where OrderID in (1001, 1010);

delete from Lab001.OrderLine where OrderID in (1001, 1010);


-- 2 Re-add any constraints that were dropped in order to meet the requirements for step 1.
-- add the FK constraint on OrderHeader to Customer
ALTER TABLE Lab001.OrderHeader
ADD CONSTRAINT Order_FK
FOREIGN KEY (CustomerID)
REFERENCES Lab001.Customer (CustomerID);
GO

ALTER TABLE Lab001.OrderLine
ADD CONSTRAINT OrderLine_FK1
FOREIGN KEY (OrderID)
REFERENCES Lab001.OrderHeader (OrderID);
GO