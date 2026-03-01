-- Jamison Orton
-- March 1, 2026
-- U080977
-- IS-6420
-- Assignment 3 - SQL 


-- SUBQUERIES VS MULTIPLE QUERIES + HARD-CODED VALUES

-- 1 List the average price for all products available to sell.
SELECT AVG(ProductPrice) AS AveragePrice FROM [Lab001].[Product]

-- 2 In a single query result, with no duplicates, ordered by the price in ascending order, 
-- list the product id, name, and price for all products with a price greater than the average price for all products available to sell.  
-- IMPORTANT: the average price should be calculated as part of a subquery (i.e., don’t just hard-code the final number from the previous question)
SELECT DISTINCT p.ProductID, p.ProductName, p.ProductPrice
FROM Lab001.Product AS p
WHERE p.ProductPrice >
(
    SELECT AVG(p2.ProductPrice)
    FROM Lab001.Product AS p2
)
ORDER BY p.ProductPrice ASC;


-- SORTING WITH SIMPLE COLUMNS, JOINS, AND AGGREGATE COLUMNS

-- 3 In a single query result, with no duplicates, ordered by the product id in ascending order, 
-- list the product id and total quantity ordered (by all customers). 
SELECT
    ol.ProductID,
    SUM(ol.Quantity) AS TotalQuantityOrdered
FROM Lab001.OrderLine AS ol
GROUP BY ol.ProductID
ORDER BY ol.ProductID ASC;

-- 4 In a single query result, with no duplicates, ordered by the product name in ascending order,
-- list the product id, product name and total quantity ordered (by all customers).
SELECT
    p.ProductID,
    p.ProductName,
    SUM(ol.Quantity) AS TotalQuantityOrdered
FROM Lab001.OrderLine AS ol
JOIN Lab001.Product AS p
    ON p.ProductID = ol.ProductID
GROUP BY
    p.ProductID,
    p.ProductName
ORDER BY
    p.ProductName ASC;

-- 5 In a single query result, with no duplicates, ordered by the total quantity ordered (by all customers) in descending order, 
-- list the product id, product name and total quantity ordered (by all customers).
SELECT
    p.ProductID,
    p.ProductName,
    SUM(ol.Quantity) AS TotalQuantityOrdered
FROM Lab001.OrderLine AS ol
JOIN Lab001.Product AS p
    ON p.ProductID = ol.ProductID
GROUP BY
    p.ProductID,
    p.ProductName
ORDER BY
    TotalQuantityOrdered DESC;

-- 6 In a single query result, with no duplicates, ordered by the total quantity ordered (by all customers) in descending order, 
-- list the product id, product name and total quantity ordered (by all customers) considering only orders after (i.e., not including) Oct. 23, 2022.
SELECT
    p.ProductID,
    p.ProductName,
    SUM(ol.Quantity) AS TotalQuantityOrdered
FROM Lab001.OrderLine AS ol
JOIN Lab001.Product AS p
    ON p.ProductID = ol.ProductID
JOIN Lab001.OrderHeader AS oh
    ON oh.OrderID = ol.OrderID
WHERE oh.OrderDate > '2022-10-23'
GROUP BY
    p.ProductID,
    p.ProductName
ORDER BY
    TotalQuantityOrdered DESC;


-- SUBQUERIES VS JOINS

-- 7 In a single query result, with no duplicates, ordered by customer id in ascending order, 
-- list the customer id for all customers who have placed at least one order on or after Oct. 22, 2022.
SELECT oh.CustomerID
FROM Lab001.OrderHeader AS oh
WHERE oh.OrderDate >= '2022-10-22'
GROUP BY oh.CustomerID
ORDER BY oh.CustomerID ASC;

-- 8 In a single query result, with no duplicates, ordered by the last name in descending order, 
-- then the first name in descending order, list the customer id, customer first and last names 
-- for all customers who have placed at least one order on or after Oct. 22, 2022.
-- IMPORTANT: You must use “in” along with a subquery (i.e. you are not allowed to use a join for this query).
SELECT DISTINCT
    c.CustomerID,
    c.FirstName,
    c.LastName
FROM Lab001.Customer AS c
WHERE c.CustomerID IN (
    SELECT oh.CustomerID
    FROM Lab001.OrderHeader AS oh
    WHERE oh.OrderDate >= '2022-10-22'
)
ORDER BY
    c.LastName DESC,
    c.FirstName DESC;

-- 9 In a single query result, with no duplicates, ordered by the last name in descending order, 
-- then first name in descending order, list the customer id, customer first and last names for all customers 
-- who have placed at least one order on or after Oct. 22, 2022.  
-- IMPORTANT: You must use a “equijoin” for this query (i.e. you are not allowed to use a subquery for this query).
SELECT DISTINCT
    c.CustomerID,
    c.FirstName,
    c.LastName
