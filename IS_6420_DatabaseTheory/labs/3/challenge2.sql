SELECT first_name, last_name, department_name
FROM [dbo].[employee], [dbo].[department]
WHERE [dbo].[employee].department_number = [dbo].[department].department_number
;