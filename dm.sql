/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - dm
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`dm` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `dm`;

/*Table structure for table `employee` */

DROP TABLE IF EXISTS `employee`;

CREATE TABLE `employee` (
  `employee_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(20) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL,
  `designation` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4;

/*Data for the table `employee` */

insert  into `employee`(`employee_id`,`login_id`,`first_name`,`last_name`,`place`,`phone`,`email`,`qualification`,`designation`) values (21,24,'Maggy','rose','kochi','7992880964','maggyros@gmail.com','BCA','manager'),(23,26,'Maggy','Rose','Kakkanad','84161697441','maggyrose561@gmail.c','BCA','manager'),(24,27,'Dona','Dixon','YWCA Shenoys','8412557896','donadixon5@gmail.co','BCA','CEO'),(26,29,'Sruti','Xavier','pachalam','7859462153','sruti@gmail.com','BCA','Manager'),(27,30,'sss','ssss','ssss','7859462153','sruti@gmail.com','BBc','Manager');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `employee_id` int(11) DEFAULT NULL,
  `feedback` varchar(100) DEFAULT NULL,
  `fb_date` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`employee_id`,`feedback`,`fb_date`) values (1,21,'It is very nice.','10/12/2019'),(2,22,'I love it!','09/12/21'),(3,23,'It meant the world to me..','05/12/2021'),(4,24,'It is wonderful','08/12/2021'),(5,21,'hi everyone','2022-02-01');

/*Table structure for table `files` */

DROP TABLE IF EXISTS `files`;

CREATE TABLE `files` (
  `file_id` int(11) NOT NULL AUTO_INCREMENT,
  `employee_id` int(11) DEFAULT NULL,
  `filename` varchar(20) DEFAULT NULL,
  `file_type` varchar(20) DEFAULT NULL,
  `date` varchar(10) DEFAULT NULL,
  `file` varchar(5000) DEFAULT NULL,
  `key` varchar(5000) DEFAULT NULL,
  `encval` varchar(5000) DEFAULT NULL,
  PRIMARY KEY (`file_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4;

/*Data for the table `files` */

insert  into `files`(`file_id`,`employee_id`,`filename`,`file_type`,`date`,`file`,`key`,`encval`) values (4,27,'gsgs','Type1','2022-02-16',NULL,NULL,NULL),(5,27,'ysys','Type1','2022-02-16',NULL,NULL,NULL),(6,27,'','Type1','2022-02-16','','',NULL),(7,27,'rgehj','Type2','2022-02-16','static/uploads/0a8d2ebf-8694-4a16-b56f-5a713ec6bbbd.jpg','ss',NULL),(8,27,'','Type2','2022-02-16','static/uploads/420fa052-12c1-4c2f-a0df-5f484733242b.jpg','<_RSAobj @0x22475a2a320 n(1024),e>',NULL),(9,27,'hdhd','Type2','2022-02-16','static/uploads/c5e55e38-58e2-44f1-bc39-2f9ec53b048b.jpg','<_RSAobj @0x28997288e10 n(1024),e,d,p,q,u,private>',NULL),(10,27,'ggtb','Type2','2022-02-16','static/uploads/1cdeabf6-98eb-4bf2-84ad-0b6be417f278.txt','<_RSAobj @0x21a4a059c18 n(1024),e,d,p,q,u,private>',NULL),(11,27,'','Type2','2022-02-16','static/uploads/9c967fa5-4ccc-450e-b47c-2c3a4842f89b.jpg','<_RSAobj @0x295492105f8 n(1024),e,d,p,q,u,private>',NULL),(12,27,'yuuy\n','Type2','2022-02-16','static/uploads/47d683c3-f5ec-493c-83cd-bcfb7a15372b.jpg','static/key/4cc719f9-0bca-479f-b9ea-b5c3266dc332.jpg',NULL),(13,27,'uhu','Type2','2022-02-16','static/uploads/ec5ee450-dd31-4ff3-aee9-b13e8ccdc1f3.jpg','<_RSAobj @0x21f069d9eb8 n(1024),e,d,p,q,u,private>',NULL),(14,27,'ddepp pu','Type2','2022-02-16','static/uploads/eecc354a-0449-4c7d-ab7c-5ea96f8cc6fb.jpg','static/key/eecc354a-0449-4c7d-ab7c-5ea96f8cc6fb.jpg',NULL),(15,27,'hdhdh','Type2','2022-02-16','static/uploads/ce15fa9f-5f97-4be6-ae91-7a747879f736.jpg','static/key/ce15fa9f-5f97-4be6-ae91-7a747879f736.jpg',NULL),(16,27,'ddd','Type2','2022-02-16','static/uploads/0998057a-7302-433a-a70b-a4e264f7919a.jpg','static/key/d2bb196b-40e4-4f68-adfb-531ce207890b.txt',NULL),(17,21,'','Type2','2022-02-18','static/uploads/40220af6-3beb-4503-b626-aba3cb13ac90.jpg','static/key/5e69ef08-a37f-4bef-85e6-1aab8039c6ef.txt',NULL),(18,21,'rosemaggy','Type1','2022-02-18','static/uploads/e725aeab-d00d-4101-b184-17afab3596a6abc.jpg','',NULL),(19,21,'det','Type1','2022-02-18','static/uploads/7fcbdf92-5555-48c5-ac28-4d389ed66bc7abc.jpg','',NULL),(20,27,'hju','Type2','2022-02-18','static/uploads/8dfeba2f-fe3e-4bcc-83da-aed3bfe1578c.jpg','static/keys/7e4f551e-9c9a-4980-8f47-244834301c7f.txt','static/encmsg/7e4f551e-9c9a-4980-8f47-244834301c7f.txt'),(21,27,'hsus','Type2','2022-02-18','static/uploads/f3ce1732-09c4-4df9-bf0b-0e21cb721c73.jpg','static/keys/356a5927-1fd2-4147-8b88-14fdf6f7da1b.txt','static/encmsg/356a5927-1fd2-4147-8b88-14fdf6f7da1b.txt'),(22,27,'ddddd','Type3','2022-02-18','static/uploads/a8ac662d-f086-4b25-979c-2f4492f91ac7.jpg','static/keys/835e82fe-ae7b-405d-a908-9b7164dd75e5.txt','static/encmsg/835e82fe-ae7b-405d-a908-9b7164dd75e5.txt'),(23,27,'ddddd','Type3','2022-02-18','static/uploads/affd4bfe-878d-4b27-95e3-7e940ecf364c.jpg','static/keys/3f1aaa75-7bb2-4aa9-a949-27ef2f00d708.txt','static/encmsg/3f1aaa75-7bb2-4aa9-a949-27ef2f00d708.txt'),(24,27,'ddddd','Type3','2022-02-18','static/uploads/2285a505-565a-4d4f-9c8f-cbca561f899d.jpg','static/keys/cf1c680f-77d6-4f73-86d4-318993006494.txt','static/encmsg/cf1c680f-77d6-4f73-86d4-318993006494.txt');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `usertype` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(24,'Maggy561','123456','employee'),(26,'manaal5','456789','employee'),(27,'sruti45','','employee'),(29,'Srtiii','asdfg','employee'),(30,'ss','ss','employee');

/*Table structure for table `transfer` */

DROP TABLE IF EXISTS `transfer`;

CREATE TABLE `transfer` (
  `transfer_id` int(11) NOT NULL AUTO_INCREMENT,
  `employee_id` int(11) DEFAULT NULL,
  `file_id` int(11) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`transfer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `transfer` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
