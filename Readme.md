||Problem Statement: Make an application for the database of a music record store.


||Database: RetroRecords \\Import commands.sql


||Tables:4 :
ENTITIES

	Customer table: Pri CID;Name;Address;
	Sales_Record table;Cid;Cost; Pri RID


NON-ENTITIES
	Rented_Records: Pri rid;Cid; 
	Records: Pri Rid;Name;Artist;Satus;Cost 
	Dates: Pri TID;AoR;ID;Rented_from;Return_Date


||ENTITIES:

	RECORD
	CUSTOMER
	EMPOYEE
	DATES




||Attributes:

	RECORDS:Public Record ID:PRID;PRIMARY 
	RECORD
	EMPOYEE		INT Auto increment		
		Record Title: Name							VARCHAR
 		Record by: Artist							VARCHAR
		Record Status:(Available/Rented): Status				VARCHAR						INT
			

	CUSTOMER:Customer ID:CID; PRIMARY KEY						INT AUTO INCREMENT
		 Customer's Name: Name							VARCHAR



		 Customer's Username:CUsr;OPTIONAL					VARCHAR					
		 Customer's Password:Cpas;OPTIONAL					VARCHAR


	EMPLOYEE:Employee ID:EID; PRIMARY KEY						INT AUTO INCREMENT
		 Employee's Name: Name							VARCHAR
		 Employee's Address:Address						VARCHAR ??
		 Employee's Username:EUsr						VARCHAR	
		 Employee's Password:Epas						VARCHAR
	


||WINDOWS:

	1]  LOGIN :	ARE YOU AN EMPLOYEE OR AN CUSTOMER?
		E] EMPLOYEE ID AND PASSWORD
	CUSTOMER] EXISTING OR NEW CUsr&CPas if EXISTING



	2C]  CUSTOMER:	Just main.py But remove AddRecords.py, also add SellRecord, SellAlbum, RentAlbum. 
					Maybe add options for viewing Records or ALbums put other functions in their window.
		        
		           	So Window with "What are you looking for?"
		          					R]Records
		          					A]Albums
			
			3R] ViewRecords,BuyRecord,RentRecord,ReturnRecord				\\Not sure if we want to also buy Records
			3A] ViewAlbums,BuyAlbums,RentAlbums,SellAlbums								\\Not sure if we want to also buy Albums
					\\Implement Buy\Rent in View




	2E]  EMPLOYEE: AddRecords, DeleteRecords, CreateAlbum, DeleteAlbum, AddEmployee, EDIT

		EDIT] 1]Edit RecordData
		      2]Edit AlbumData
		      3]New Employee 			\\Maybe also add condion that the employee adding another has to be allowed






