import sqlite3
conn = sqlite3.connect('princess.db') # Warning: This file is created in the current directory

conn.execute("DROP TABLE if exists User")
conn.execute("DROP TABLE if exists GameHistory ")
conn.execute("DROP TABLE if exists Questions")
conn.execute("DROP TABLE if exists Answers")
conn.execute("DROP TABLE if exists Options")

conn.execute("CREATE TABLE User (UserID INTEGER PRIMARY KEY AUTOINCREMENT, EmailAddress nvarchar(300) , CurrentGameLevel char(1000) )")

conn.execute("CREATE TABLE GameHistory (UserID INTEGER PRIMARY KEY AUTOINCREMENT , QuestionID INTEGER)")

conn.execute("CREATE TABLE Questions (QuestionID INTEGER PRIMARY KEY,Question nvarchar(500)  , GameLevel char(1000) )")

conn.execute("CREATE TABLE Answers (QuestionID INTEGER PRIMARY KEY, CorrectOptionID char(30) )")

conn.execute("CREATE TABLE Options (OptionID char(30)    , QuestionID INTEGER, Options_value CHAR(100))")





conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (1,'Which insect inspired the term computer bug?','EntryLevel')")
conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (2,'Which of these U.S. presidents appeared on the television series LaughIn ? ','EntryLevel')")
conn.execute ("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (3,'which of the following landlocked countries is entirely contained within another country?', 'EntryLevel')")
conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (4,'who is credited with inventing the first mass produced helicopter?','MidLevel')")
conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (5,'What letter must appear at the beginning of the registration number of all non-military aircraft in the U.S.?','MidLevel')")
conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (6,'Who did artist Grant Wood use as the model for the farmer in his classic painting an American Gothic?','MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (7,'The U.S. icon Uncle sam was based on samuel wilson,who worked during the war of 1812 as a what?','MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (8,'Which of the following men does not have a chemical element named after him?','MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (9,'Where should choking victims place their hands to indicate to others that they need help?' , 'MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (10,'In the Road Runner and Coyote; cartoons, what famous sound does the Road Runner make?','MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (11,'Which of these dance names is used to describe a fashionable dot?','HighLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (12,'What is the only position on a football team that can be sacked? ',  'HighLevel')")


conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (13,'What country launched its first space rocket January 1961?','MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (14,'Which American state is nicknamed The Diamond State?','MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (15,'In these series, you will be looking at both the letter pattern and the number pattern.Fill the blank in the middle of the series or end of the series?' , 'MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (16,'Who is the only American president elected unopposed?','MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (17,'What was the first credit card?','HighLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (18,'Who Wrote the Harry Potter Series?? ',  'HighLevel')")


conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (19,'On What Continent is Zambia Located?','MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (20,'What is 6 inches bigger in Summer?','MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (21,'Who did the USA buy the Virgin Islands from?' , 'MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (22,'What is the staple food of one third of the world’s population?','MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (23,'Who said COMPUTERS ARE USELESS THEY ONLY GIVE YOU ANSWERS?','HighLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (24,'25% of Americans believe which fictional character is real? ',  'HighLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (25,'Chrometrophobia is the fear of what?','MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (26,'In the UK 60% of pets have what?','MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (27,'Which of these games might start with one kid saying, “taking care of business” and other saying “baking carrot biscuits”?' , 'MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (28,'I PITY THE FOOL is a catchphrase of which famous American?','MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (29,'Denny’s restaurants offer a signature breakfast dish names after what sports team?','HighLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (30,'How many U.S states have names that begin with the word “New”? ',  'HighLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (31,'Slightly inebriated is a common definition for which of these words?','MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (32,'What is the most chosen name for US school’s sports teams?','MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (33,'Which profession drinks the most coffee?' , 'MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (34,'Which duo has won seven Oscars?','MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (35,'Linus Torvalds invented and wrote what?','HighLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (36,'What is measured on the Torro scale?',  'HighLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (37,'What colour is the wax covering Gouda cheese?','MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (38,'Triton is the largest satellite of which planet?','MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (39,'Which of these operating systems was written by Linus Torvalds?' , 'MidLevel')")

conn.execute("INSERT into Questions(QuestionID,Question,GameLevel) VALUES (40,'What is software testing?','MidLevel')")


conn.execute("Insert into GameHistory(QuestionID) values (1)")
conn.execute("Insert into GameHistory(QuestionID) values (2)")
conn.execute("Insert into GameHistory(QuestionID) values (3)")
conn.execute("Insert into GameHistory(QuestionID) values (4)")
conn.execute("Insert into GameHistory(QuestionID) values (5)")
conn.execute("Insert into GameHistory(QuestionID) values (6)")
conn.execute("Insert into GameHistory(QuestionID) values (7)")
conn.execute("Insert into GameHistory(QuestionID) values (8)")
conn.execute("Insert into GameHistory(QuestionID) values (9)")
conn.execute("Insert into GameHistory(QuestionID) values (10)")
conn.execute("Insert into GameHistory(QuestionID) values (11)")
conn.execute("Insert into GameHistory(QuestionID) values (12)")
conn.execute("Insert into GameHistory(QuestionID) values (13)")
conn.execute("Insert into GameHistory(QuestionID) values (14)")
conn.execute("Insert into GameHistory(QuestionID) values (15)")
conn.execute("Insert into GameHistory(QuestionID) values (16)")
conn.execute("Insert into GameHistory(QuestionID) values (17)")
conn.execute("Insert into GameHistory(QuestionID) values (18)")
conn.execute("Insert into GameHistory(QuestionID) values (19)")
conn.execute("Insert into GameHistory(QuestionID) values (20)")
conn.execute("Insert into GameHistory(QuestionID) values (21)")
conn.execute("Insert into GameHistory(QuestionID) values (22)")
conn.execute("Insert into GameHistory(QuestionID) values (23)")
conn.execute("Insert into GameHistory(QuestionID) values (24)")
conn.execute("Insert into GameHistory(QuestionID) values (25)")
conn.execute("Insert into GameHistory(QuestionID) values (26)")
conn.execute("Insert into GameHistory(QuestionID) values (27)")
conn.execute("Insert into GameHistory(QuestionID) values (28)")
conn.execute("Insert into GameHistory(QuestionID) values (29)")
conn.execute("Insert into GameHistory(QuestionID) values (30)")
conn.execute("Insert into GameHistory(QuestionID) values (31)")
conn.execute("Insert into GameHistory(QuestionID) values (32)")
conn.execute("Insert into GameHistory(QuestionID) values (33)")
conn.execute("Insert into GameHistory(QuestionID) values (34)")
conn.execute("Insert into GameHistory(QuestionID) values (35)")
conn.execute("Insert into GameHistory(QuestionID) values (36)")
conn.execute("Insert into GameHistory(QuestionID) values (37)")
conn.execute("Insert into GameHistory(QuestionID) values (38)")
conn.execute("Insert into GameHistory(QuestionID) values (39)")
conn.execute("Insert into GameHistory(QuestionID) values (40)")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',1,'Moth')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',1,'Cockroach')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',1,'Fly')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',1,'Beetle')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',2,'Lyndon Johnson')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',2,'Richard Nixon')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',2,'Jimmy carter')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',2,'Gerald Ford')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',3,'Lesotho')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',3,'Burkina Faso')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',3,'Mongolia')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',3,'Luxembourg')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',4,'Igor sikorsky')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',4,'Elmer sperry')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',4,'ferdinard von zeppelin')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',4,'Gottlieb Daimler')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',5,'N')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',5,'A')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',5,'U')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',5,'L')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',6,'Traveling  Salesman')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',6,'Local  Sheriff')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',6,'His dentist')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',6,'His butcher')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',7,'Meat Inspector')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',7,'Mail deliver')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',7,'Historian')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',7,'Weapons Mechanic')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',8,'Albert Einstein')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',8,'Niels bohr')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',8,'Issac Newton')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',8,'Enrico Fermi')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',9,'Over the eyes')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',9,'On the knees')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',9,'Around the throat')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',9,'On the hips?')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',10,'ping!ping!')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',10,'beep!beep!')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',10,'Aooga!Aooga!')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',10,'Vroom!Vroom!')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',11,'Hora')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',11,'Swing')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',11,'Lambada')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',11,'Polka')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',12,'Center')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',12,'Wide receiver')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',12,'Tight End')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',12,'Quarter back')")


conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',13,'Europe')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',13,'United States')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',13,'India')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',13,'Italy')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',14,'California')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',14,'Florida')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',14,'Delaware')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',14,'New Jersey')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',15,'CMN')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',15,'UJI')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',15,'VIJ')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',15,'IJT')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',16,'Donald Trump')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',16,'George Washington')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',16,'Barak Obama')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',16,'Bill Clinton')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',17,'MasterCard')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',17,'Visa')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',17,'Diners Club')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',17,'Capital One')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',18,'J.R.R Tolkien')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',18,'J.K Rowling')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',18,'Christopher Paolini')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',18,'Dan Brown')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',19,'Africa')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',19,'Asia')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',19,'Europe')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',19,'South America')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',20,'Eiffel tower')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',20,'Statue Of Liberty')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',20,'Taj Mahal')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',20,'Mount Rushmore')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',21,'Denmark')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',21,'Mexico')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',21,'Netherland')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',21,'United Kingdom')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',22,'Rice')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',22,'Pizza')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',22,'Quinoa')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',22,'Bread')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',23,'Pablo Picasso')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',23,'Bill Gates')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',23,'Steve Jobs')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',23,'Charles Babbage')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',24,'Sherlock Holmes')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',24,'Lolita')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',24,'Leopold Bloom')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',24,'Rabbit Angstrom')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',25,'Money')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',25,'Height')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',25,'Tree')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',25,'Rain')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',26,'Health Insurance')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',26,'Clothes')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',26,'Passport')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',26,'Vaccine against Rabies')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',27,'Hopscotch')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',27,'Rock, Paper, Scissors')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',27,'Telephone')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',27,'Marbles')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',28,'Tom Cruise')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',28,'Mr T')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',28,'Jerry Seinfeld')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',28,'George Washington')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',29,'Slam Dunk')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',29,'Touchdown')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',29,'Knockout')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',29,'Grand slam')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',30,'2')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',30,'3')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',30,'4')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',30,'5')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',31,'Milky')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',31,'Watery')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',31,'Berry')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',31,'Jello-shotty')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',32,'Eagles or Tigers')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',32,'Stars')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',32,'Pythons')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',32,'Bulls')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',33,'Health care')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',33,'Information Technology')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',33,'Human Resource')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',33,'Sports')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',34,'Tom and Jerry')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',34,'Yogi Bear and Boo Boo')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',34,'Itchy and Scratchy')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',34,'Road Runner and Wiley Coyote')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',35,'Linux computer operating system')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',35,'Mac operating system')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',35,'Kernel')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',35,'Ubuntu')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',36,'Tornados')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',36,'Hurricane')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',36,'Tsunami')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',36,'Earthquake')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',37,'Yellow')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',37,'White')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',37,'Red')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',37,'Blue')")

conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',38,'Venus')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',38,'Uranus')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',38,'Pluto')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',38,'Neptune')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',39,'MS DOS')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',39,'Windows 95')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',39,'Linux')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',39,'MVS')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('A',40,'Provide Evidence')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('B',40,'Find bugs')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('C',40,'Find Issues')")
conn.execute("Insert into Options(OptionID,QuestionID,Options_value) values ('D',40,'All the above options')")

conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (1,'A')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (2,'B')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (3,'A')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (4,'A')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (5,'A')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (6,'C')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (7,'A')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (8,'C')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (9,'C')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (10,'B')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (11,'D')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (12,'D')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (13,'D')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (14,'C')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (15,'C')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (16,'B')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (17,'C')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (18,'B')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (19,'A')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (20,'A')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (21,'A')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (22,'A')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (23,'A')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (24,'A')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (25,'A')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (26,'A')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (27,'C')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (28,'B')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (29,'D')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (30,'C')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (31,'C')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (32,'A')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (33,'A')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (34,'A')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (35,'A')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (36,'A')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (37,'A')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (38,'D')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (39,'C')")
conn.execute("Insert into Answers(QuestionID,CorrectOptionID) values (40,'D')")


conn.execute("insert into User (EmailAddress,CurrentGameLevel) values ('eg46shrsr@gmail.com','Entrylevel')")
conn.execute("insert into User (EmailAddress,CurrentGameLevel) values ('gxhxjyj@gmail.com','MidLevel')")
conn.execute("insert into User (EmailAddress,CurrentGameLevel) values ('seystuhsrtu@gmail.com','HighLevel')")

conn.commit()








