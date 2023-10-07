CREATE DATABASE Guvi_CodeKata;

USE Guvi_CodeKata;

CREATE TABLE Module_Details (
    Module_ID INT AUTO_INCREMENT,
    Module_Name NVARCHAR(200),
    Total_Problems INT,
    Total_Solved_Problems INT,
    Total_Resultant_Issue INT,
    List_Of_Solved_Problems NVARCHAR(500),
    List_Of_Unsolved_Problems NVARCHAR(500),
    List_Of_Issues_In_Problems NVARCHAR(500),
    CONSTRAINT PK PRIMARY KEY (Module_ID)
);

INSERT INTO Module_Details VALUES(1, "Input/Output", 10, 10, 0, "[1-10]", NULL, NULL);
INSERT INTO Module_Details VALUES(2, "Absolute Beginner", 30, 30, 0, "[1-30]", NULL, NULL);
INSERT INTO Module_Details VALUES(3, "Array", 308, 111, 27, "[1,2,6,8,9,11-15,17-20,22,24,25,27-35,33,37-45,50-52,54-60,62,65,66,68,70,72-74,77-80,83,84,86-91,93,95-97,100,102,104,107,115,118,124,135,136,141,144,146,152,153,158,160,161,164,166,172-174,176,177,180,188,189,192,196,197,200,202,208,211,212,222,223,232,238,244,249]", "[4,5,16,21,23,26,34,44,53,61,67,69,71,75,76,81,82,85,92,94,98,99,101,103,105,106,108-114,116,117,119,122,125,126,129-132,134,138-140,142,143,145,148,150,151,154-157,159,162,163,165,167-169,171,178,181-187,190,191,193-195,198,201,203-207,209,210,213-215,217-221,224-231,234-237,239,240,242,243,245-248,250-256,258-283,285-308]", "[3,7,10,31,32,43,49,63,64,92,98,123,127,128,133,137,147,149,170,175,179,199,216,233,241,257,284]");
INSERT INTO Module_Details VALUES(4, "Mathematics", 192, 70, 9, "[1,2,4,6,7,9,10,12,13,16,17,19-23,25,27,28,30,32-35,37-47,49-52,54,55,57,58,63,65,71,72,77,80-82,86,87,89-90,92,100,110,111,117,119,122,124,126,128,131,135,136,150]", "[5,8,11,14,15,18,24,31,36,48,53,56,59,60,62,64,66-70,73,75,76,78,79,83-85,88,91,93-99,101-109,112-116,118,121,125,127,129,130,132,133,137-149,151-155,157-163,165-192]", "[3,26,29,61,74,123,134,156,164]");
INSERT INTO Module_Details VALUES(5, "Strings", 196, 93, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(6, "Basics", 41, 36, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(7, "Companies", 99, 17, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(8, "Looping", 14, 12, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(9, "Guvi-Learning-Path", 46, 19, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(10, "Numbers", 22, 10, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(11, "Amazon", 38, 15, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(12, "Sorting", 38, 10, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(13, "Patterns", 61, 6, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(14, "Microsoft", 22, 11, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(15, "Searching", 21, 11, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(16, "Bitwise", 10, 4, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(17, "Samsung", 18, 6, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(18, "Zen", 53, 46, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(19, "Algorithm", 16, 7, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(20, "Zoho", 11, 4, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(21, "Accolite", 12, 6, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(22, "Data Structures", 11, 3, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(23, "Bit Manipulation", 12, 2, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(24, "Walmart", 11, 3, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(25, "Matrix", 37, 0, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(26, "MakeMyTrip", 10, 3, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(27, "Hashing", 28, 2, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(28, "Stack", 19, 2, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(29, "Trees And Graphs", 20, 1, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(30, "Linked List", 14, 1, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(31, "Queue", 11, 1, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(32, "Dynamic Programming", 14, 1, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(33, "Tries", 22, 0, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(34, "Segment Tree", 21, 0, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(35, "KPRIET-U19CS307", 14, 3, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(36, "OOPS - KPR", 11, 0, 0, NULL, NULL, NULL);
INSERT INTO Module_Details VALUES(37, "Advanced DS - KPR", 10, 0, 0, NULL, NULL, NULL);

CREATE VIEW Total_Problems_Solved AS SELECT SUM(Total_Solved_Problems) FROM Module_Details;

CREATE VIEW Yet_To_Solve_And_Complete AS SELECT SUM(Total_Problems) - SUM(Total_Solved_Problems) FROM Module_Details;

CREATE VIEW Yet_To_Solve_By_Module AS SELECT Module_ID, Module_Name, Total_Problems - Total_Solved_Problems AS Yet_To_Solve FROM Module_Details;

SELECT * FROM Total_Problems_Solved;
SELECT * FROM Yet_To_Solve_And_Complete;
SELECT * FROM Yet_To_Solve_By_Module;
