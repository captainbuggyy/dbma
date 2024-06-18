CREATE DATABASE  IF NOT EXISTS `agriculture` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `agriculture`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: agriculture
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `govt_schemes`
--

DROP TABLE IF EXISTS `govt_schemes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `govt_schemes` (
  `scheme_id` int NOT NULL AUTO_INCREMENT,
  `criteria_area` tinytext,
  `income` tinytext,
  `benefits` text,
  `name` tinytext,
  PRIMARY KEY (`scheme_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `govt_schemes`
--

LOCK TABLES `govt_schemes` WRITE;
/*!40000 ALTER TABLE `govt_schemes` DISABLE KEYS */;
INSERT INTO `govt_schemes` VALUES (1,'Minimum 2 acres','Below 1 lakh','Under the PM-KISAN Scheme, farmers receive an annual financial assistance of Rs 6,000. This amount is sent to farmers\' accounts in three installments of Rs 2,000 each at intervals of four months. Currently, 15 installments have already been transferred to farmers\' accounts. If you haven\'t yet applied for this scheme, it is advisable to do so.','Prime Minister Matsya Sampada Yojana'),(2,'Minimum 10 acres','below 5 lakhs','Started in 2016, PMFBY has become the world\'s largest crop insurance scheme, with more than 5.5 crore farmers registering for crop insurance annually. It ensures claims of maximum benefits at minimum premiums and is an easy process for farmers to insure their crops against natural calamities like rainfall, temperature variations, hailstorms, and humidity.','Pradhan Mantri Fasal Bima Yojana (PMFBY)'),(3,'Anyone with agriculture land','Anyone','Any farmer involved in agriculture, fisheries, or animal husbandry can benefit from obtaining a Kisan Credit Card. Initiated in 1998, this scheme is run by various government and non-government banks across the country. It provides loans based on land cultivation and crop sowing for purchasing farm inputs like fertilizers, pesticides, machinery, and insecticides.','Kisan Credit Card Scheme'),(4,'No Criteria','No Criteria','Adequate irrigation is crucial for cash crops. If farmers don\'t move towards self-dependence on irrigation from traditional sources, it could negatively impact agricultural production. The aim of this centrally sponsored PMKSY started in 2015, is to ensure sufficient water availability for farming, expand irrigation in agriculture-compatible areas, improve water use efficiency, and promote continuous water conservation measures. Farmers installing drip irrigation systems under this scheme receive subsidie.',' Pradhan Mantri Krishi Sinchai Yojana (PMKSY)');
/*!40000 ALTER TABLE `govt_schemes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-19  0:06:44
