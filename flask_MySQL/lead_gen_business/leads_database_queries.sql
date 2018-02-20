/* 1. What query would you run to get the total revenue for March of 2012? */
USE lead_gen_business;
SELECT sum(billing.amount)
FROM billing
		WHERE billing.charged_datetime LIKE '2012-03%';


/* 2. What query would you run to get total revenue collected from 
the client with an id of 2? */
USE lead_gen_business;
SELECT sum(billing.amount)
FROM billing
		JOIN clients ON billing.client_id = clients.client_id
		WHERE clients.client_id = 2;

/* 3. What query would you run to get all the sites that client=10 owns? */
USE lead_gen_business;
SELECT sites.domain_name, clients.client_id, CONCAT(clients.first_name, " ", clients.last_name) AS domain_owner
FROM sites
		JOIN clients ON sites.client_id = clients.client_id
		WHERE clients.client_id = 10;

/* 4. What query would you run to get total # of sites created per month per year 
for the client with an id of 1? What about for client=20? */
USE lead_gen_business;
SELECT YEAR(sites.created_datetime) AS sites_year, MONTHNAME(sites.created_datetime) AS sites_month, COUNT(sites.site_id) AS total_number_of_sites
FROM sites
	JOIN clients ON sites.client_id = clients.client_id
	WHERE clients.client_id = 1
		GROUP BY sites_year, sites_month;
SELECT YEAR(sites.created_datetime) AS sites_year, MONTHNAME(sites.created_datetime) AS sites_month, COUNT(sites.site_id) AS total_number_of_sites
FROM sites
	JOIN clients ON sites.client_id = clients.client_id
	WHERE clients.client_id = 20
		GROUP BY sites_year, sites_month;

/* 5. What query would you run to get the total # of leads generated 
for each of the sites between January 1, 2011 to February 15, 2011? */
USE lead_gen_business;
SELECT sites.domain_name, COUNT( leads.leads_id) AS total_number_of_leads, DATE_FORMAT(leads.registered_datetime, '%M %d, %Y') AS date_generated
FROM sites
	JOIN leads ON sites.site_id = leads.site_id
		WHERE leads.registered_datetime  BETWEEN '2011-01-01 00:00:00' AND '2011-02-15 23:59:59'
		GROUP BY sites.domain_name, date_generated;

/* 6. What query would you run to get a list of client names and 
the total # of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011? */
USE lead_gen_business;
SELECT clients.client_id, CONCAT( clients.first_name, " ", clients.last_name) AS client_name, COUNT( leads.leads_id) AS total_number_of_leads
FROM clients
	JOIN sites ON sites.client_id = clients.client_id
	JOIN leads ON sites.site_id = leads.site_id
		WHERE leads.registered_datetime  BETWEEN '2011-01-01 00:00:00' AND '2011-12-31 23:59:59'
		GROUP BY  clients.client_id;


/* 7. What query would you run to get a list of client names 
and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011? */
USE lead_gen_business;
SELECT clients.client_id, CONCAT( clients.first_name, " ", clients.last_name) AS client_name, MONTHNAME(leads.registered_datetime ) AS month, COUNT( leads.leads_id) AS total_number_of_leads
FROM clients
	JOIN sites ON sites.client_id = clients.client_id
	JOIN leads ON sites.site_id = leads.site_id
		WHERE leads.registered_datetime  LIKE '2011%' AND MONTH(leads.registered_datetime) BETWEEN 1 and 6
		GROUP BY  month, clients.client_id
        ORDER BY (CASE month
			WHEN 'January' 	THEN 1
			WHEN 'February' THEN 2
			WHEN 'March' THEN 3
			WHEN 'April' THEN 4
			WHEN 'May' THEN 5
            WHEN 'June' THEN 6
			ELSE 100 END) ASC;


/* 8. What query would you run to get a list of client names and 
the total # of leads we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011?  
Order this query by client id.  
Come up with a second query that shows all the clients, the site name(s), and 
the total number of leads generated from each site for all time. */
USE lead_gen_business;
SELECT clients.client_id, CONCAT( clients.first_name, " ", clients.last_name) AS client_name, sites.domain_name, COUNT( leads.leads_id) AS total_number_of_leads
FROM clients
	JOIN sites ON sites.client_id = clients.client_id
	JOIN leads ON sites.site_id = leads.site_id
		WHERE leads.registered_datetime  BETWEEN '2011-01-01 00:00:00' AND '2011-12-31 23:59:59'
		GROUP BY  clients.client_id, sites.domain_name
        ORDER BY clients.client_id;

SELECT clients.client_id, CONCAT( clients.first_name, " ", clients.last_name) AS client_name, sites.domain_name, COUNT( leads.leads_id) AS total_number_of_leads
FROM clients
	JOIN sites ON sites.client_id = clients.client_id
	JOIN leads ON sites.site_id = leads.site_id
		GROUP BY  clients.client_id, sites.domain_name
        ORDER BY clients.client_id;
        
        
/* 9. Write a single query that retrieves total revenue collected from each client 
for each month of the year. Order it by client id. */
USE lead_gen_business;
SELECT clients.client_id, CONCAT( clients.first_name, " ", clients.last_name) AS client_name, MONTHNAME( billing.charged_datetime ) AS month, YEAR( billing.charged_datetime ) AS year, sum(billing.amount) as total_revenue
FROM billing
		JOIN clients ON billing.client_id = clients.client_id
        GROUP BY clients.client_id, year, month
		ORDER BY clients.client_id, year, (CASE month
			WHEN 'January' 	THEN 1
			WHEN 'February' THEN 2
			WHEN 'March' THEN 3
			WHEN 'April' THEN 4
			WHEN 'May' THEN 5
            WHEN 'June' THEN 6
			WHEN 'July' THEN 7
			WHEN 'August' THEN 8
			WHEN 'September' THEN 9
			WHEN 'October' THEN 10
			WHEN 'November' THEN 11
            WHEN 'December' THEN 12
			ELSE 100 END) ASC;


/* 10. Write a single query that retrieves all the sites that each client owns. 
Group the results so that each row shows a new client. 
It will become clearer when you add a new field called 'sites' that has 
all the sites that the client owns. (HINT: use GROUP_CONCAT) */
USE lead_gen_business;
SELECT clients.client_id, CONCAT(clients.first_name, " ", clients.last_name) AS domain_owner, GROUP_CONCAT(sites.domain_name ORDER BY sites.domain_name SEPARATOR ' / ')
FROM sites
		JOIN clients ON sites.client_id = clients.client_id
		GROUP BY clients.client_id;

