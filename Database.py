import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="qwerty22",
    database="Logbook"
    )

mycursor = db.cursor()


mycursor.execute("DROP TABLE Grain")
mycursor.execute("DROP TABLE Hop")
mycursor.execute("DROP TABLE Yeast")
mycursor.execute("DROP TABLE Ingredients")

mycursor.execute("""CREATE TABLE Ingredients (
    IngredientsID int PRIMARY KEY AUTO_INCREMENT, 
    Name VARCHAR(50), 
    Class ENUM('Grain','Hop','Yeast','Additional','Spice'),
    Brand VARCHAR(50)
    )""")
mycursor.execute("""CREATE TABLE Grain (
    GrainID int PRIMARY KEY AUTO_INCREMENT,
    IngredientsID int,
    Material VARCHAR(50),
    ColorMin SMALLINT,
    ColorMax SMALLINT,
    Rate SMALLINT,
    Result VARCHAR(100),
    Style VARCHAR(100),
    Description VARCHAR(100),
    FOREIGN KEY (IngredientsID) REFERENCES Ingredients (IngredientsID)
    )""")
mycursor.execute("""CREATE TABLE Hop (
    HopID int PRIMARY KEY AUTO_INCREMENT,
    IngredientsID int,
    AcidMin SMALLINT,
    AcidMax SMALLINT,
    Citrusy TINYINT,
    Floral TINYINT,
    Fruity TINYINT,
    Herbal TINYINT,
    Other TINYINT,
    Resinous TINYINT,
    Spicy TINYINT,
    Alternative VARCHAR(100),
    Purpose ENUM('Aroma','Bitter','Both'),
    Style VARCHAR(100),
    Description VARCHAR(100),
    FOREIGN KEY (IngredientsID) REFERENCES Ingredients (IngredientsID)
    )""")
mycursor.execute("""CREATE TABLE Yeast (
    YeastID int PRIMARY KEY AUTO_INCREMENT,
    IngredientsID int,
    AttenMin SMALLINT,
    AttenMax SMALLINT,
    Tolerance SMALLINT,
    TempMin SMALLINT,
    TempMax SMALLINT,
    Floculation ENUM('High','Medium','Low'),
    VG ENUM('Yes','No'),
    Dried ENUM('Yes','No') DEFAULT 'No',
    Fridge ENUM('Yes','No') DEFAULT 'No',
    Freezer ENUM('Yes','No') DEFAULT 'No',
    Style VARCHAR(100),
    Description VARCHAR(100),
    FOREIGN KEY (IngredientsID) REFERENCES Ingredients (IngredientsID)
    )""")

mycursor.execute("""CREATE TABLE Additional(
    AdditionalID int PRIMARY KEY AUTO_INCREMENT,
    IngredientsID int,
    When VARCHAR(50),
    Style VARCHAR(100),
    Description VARCHAR(100),
    FOREIGN KEY (IngredientsID) REFERENCES Ingredients (IngredientsID)    
    )""")

mycursor.execute("""CREATE TABLE Recipe(
    AdditionalID int PRIMARY KEY,
    IngredientsID int,
    NameBeer VARCHAR(50),
    Style VARCHAR(50),
    Description VARCHAR(100),
    DateStart DATETIME,
    DateBottle DATETIME,
    Bottle SMALLINT,
    FOREIGN KEY (IngredientsID) REFERENCES Ingredients (IngredientsID)
    )""")

#Misschien Material veranderen naar ENUM
mycursor.execute("DESCRIBE Ingredients")
for x in mycursor:
    print(x)

db.commit()
"""
#to add ingredients
pers_1 = ("Wheat Malt","Grain")

sql = "INSERT INTO Ingredients (name,class) VALUES (%s,%s)"
val = pers_1
mycursor.execute(sql,val)
db.commit()
""" 
mycursor.execute("SELECT * FROM Ingredients")
for x in mycursor:
    print(x)

#LAST_INSERT_ID() tijdelijk ff hier neer zetten voor herreering

"""
class Person:
    def __init__(self, name,age)
        self.name = name
        self.age = age

pers_1 = ("Test",27)

sql = "INSERT INTO Person (name,age) VALUES (%s,%s)"
val = pers_1
mycursor.execute(sql,val)
db.commit()

#def insert_person(pers):
#    with db:
#        mycursor.execute("INSERT INTO Person (name,age) VALUES (%s,%s)", pers)
#        db.commit()


#insert_person(pers_1)
mycursor.execute("SELECT * FROM Person")
for x in mycursor:
    print(x)
"""
