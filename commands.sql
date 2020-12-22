DROP DATABASE RetroRecords;


CREATE DATABASE RetroRecords;

USE RetroRecords;


CREATE TABLE Records(
	RID INT NOT NULL  AUTO_INCREMENT,
	Stock INT NOT NULL  DEFAULT 1,
	Name VARCHAR(255) NOT NULL,
	Artist VARCHAR(255) NOT NULL,
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
	CID INT,
	NRENTED INT DEFAULT 1
);

CREATE TABLE Employee(
	EID INT AUTO_INCREMENT,
	Name VARCHAR(255) NOT NULL,
	EUsr VARCHAR(255),
	EPas VARCHAR(255),
	Phone_No VARCHAR(255),
	PRIMARY KEY (EID)
);

INSERT INTO Employee(Name, EUsr, EPas,Phone_no) VALUES('EMP1','admin','admin','1111111111');

INSERT INTO Customer(Name, CUsr, CPas,Phone_no) VALUES('CUS1','admin','admin','2222222222');

INSERT INTO Customer(Name, CUsr, CPas, Phone_No) VALUES('CUS2','CUS2','pass','3333333333');

INSERT INTO Customer(Name, CUsr, CPas, Phone_No) VALUES('CUS3',' CUS3','pass','4444444444');

INSERT INTO Customer(Name, CUsr, CPas, Phone_No) VALUES('CUS4','CUS4','pass','5555555555');

INSERT INTO Employee(Name, Phone_No, EUsr, EPas) VALUES('EMP2','6666666666','EMP2','pass');

INSERT INTO Employee(Name, Phone_No, EUsr, EPas) VALUES('EMP3','7777777777','EMP3 ','pass');

INSERT INTO Records (Name,Artist,Stock) VALUES ('O Mere Dil Ke Chain','Kishore Kumar',32);

INSERT INTO Records (Name,Artist,Stock) VALUES ('Kya Hua Tera Wada','Mohammed Rafi',32);



SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE, COLUMN_TYPE, COLUMN_DEFAULT, COLUMN_KEY, EXTRA FROM information_schema.columns WHERE ( table_schema = 'RetroRecords') ORDER BY TABLE_NAME;


