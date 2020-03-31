Select
CustomerID
,CompanyName
,Region
From Customers
Where customerID in (Select 
customerID
    From Orders
    Where Freight > 100);

subqueries immer von innen nach aussen schreiben und lesen.
subquery selects can only retrieve a single column.
formatierer unter poorsql.com
subqueries können auch ein zusätzliches z.B. berechnetes 
Feld in die Ausgabe hinzufügen

Select customer_name 
    ,customer_state 
    (Select count(*) as Orders
    from Orders
    where Orders.customer_id = Customer.customer_id) AS Orders
from Customers
order by customer_name

inner joins bringen nur die datensätze, wo ein
match (auf beiden seiten) gefunden wird.

left join returns alle daten von der linken seite, aber
kann ein Null enthalten für die rechte seite

|| für konkatenation von strings

case kann in select, insert, delete und update verwendet werden

By including a GROUP BY clause 
functions such as SUM and COUNT are applied to groups of items sharing values.
When you specify GROUP BY continent the result is 
that you get only one row for each different value of continent. 
All the other columns must be "aggregated" by one of SUM, COUNT ...

The HAVING clause allows use to filter the groups which are displayed.
The WHERE clause filters rows before the aggregation, 
the HAVING clause filters after the aggregation.