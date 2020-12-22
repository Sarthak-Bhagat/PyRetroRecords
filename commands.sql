DROP DATABASE RetroRecords;


CREATE DATABASE RetroRecords;

USE RetroRecords;


CREATE TABLE Records(
	RID INT NOT NULL  AUTO_INCREMENT,
	Name VARCHAR(255) NOT NULL,
	Artist VARCHAR(255) NOT NULL,
	Status VARCHAR(255) NOT NULL DEFAULT 'Available',
	PRIMARY KEY (RID)
);

CREATE TABLE Customer(
	CID INT AUTO_INCREMENT,
	Name VARCHAR(255) NOT NULL,
	CUsr VARCHAR(255),
	CPas VARCHAR(255),
	Phone_No VARCHAR(255),
	PRIMARY KEY (CID)
);

CREATE TABLE RENTED(
	RID INT,
	CID INT
);

CREATE TABLE Employee(
	EID INT AUTO_INCREMENT,
	Name VARCHAR(255) NOT NULL,
	EUsr VARCHAR(255),
	EPas VARCHAR(255),
	Phone_No VARCHAR(255),
	PRIMARY KEY (EID)
);

INSERT INTO Employee(Name, EUsr, EPas,Phone_no) VALUES('Sarthak','admin','admin','9137834443');

INSERT INTO Customer(Name, CUsr, CPas,Phone_no) VALUES('Pooja','admin','admin','232084712');

INSERT INTO Customer(Name, CUsr, CPas, Phone_No) VALUES('Raghav Sharma','Raghav65','R@556','983461793');

INSERT INTO Customer(Name, CUsr, CPas, Phone_No) VALUES('Pooja Bendale',' Pooja7','PBendale','9702050041');

INSERT INTO Customer(Name, CUsr, CPas, Phone_No) VALUES('Sarthak Bhagat','dezxerneas','PBendale','9702050041');

INSERT INTO Employee(Name, Phone_No, EUsr, EPas) VALUES('Shreeya Nair','983461793','ShreeyaN','Nair45');

INSERT INTO Employee(Name, Phone_No, EUsr, EPas) VALUES('Sanika Badhe','9865234158','San22 ','SBadhe');

INSERT INTO Records (Name,Artist) VALUES ('O Mere Dil Ke Chain','Kishore Kumar');

INSERT INTO Records (Name,Artist) VALUES ('Kya Hua Tera Wada','Mohammed Rafi');



SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE, COLUMN_TYPE, COLUMN_DEFAULT, COLUMN_KEY, EXTRA FROM information_schema.columns WHERE ( table_schema = 'RetroRecords') ORDER BY TABLE_NAME;


