DROP DATABASE IF EXISTS ticket_sales;

CREATE DATABASE ticket_sales;

USE ticket_sales;

CREATE TABLE tickets(
  ticket_id INT NOT NULL,
  trans_date DATE NOT NULL,
  event_id INT NOT NULL,
  event_name TEXT(50) NOT NULL,
  event_date DATE NOT NULL,
  event_type TEXT(10) NOT NULL,
  event_city TEXT(20) NOT NULL,
  customer_id INT NOT NULL,
  price DECIMAL NOT NULL,
  num_tickets INT NOT NULL
);