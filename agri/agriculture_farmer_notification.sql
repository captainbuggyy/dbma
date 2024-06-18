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
-- Table structure for table `farmer_notification`
--

DROP TABLE IF EXISTS `farmer_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farmer_notification` (
  `notification_id` int NOT NULL AUTO_INCREMENT,
  `farmer_id` int DEFAULT NULL,
  `reason` text,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farmer_notification`
--

LOCK TABLES `farmer_notification` WRITE;
/*!40000 ALTER TABLE `farmer_notification` DISABLE KEYS */;
INSERT INTO `farmer_notification` VALUES (1,4,'your application for land is approved'),(2,4,'your application for land is approved'),(3,4,'Rejected Land Application:Document not uploaded properly'),(4,4,'your application for Pradhan Mantri Fasal Bima Yojana (PMFBY)is approved'),(5,4,'your application for Prime Minister Matsya Sampada Yojanais approved'),(6,4,'your application for Prime Minister Matsya Sampada Yojanais approved'),(7,4,'your application for Prime Minister Matsya Sampada Yojanais approved'),(8,5,'your application for land is approved'),(9,5,'your application for land is approved'),(10,5,'your application for land is approved'),(11,5,'your application for land is approved'),(12,5,'your application for Prime Minister Matsya Sampada Yojanais approved'),(13,6,'your application for land is approved'),(14,6,'your application for land is approved'),(15,6,'your application for land is approved'),(16,6,'your application for Prime Minister Matsya Sampada Yojanais approved');
/*!40000 ALTER TABLE `farmer_notification` ENABLE KEYS */;
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