FROM Lab001.Customer AS c
JOIN Lab001.OrderHeader as oh
    ON oh.CustomerID = c.CustomerID
WHERE oh.OrderDate >= '2022-10-22'
ORDER BY
    c.LastName DESC,
    c.FirstName DESC;


-- SET OPERATIONS

-- 10 In a single query result, with no duplicates, ordered by the product id in ascending order,
-- list the product ids that have NOT been ordered after Oct. 27, 2022.
-- IMPORTANT: You must use the “except” operator for this query.
SELECT p.ProductID
FROM Lab001.Product AS p

EXCEPT

SELECT ol.ProductID
FROM Lab001.OrderLine AS ol
JOIN Lab001.OrderHeader AS oh
    ON oh.OrderID = ol.OrderID
WHERE oh.OrderDate > '2022-10-27'

ORDER BY ProductID ASC;

-- 11 In a single query result, with no duplicates, ordered by the customer id in descending order,
-- list the customer id for all customers from Arizona who have placed order(s) on or after Oct. 27, 2022.
-- IMPORTANT: You must use the “intersect” operator for this query.
SELECT c.CustomerID
FROM Lab001.Customer AS c
WHERE c.RegionAbbr = 'AZ'

INTERSECT

SELECT oh.CustomerID
FROM Lab001.OrderHeader AS oh
WHERE oh.OrderDate >= '2022-10-27'

ORDER BY CustomerID DESC;

-- 12 In a single query result, with no duplicates, ordered by the customer id in ascending order,
-- list the customer id and customer first and last names for all customers from California along with
-- all customers who have placed order(s) on or after Oct. 23, 2022.
-- IMPORTANT: You must use the “union” operator for this query.
SELECT
    c.CustomerID,
    c.FirstName,
    c.LastName
FROM Lab001.Customer AS c
WHERE c.RegionAbbr = 'CA'

UNION

SELECT
    c.CustomerID,
    c.FirstName,
    c.LastName
FROM Lab001.Customer AS c
JOIN Lab001.OrderHeader AS oh
    ON oh.CustomerID = c.CustomerID
WHERE oh.OrderDate >= '2022-10-23'

ORDER BY CustomerID ASC;


-- WILDCARDS

-- 13 In a single query result, with no duplicates, ordered by the last name in descending order,
-- then the first name in descending order, list the customer id, first name, last name and city for
-- all customers whose first name starts with a “B”.
SELECT 
    c.CustomerID,
    c.FirstName,
    c.LastName,
    c.City
FROM Lab001.Customer AS c
WHERE c.FirstName LIKE 'B%'

ORDER BY
    c.LastName DESC,
    c.FirstName DESC;

-- 14 In a single query result, with no duplicates, ordered by the last name in descending order,
-- then the first name in ascending order, list the customer id, first name, last name and city for
-- all customers whose first name contains a “t” and whose last name contains an “o”.
SELECT DISTINCT
    c.CustomerID,
    c.FirstName,
    c.LastName,
    c.City
FROM Lab001.Customer AS c
WHERE c.FirstName LIKE '%t%' AND c.LastName LIKE '%o%'
ORDER BY
    c.LastName DESC,
    c.FirstName ASC;

-- FILTERING WITH WHERE (BEFORE AGGREGATION) VS HAVING (AFTER AGGREGATION)

-- 15 In a single query result, with no duplicates, ordered by the product name in ascending order,
-- list the product id, product name, and total quantity ordered (by all customers) for products
-- with a total quantity ordered (by all customers)  greater than 5.
SELECT
    p.ProductID,
    p.ProductName,
    SUM(ol.Quantity) AS TotalQuantityOrdered
FROM Lab001.Product AS p
JOIN Lab001.OrderLine AS ol
    ON ol.ProductID = p.ProductID
GROUP BY
    p.ProductID,
    p.ProductName
HAVING
    SUM(ol.Quantity) > 5
ORDER BY
    p.ProductName ASC;

-- 16 In a single query result, with no duplicates, ordered by the product name in ascending order,
-- list the product id, product name, and total quantity ordered (by all Utah customers) for products
-- with a total quantity ordered (by all Utah customers) greater than 2.
SELECT
    p.ProductID,
    p.ProductName,
    SUM(ol.Quantity) AS TotalQuantityOrdered
FROM Lab001.Product AS p
JOIN Lab001.OrderLine AS ol
    ON ol.ProductID = p.ProductID
JOIN Lab001.OrderHeader AS oh
    ON oh.OrderID = ol.OrderID
JOIN Lab001.Customer AS c
    ON c.CustomerID = oh.CustomerID
WHERE c.RegionAbbr = 'UT'
GROUP BY
    p.ProductID,
    p.ProductName
HAVING
    SUM(ol.Quantity) > 2
ORDER BY
    p.ProductName ASC;
