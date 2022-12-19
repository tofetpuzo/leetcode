-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 03, 2022 at 11:32 PM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bloodbank`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
CREATE TABLE IF NOT EXISTS `admin` (
  `admin_id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_user` varchar(255) NOT NULL,
  `pass_word` varchar(255) NOT NULL,
  `date_created` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`admin_id`),
  UNIQUE KEY `admin_user` (`admin_user`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `admin_user`, `pass_word`, `date_created`) VALUES
(1, 'bolajoko', 'Malomo', '2022-11-03 21:34:04');

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
CREATE TABLE IF NOT EXISTS `doctor` (
  `doctor_id` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(255) NOT NULL,
  `lastName` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `pass_word` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`doctor_id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`doctor_id`, `firstName`, `lastName`, `username`, `pass_word`, `created_at`) VALUES
(1, 'bis', 'Ali', 'bisiali', 'mario', '2022-11-03 21:40:13'),
(2, 'kehinde', 'ajisafe', 'kenny', 'kehinde', '2022-11-03 21:40:13'),
(3, 'jennifer', 'alo', 'alojeny', 'jenny', '2022-11-03 21:41:14'),
(4, 'fola', 'shade', 'folashade', 'fola', '2022-11-03 21:41:14'),
(5, 'akeem', 'abass', 'abassakem', 'abass', '2022-11-03 21:41:49');

-- --------------------------------------------------------

--
-- Table structure for table `doctorservices`
--

DROP TABLE IF EXISTS `doctorservices`;
CREATE TABLE IF NOT EXISTS `doctorservices` (
  `doctor_service_id` int(11) NOT NULL AUTO_INCREMENT,
  `doctor_id` int(11) NOT NULL,
  `service_id` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`doctor_service_id`),
  KEY `doctor_id` (`doctor_id`),
  KEY `service_id` (`service_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctorservices`
--

INSERT INTO `doctorservices` (`doctor_service_id`, `doctor_id`, `service_id`, `created_at`) VALUES
(2, 1, 2, '2022-11-03 23:21:06');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
CREATE TABLE IF NOT EXISTS `patient` (
  `patient_id` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(255) NOT NULL,
  `lastName` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone_number` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `pass_word` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`patient_id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`patient_id`, `firstName`, `lastName`, `email`, `phone_number`, `username`, `pass_word`, `created_at`) VALUES
(1, 'lolade', 'tinubu', 'tofet@gmail.com', '09023404932', 'lola', 'bisi', '2022-11-03 23:20:29');

-- --------------------------------------------------------

--
-- Table structure for table `patientlaboratoryservices`
--

DROP TABLE IF EXISTS `patientlaboratoryservices`;
CREATE TABLE IF NOT EXISTS `patientlaboratoryservices` (
  `patient_service_id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_id` int(11) NOT NULL,
  `service_id` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`patient_service_id`),
  KEY `patient_id` (`patient_id`),
  KEY `service_id` (`service_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patientlaboratoryservices`
--

INSERT INTO `patientlaboratoryservices` (`patient_service_id`, `patient_id`, `service_id`, `created_at`) VALUES
(1, 1, 2, '2022-11-03 23:20:43');

-- --------------------------------------------------------

--
-- Table structure for table `servicecategory`
--

DROP TABLE IF EXISTS `servicecategory`;
CREATE TABLE IF NOT EXISTS `servicecategory` (
  `cat_id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_name` varchar(255) NOT NULL,
  PRIMARY KEY (`cat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `servicecategory`
--

INSERT INTO `servicecategory` (`cat_id`, `cat_name`) VALUES
(1, 'Laboratory'),
(2, 'Radiology'),
(3, 'GeneralServices');

-- --------------------------------------------------------

--
-- Table structure for table `services`
--

DROP TABLE IF EXISTS `services`;
CREATE TABLE IF NOT EXISTS `services` (
  `service_id` int(11) NOT NULL AUTO_INCREMENT,
  `service_name` varchar(255) NOT NULL,
  `cat_id` int(11) DEFAULT NULL,
  `service_price` double NOT NULL,
  PRIMARY KEY (`service_id`),
  KEY `cat_id` (`cat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `services`
--

INSERT INTO `services` (`service_id`, `service_name`, `cat_id`, `service_price`) VALUES
(2, 'urine test', 1, 10000);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `doctorservices`
--
ALTER TABLE `doctorservices`
  ADD CONSTRAINT `doctorservices_ibfk_1` FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`doctor_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `doctorservices_ibfk_2` FOREIGN KEY (`service_id`) REFERENCES `services` (`service_id`) ON UPDATE CASCADE;

--
-- Constraints for table `patientlaboratoryservices`
--
ALTER TABLE `patientlaboratoryservices`
  ADD CONSTRAINT `patientlaboratoryservices_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`patient_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `patientlaboratoryservices_ibfk_2` FOREIGN KEY (`service_id`) REFERENCES `services` (`service_id`) ON UPDATE CASCADE;

--
-- Constraints for table `services`
--
ALTER TABLE `services`
  ADD CONSTRAINT `services_ibfk_1` FOREIGN KEY (`cat_id`) REFERENCES `servicecategory` (`cat_id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
