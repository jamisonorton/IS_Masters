SELECT 'Customer' AS table_name, COUNT(*) number_records FROM Lab001.Customer
UNION ALL
SELECT 'OrderHeader' AS table_name, COUNT(*) number_records FROM Lab001.OrderHeader
UNION ALL
SELECT 'OrderLine' AS table_name, COUNT(*) number_records FROM Lab001.OrderLine
UNION ALL
SELECT 'Product' AS table_name, COUNT(*) number_records FROM Lab001.Product
;