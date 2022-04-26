BEGIN TRANSACTION;
CREATE TABLE "Customer"
(
    id   SMALLINT UNSIGNED IDENTITY(1, 1) not null
        primary key,
    name VARCHAR(50) default null not null,
    city VARCHAR(50)                      not null,
    date DATE                             not null
);
INSERT INTO "Customer" VALUES(1,'Adam','Lublin','2011-02-05');
INSERT INTO "Customer" VALUES(2,'Monika','Gdynia','2011-02-19');
INSERT INTO "Customer" VALUES(3,'Natalia','Zakopane','2011-02-23');
INSERT INTO "Customer" VALUES(4,'Katarzyna','Lublin','2011-03-08');
INSERT INTO "Customer" VALUES(5,'Marcin','Warszawa','2011-03-21');
CREATE TABLE "Order_product" (
	"order_id"	SMALLINT UNSIGNED NOT NULL,
	"product_id"	SMALLINT UNSIGNED NOT NULL,
	"amount"	TINYINT(2) NOT NULL
);
INSERT INTO "Order_product" VALUES(1,2,2);
INSERT INTO "Order_product" VALUES(1,4,1);
INSERT INTO "Order_product" VALUES(2,6,1);
INSERT INTO "Order_product" VALUES(2,8,1);
INSERT INTO "Order_product" VALUES(2,5,2);
INSERT INTO "Order_product" VALUES(3,5,1);
INSERT INTO "Order_product" VALUES(3,7,2);
INSERT INTO "Order_product" VALUES(4,5,1);
INSERT INTO "Order_product" VALUES(4,2,1);
INSERT INTO "Order_product" VALUES(4,7,2);
INSERT INTO "Order_product" VALUES(5,4,1);
INSERT INTO "Order_product" VALUES(6,6,1);
CREATE TABLE "Product" (
	"id"	SMALLINT UNSIGNED IDENTITY(1 , 1) NOT NULL,
	"name"	VARCHAR(50) NOT NULL,
	"price"	FLOAT NOT NULL,
	"amount"	TINYINT(2) NOT NULL,
	"date"	DATE NOT NULL,
	PRIMARY KEY("id")
);
INSERT INTO "Product" VALUES(5,'Spodnie',133.1,5,'2011-02-01');
INSERT INTO "Product" VALUES(10,'Kaplusz',60.0,4,'2011-02-20');
INSERT INTO "Product" VALUES(11,'Kaplusz',60.0,4,'2011-02-20');
INSERT INTO "Product" VALUES(12,'Kaplusz',60.0,6,'2011-02-20');
INSERT INTO "Product" VALUES(13,'Kaplusz',26.0,5,'2011-02-20');
INSERT INTO "Product" VALUES(14,'Kaplusz',61.0,7,'2011-02-20');
INSERT INTO "Product" VALUES(15,'Kaplusz',25.0,1,'2011-02-20');
INSERT INTO "Product" VALUES(16,'Kaplusz',58.0,6,'2011-02-20');
INSERT INTO "Product" VALUES(17,'Kaplusz',36.0,7,'2011-02-20');
INSERT INTO "Product" VALUES(18,'Kaplusz',6.0,7,'2011-02-20');
INSERT INTO "Product" VALUES(19,'Kaplusz',3.0,8,'2011-02-20');
INSERT INTO "Product" VALUES(20,'Kaplusz',79.0,6,'2011-02-20');
INSERT INTO "Product" VALUES(21,'Kaplusz',13.0,0,'2011-02-20');
INSERT INTO "Product" VALUES(22,'Kaplusz',6.0,1,'2011-02-20');
INSERT INTO "Product" VALUES(23,'Kaplusz',8.0,9,'2011-02-20');
INSERT INTO "Product" VALUES(24,'Kaplusz',57.0,5,'2011-02-20');
INSERT INTO "Product" VALUES(25,'Kaplusz',11.0,6,'2011-02-20');
INSERT INTO "Product" VALUES(26,'Kaplusz',52.0,6,'2011-02-20');
INSERT INTO "Product" VALUES(27,'Kaplusz',66.0,9,'2011-02-20');
INSERT INTO "Product" VALUES(28,'Kaplusz',46.0,6,'2011-02-20');
INSERT INTO "Product" VALUES(29,'Kaplusz',51.0,2,'2011-02-20');
INSERT INTO "Product" VALUES(30,'Kaplusz',8.0,6,'2011-02-20');
INSERT INTO "Product" VALUES(31,'Kaplusz',77.0,9,'2011-02-20');
INSERT INTO "Product" VALUES(32,'Kaplusz',13.0,4,'2011-02-20');
INSERT INTO "Product" VALUES(33,'Kaplusz',3.0,4,'2011-02-20');
INSERT INTO "Product" VALUES(34,'Kaplusz',67.0,3,'2011-02-20');
INSERT INTO "Product" VALUES(35,'Kaplusz',49.0,2,'2011-02-20');
CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real);
INSERT INTO "stocks" VALUES('2006-01-05','BUY','RHAT',100.0,35.14);
INSERT INTO "stocks" VALUES('2006-03-28','BUY','IBM',1000.0,45.0);
INSERT INTO "stocks" VALUES('2006-04-05','BUY','MSFT',1000.0,72.0);
INSERT INTO "stocks" VALUES('2006-04-06','SELL','IBM',500.0,53.0);
COMMIT;
