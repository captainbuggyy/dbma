CREATE DATABASE  IF NOT EXISTS `agriculture` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `agriculture`;
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`username`)
)
INSERT INTO `admin` VALUES ('satvat','satvat'),('sunil','sunil');

CREATE DATABASE  IF NOT EXISTS `agriculture` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `agriculture`;
DROP TABLE IF EXISTS `farmer`;
CREATE TABLE `farmer` (
  `farmer_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `contact` varchar(10) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `village` varchar(100) DEFAULT NULL,
  `approved` int DEFAULT NULL,
  `income` int DEFAULT NULL,
  PRIMARY KEY (`farmer_id`),
  CONSTRAINT `fk_farmer_user` FOREIGN KEY (`farmer_id`) REFERENCES `user` (`id`)
);
INSERT INTO `farmer` VALUES (41,'WOODIE SYMONS','9259683459','wsymons0@pagesperso-orange.fr','Roth','California','1 Corry Drive',1,NULL),(42,'ELFRIEDA ARSEY','2146910388','earsey1@bluehost.com','Center','Texas','73 Shelley Plaza',1,NULL),(43,'SAVINA PELLEW','9181565742','spellew2@about.com','Jenna','Oklahoma','56 Farragut Hill',1,NULL),(44,'SIBYLLE MCCOID','9717242635','smccoid3@infoseek.co.jp','Larry','Oregon','1685 David Drive',1,NULL),(45,'CECILIO BAWDON','9159169445','cbawdon4@hugedomains.com','Forest Dale','Texas','05 Gerald Avenue',1,NULL),(46,'HORTENSIA BRACE','4128034150','hbrace5@hc360.com','Mayer','Pennsylvania','636 Nevada Crossing',1,NULL),(47,'ANNE-CORINNE GOODSWEN','5628505616','agoodswen6@last.fm','Meadow Ridge','California','8730 Loftsgordon Road',1,NULL),(48,'LUCINDA CLINTON','2067962845','lclinton7@drupal.org','Sommers','Washington','7371 Russell Street',1,NULL),(49,'ASHLEE HUGUET','3153590400','ahuguet8@nasa.gov','Lakewood Gardens','New York','3 Waubesa Avenue',1,NULL),(50,'DONIA BRAMBLEY','9528130742','dbrambley9@intel.com','Sachtjen','Minnesota','12 Stephen Point',1,NULL),(51,'ATLANTA MATIJASEVIC','6513257601','amatijasevica@cbsnews.com','Susan','Minnesota','048 5th Circle',1,NULL),(52,'HILTON HAKEY','3122055212','hhakeyb@histats.com','Doe Crossing','Illinois','25383 Prentice Drive',1,NULL),(53,'CATHA GORVETTE','8121106374','cgorvettec@imdb.com','Shasta','Indiana','7 Golden Leaf Avenue',1,NULL),(54,'ELLYNN DANSER','7177515554','edanserd@sfgate.com','Stone Corner','Pennsylvania','67 Union Lane',1,NULL),(55,'SMITTY HUTCHEON','8475225174','shutcheone@blog.com','Pennsylvania','Illinois','14662 Gale Hill',1,NULL),(56,'EZECHIEL BEDDIS','2029266361','ebeddisf@vinaora.com','Glendale','District of Columbia','96 Glacier Hill Place',1,NULL),(57,'JEMIE COOMBE','2029059404','jcoombeg@cam.ac.uk','Quincy','District of Columbia','8283 Farwell Pass',1,NULL),(58,'ELIANORE BUBEAR','2544580187','ebubearh@cam.ac.uk','Swallow','Texas','167 Montana Alley',1,NULL),(59,'ZEB BASS','8069449598','zbassi@prnewswire.com','Waywood','Texas','88157 Kim Street',1,NULL),(60,'DINA BREW','7609041619','dbrewj@surveymonkey.com','Lyons','California','48 Buena Vista Avenue',1,NULL),(61,'MILDRID MCSHARRY','7701160390','mmcsharryk@drupal.org','Corben','Georgia','501 Bluejay Alley',1,NULL),(62,'CLAUDINA BENNETT','3367296520','cbennettl@vimeo.com','Milwaukee','North Carolina','61 Hauk Road',1,NULL),(63,'RUSSELL BRINKMAN','3077385757','rbrinkmanm@posterous.com','Buell','Wyoming','5 Spohn Place',1,NULL),(64,'ROSALEEN DREWE','8178392291','rdrewen@blogs.com','Heffernan','Texas','705 Nancy Lane',1,NULL),(65,'DOUGIE JEWETT','4323730623','djewetto@php.net','Manley','Texas','6256 Melvin Place',1,NULL),(66,'LUCIE FINGLETON','6191487906','lfingletonp@example.com','Schlimgen','California','23 Judy Junction',1,NULL),(67,'ARCH EILERT','5021561096','aeilertq@rambler.ru','Pond','Kentucky','465 Rigney Avenue',1,NULL),(68,'LOREEN TRICKER','7174598367','ltrickerr@msn.com','Hanson','Pennsylvania','30798 Pearson Crossing',1,NULL),(69,'PETERUS SWEETENHAM','2518476219','psweetenhams@about.com','Farwell','Alabama','69643 Kropf Avenue',1,NULL),(70,'MERRILEE ROUNSEFELL','2405628487','mrounsefellt@mac.com','Carey','Maryland','162 Redwing Crossing',1,NULL),(71,'RAMSEY CRICHTON','2096311589','rcrichtonu@buzzfeed.com','Lukken','California','7 Emmet Court',1,NULL),(72,'BATHSHEBA KERWEN','2609402678','bkerwenv@webs.com','Ridgeway','Indiana','5 Mccormick Point',1,NULL),(73,'MANDY DRINKALE','9042160385','mdrinkalew@topsy.com','Kenwood','Florida','160 Birchwood Trail',1,NULL),(74,'KRISTOFORO COLLET','6168414024','kcolletx@ifeng.com','Gale','Michigan','45664 Toban Court',1,NULL),(75,'SLADE EDELER','8163651752','sedelery@nymag.com','Dahle','Missouri','22484 Northview Way',1,NULL),(76,'TATIANIA STIBBS','6825473754','tstibbsz@newsvine.com','Huxley','Texas','336 Declaration Drive',1,NULL),(77,'LESLEY BLAKENEY','2065200140','lblakeney10@mit.edu','Katie','Washington','6 Waxwing Pass',1,NULL),(78,'WYNN FERNIER','3189596630','wfernier11@xing.com','North','Louisiana','4 Columbus Park',1,NULL),(79,'LORIANNE KENWORTH','7862909997','lkenworth12@tmall.com','Maywood','Florida','39 Graceland Road',1,NULL),(80,'LUCIO FIDIAN','4123873390','lfidian13@kickstarter.com','Division','Pennsylvania','22677 Bluestem Terrace',1,NULL),(81,'DENE DRINKELD','4321875492','ddrinkeld14@nytimes.com','Jana','Texas','93 Superior Plaza',1,NULL),(82,'GLEDA RODENBURG','9044582235','grodenburg15@flickr.com','Mockingbird','Florida','46715 Sherman Alley',1,NULL),(83,'STAFFORD BARLTHROP','3361198078','sbarlthrop16@exblog.jp','Debra','North Carolina','05 Park Meadow Avenue',1,NULL),(84,'RING AXTON','9017370644','raxton17@sitemeter.com','Pankratz','Tennessee','82423 Cordelia Road',1,NULL),(85,'EMELINE SLIDDERS','3155864211','eslidders18@sohu.com','Thierer','New York','8784 Eastwood Street',1,NULL),(86,'BIRDIE CAMMOCK','2609525344','bcammock19@ca.gov','Amoth','Indiana','0146 Delaware Center',1,NULL),(87,'AURLIE BLEIER','3148321211','ableier1a@adobe.com','Center','Missouri','7 Hoard Alley',1,NULL),(88,'HELAINA DEAN','8051609884','hdean1b@geocities.com','Blaine','California','58 Tennyson Parkway',1,NULL),(89,'MARNI BOYDELL','3037529768','mboydell1c@google.ru','Rusk','Colorado','7462 Debs Drive',1,NULL),(90,'MARIJO GARRATT','9015039192','mgarratt1d@cpanel.net','Swallow','Tennessee','602 Westerfield Junction',1,NULL),(91,'JAKE BYNE','2253444088','jbyne1e@dell.com','Bartelt','Louisiana','0876 5th Alley',1,NULL),(92,'ANGE KRUGMANN','3604574058','akrugmann1f@tripod.com','Acker','Washington','0 Pine View Road',1,NULL),(93,'CINDELYN STEMP','5052256323','cstemp1g@answers.com','Pine View','New Mexico','723 Debs Circle',1,NULL),(94,'REUBEN GEDDIS','5132421850','rgeddis1h@wikipedia.org','Monica','Ohio','74 Doe Crossing Avenue',1,NULL),(95,'HIRSCH GILLIARD','9164950548','hgilliard1i@va.gov','Mendota','California','446 Old Shore Avenue',1,NULL),(96,'HAILY VANNOORT','3375617646','hvannoort1j@nbcnews.com','Summerview','Louisiana','105 Lunder Way',1,NULL),(97,'ARDISJ DANAT','8161037890','adanat1k@usatoday.com','Cottonwood','Missouri','08498 Loftsgordon Point',1,NULL),(98,'PALM PIDWELL','9079666641','ppidwell1l@issuu.com','Chinook','Alaska','3 Fulton Circle',1,NULL),(99,'PATSY LANON','5596110101','planon1m@cloudflare.com','Muir','California','632 Morning Avenue',1,NULL),(100,'MAVRA MACDUNLEVY','9727725893','mmacdunlevy1n@angelfire.com','Packers','Texas','197 Dennis Court',1,NULL),(101,'ROSEMARIA DEY','5628334115','rdey1o@instagram.com','Sunbrook','California','23 Towne Court',1,NULL),(102,'ARLINA ECOB','5043186919','aecob1p@timesonline.co.uk','Muir','Louisiana','0695 Knutson Junction',1,NULL),(141,'Amol','886867508','s@gmail.com','Bangalore','Karnataka','Village2',NULL,NULL),(142,'sunil','9927837972','sunil@gmailas.com','Mysore','Maharashtra','Village3',NULL,NULL),(143,'Mohan','877937884','abc@gmail.com','Mysore','Karnataka','Village3',NULL,NULL),(144,'punit','3783846','punit@gmail.com','Bangalore','Maharashtra','Village4',NULL,NULL),(146,'sudhanshu12','2979872487','Sudhanshu@gmail.com','Bangalore','Karnataka','Village4',NULL,NULL);
CREATE DATABASE  IF NOT EXISTS `agriculture` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `agriculture`;

DROP TABLE IF EXISTS `farmer_notification`;
CREATE TABLE `farmer_notification` (
  `notification_id` int NOT NULL AUTO_INCREMENT,
  `farmer_id` int DEFAULT NULL,
  `reason` text,
  PRIMARY KEY (`notification_id`)
);
INSERT INTO `farmer_notification` VALUES (1,4,'your application for land is approved'),(2,4,'your application for land is approved'),(3,4,'Rejected Land Application:Document not uploaded properly'),(4,4,'your application for Pradhan Mantri Fasal Bima Yojana (PMFBY)is approved'),(5,4,'your application for Prime Minister Matsya Sampada Yojanais approved'),(6,4,'your application for Prime Minister Matsya Sampada Yojanais approved'),(7,4,'your application for Prime Minister Matsya Sampada Yojanais approved'),(8,5,'your application for land is approved'),(9,5,'your application for land is approved'),(10,5,'your application for land is approved'),(11,5,'your application for land is approved'),(12,5,'your application for Prime Minister Matsya Sampada Yojanais approved'),(13,6,'your application for land is approved'),(14,6,'your application for land is approved'),(15,6,'your application for land is approved'),(16,6,'your application for Prime Minister Matsya Sampada Yojanais approved'),(17,141,'your application for land is approved'),(18,141,'your application for land is approved'),(19,141,'your application for land is approved'),(20,141,'your application for Prime Minister Matsya Sampada Yojanais approved'),(21,146,'your application for land is approved'),(22,146,'your application for Prime Minister Matsya Sampada Yojanais approved'),(23,146,'your application for land is approved'),(24,146,'your application for Prime Minister Matsya Sampada Yojanais approved');
CREATE DATABASE  IF NOT EXISTS `agriculture` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `agriculture`;
DROP TABLE IF EXISTS `govt_schemes`;

CREATE TABLE `govt_schemes` (
  `scheme_id` int NOT NULL AUTO_INCREMENT,
  `criteria_area` tinytext,
  `income` tinytext,
  `benefits` text,
  `name` tinytext,
  PRIMARY KEY (`scheme_id`)
);
INSERT INTO `govt_schemes` VALUES (1,'Minimum 2 acres','Below 1 lakh','Under the PM-KISAN Scheme, farmers receive an annual financial assistance of Rs 6,000. This amount is sent to farmers\' accounts in three installments of Rs 2,000 each at intervals of four months. Currently, 15 installments have already been transferred to farmers\' accounts. If you haven\'t yet applied for this scheme, it is advisable to do so.','Prime Minister Matsya Sampada Yojana'),(2,'Minimum 10 acres','below 5 lakhs','Started in 2016, PMFBY has become the world\'s largest crop insurance scheme, with more than 5.5 crore farmers registering for crop insurance annually. It ensures claims of maximum benefits at minimum premiums and is an easy process for farmers to insure their crops against natural calamities like rainfall, temperature variations, hailstorms, and humidity.','Pradhan Mantri Fasal Bima Yojana (PMFBY)'),(3,'Anyone with agriculture land','Anyone','Any farmer involved in agriculture, fisheries, or animal husbandry can benefit from obtaining a Kisan Credit Card. Initiated in 1998, this scheme is run by various government and non-government banks across the country. It provides loans based on land cultivation and crop sowing for purchasing farm inputs like fertilizers, pesticides, machinery, and insecticides.','Kisan Credit Card Scheme'),(4,'No Criteria','No Criteria','Adequate irrigation is crucial for cash crops. If farmers don\'t move towards self-dependence on irrigation from traditional sources, it could negatively impact agricultural production. The aim of this centrally sponsored PMKSY started in 2015, is to ensure sufficient water availability for farming, expand irrigation in agriculture-compatible areas, improve water use efficiency, and promote continuous water conservation measures. Farmers installing drip irrigation systems under this scheme receive subsidie.',' Pradhan Mantri Krishi Sinchai Yojana (PMKSY)');

CREATE DATABASE  IF NOT EXISTS `agriculture` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `agriculture`;

DROP TABLE IF EXISTS `images`;
CREATE TABLE `images` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `image` blob,
  PRIMARY KEY (`id`)
);

CREATE DATABASE  IF NOT EXISTS `agriculture`;
USE `agriculture`;
DROP TABLE IF EXISTS `land`;
CREATE TABLE `land` (
  `farmer_id` int DEFAULT NULL,
  `land_id` int NOT NULL AUTO_INCREMENT,
  `survey_no` int DEFAULT NULL,
  `district` varchar(20) DEFAULT NULL,
  `soil_type` varchar(20) DEFAULT NULL,
  `land_area` decimal(10,2) DEFAULT NULL,
  `approved` tinytext,
  `file` longblob,
  PRIMARY KEY (`land_id`),
  KEY `fk_farmer` (`farmer_id`),
  CONSTRAINT `fk_farmer` FOREIGN KEY (`farmer_id`) REFERENCES `farmer` (`farmer_id`)
);

