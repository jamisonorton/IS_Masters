-- For a sample submission see this document: https://docs.google.com/document/d/e/2PACX-1vSkHhLLzj2Ldwk_AQairwCaZ-jk6S2ARGvP3YjfNNRz7VcdQFIcFLCODyYSJWCf4A/pub

-- 1. Views

-- a. Review this example view
CREATE OR ALTER VIEW Lab001.OrderSummary AS
SELECT OrderID
, SUM(ol.Quantity * p.ProductPrice) TotalAmount
FROM Lab001.OrderLine ol 
    JOIN Lab001.product p on ol.ProductID = p.ProductID
GROUP BY OrderID
GO

-- b. Create a view, "Lab001.OrderDetail" based on the user-friendly 
-- order details query below
CREATE OR ALTER VIEW Lab001.OrderDetail AS
SELECT oh.OrderDate,
oh.OrderID,
cu.FirstName,
cu.LastName,
cu.AddressLine1,
cu.City,
cu.RegionAbbr,
cu.PostalCode,
p.ProductName,
ol.Quantity,
p.ProductPrice
FROM Lab001.customer cu, Lab001.OrderHeader oh, Lab001.OrderLine ol, Lab001.product p
WHERE cu.CustomerID=oh.CustomerID AND
oh.OrderID=ol.OrderID AND
ol.ProductID=p.ProductID
GO

-- c. Select all rows and columns from Lab001.OrderDetail and take a screenshot

SELECT * FROM Lab001.OrderDetail;

-- 2. Triggers

-- a. Review the table below
DROP TABLE IF EXISTS Lab001.ProductPriceAudit
GO
CREATE TABLE Lab001.ProductPriceAudit
(
    UpdateDate date,
    OldValue money,
    NewValue money
)
GO

-- b. Review the trigger below
CREATE OR ALTER TRIGGER Lab001.AuditPriceChangeTrigger 
    ON [Lab001].[product]
    FOR UPDATE
AS
BEGIN
SET NOCOUNT ON;
    DECLARE @oldValue AS MONEY;
    DECLARE @newValue AS MONEY;
    SELECT @oldValue = ProductPrice from deleted;
    SELECT @newValue = ProductPrice from inserted;
    INSERT INTO Lab001.ProductPriceAudit VALUES (GETDATE(), @oldValue, @newValue);
END
GO

-- c. Increase price for product by $10
UPDATE Lab001.product 
SET ProductPrice = ProductPrice + 10.00 
WHERE ProductID = 101
GO

-- d. Verify trigger has worked
SELECT * 
FROM Lab001.ProductPriceAudit
GO

-- e. Update the Lab001.ProductPriceAudit adding price_change_percentage column
ALTER TABLE Lab001.ProductPriceAudit
ADD price_change_percentage NUMERIC(10,3);
GO

-- f. Update the Lab001.AuditPriceChangeTrigger trigger to add the price percentage change
CREATE OR ALTER TRIGGER Lab001.AuditPriceChangeTrigger 
ON [Lab001].[product]
FOR UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @oldValue MONEY;
    DECLARE @newValue MONEY;
    DECLARE @percentageChange NUMERIC(10,3);

    SELECT @oldValue = ProductPrice FROM deleted;
    SELECT @newValue = ProductPrice FROM inserted;

    SET @percentageChange = 
        CASE 
            WHEN @oldValue = 0 THEN NULL
            ELSE ((@newValue - @oldValue) * 100) / @oldValue
        END;

    INSERT INTO Lab001.ProductPriceAudit
    (
        UpdateDate,
        OldValue,
        NewValue,
        price_change_percentage
    )
    VALUES
    (
        GETDATE(),
        @oldValue,
        @newValue,
        @percentageChange
    );
END
GO

-- g. Increase price for product by 10%
UPDATE Lab001.product 
SET ProductPrice = ProductPrice * 1.1 -- 10% price incrase
WHERE ProductID = 101
GO


-- h. Verify the trigger has worked by selecting all rows and 
-- columns from Lab001.ProductPriceAudit and take a screenshot
SELECT * 
FROM Lab001.ProductPriceAudit
GO


-- 3. Functions

-- a. Review the function below
CREATE OR ALTER FUNCTION Lab001.CalculateDiscountedPrice(
@productID INT,
@percentDiscount NUMERIC(10,3))
RETURNS MONEY
AS
BEGIN
DECLARE @returnValue AS MONEY;
SELECT @returnValue = ProductPrice * @percentDiscount
FROM [Lab001].[product]
WHERE [Lab001].[product].ProductID = @productID
RETURN(@returnValue)
END
GO


-- b. Run the function (experiment with different parameters)
SELECT Lab001.CalculateDiscountedPrice(102, .50) AS DiscountedPrice
GO

-- c. Create a new function called Lab001.calculate_discounted_percent that takes 
-- a product id and a new price and returns the discount percentage
CREATE OR ALTER FUNCTION Lab001.calculate_discounted_percent(
@productID INT,
@newPrice NUMERIC(10,3))
RETURNS MONEY
AS
BEGIN
DECLARE @returnValue AS MONEY;
SELECT @returnValue = ((ProductPrice - @newPrice)/ProductPrice)
FROM [Lab001].[product]
WHERE [Lab001].[product].ProductID = @productID
RETURN(@returnValue)
END
GO
-- For example, if ProductID 103 was discounted to $29.50 it would return approx 0.81

-- d. Run the function discounting ProductID 103 to $29.50 and take a screenshot
SELECT Lab001.calculate_discounted_percent(103, 29.50) AS DiscountedPercent
GO