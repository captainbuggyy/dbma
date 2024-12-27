CREATE DATABASE  IF NOT EXISTS `agriculture`;
USE `agriculture`;
DROP TABLE IF EXISTS `farmer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farmer` (
  `farmer_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `contact` varchar(10) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `district` varchar(20) DEFAULT NULL,
  `state` varchar(20) DEFAULT NULL,
  `village` varchar(20) DEFAULT NULL,
  `approved` int DEFAULT NULL,
  `income` int DEFAULT NULL,
  PRIMARY KEY (`farmer_id`),
  CONSTRAINT `fk_farmer_user` FOREIGN KEY (`farmer_id`) REFERENCES `user` (`id`)
)

INSERT INTO `farmer` VALUES (4,'SATVAT SAGAR','9541746008','satvatsharma@gmail.com','Bangalore','Karnataka','Village4',NULL,NULL),(5,'sunil','933989894','sunil@gmail.com','Bangalore','Karnataka','Village3',NULL,NULL),(6,'Sudhanshu','998398920','Sudhanshu@gmail.com','Mysore','Maharashtra','Village4',NULL,NULL);

