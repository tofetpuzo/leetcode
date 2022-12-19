CREATE DATABASE BloodBank;

USE BloodBank;

CREATE TABLE
    Doctor (
        doctor_id INTEGER AUTO_INCREMENT PRIMARY KEY,
        firstName VARCHAR(255) NOT NULL,
        lastName VARCHAR(255) NOT NULL,
        username VARCHAR(255) UNIQUE NOT NULL,
        pass_word VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT NOW(),
    );

CREATE TABLE
    Patient (
        patient_id INTEGER AUTO_INCREMENT PRIMARY KEY,
        firstName VARCHAR(255) NOT NULL,
        lastName VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE,
        phone_number VARCHAR(255) NOT NULL,
        username VARCHAR(255) UNIQUE NOT NULL,
        pass_word VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT NOW()
    );

CREATE TABLE
    Admin (
        admin_id INTEGER AUTO_INCREMENT PRIMARY KEY,
        admin_user VARCHAR(255) UNIQUE NOT NULL,
        pass_word VARCHAR(255) NOT NULL,
        date_created TIMESTAMP DEFAULT NOW(),
    );

CREATE TABLE
    ServiceCategory (
        cat_id INT AUTO_INCREMENT PRIMARY KEY,
        cat_name VARCHAR(255) NOT NULL,
    );

CREATE TABLE
    Services (
        service_id INT AUTO_INCREMENT PRIMARY KEY,
        service_name VARCHAR(255) NOT NULL,
        cat_id INT,
        FOREIGN KEY(cat_id) REFERENCES ServiceCategory(cat_id),
        service_price DOUBLE NOT NULL
        
    );

CREATE TABLE
    PatientLaboratoryServices (
        patient_service_id AUTO_INCREMENT PRIMARY KEY,
        patient_id INT NOT NULL,
        service_id INT NOT NULL,
        FOREIGN KEY(service_id) REFERENCES Services(service_id),
        FOREIGN KEY(patient_id) REFERENCES Patient(patient_id),
        created_at DATETIME DEFAULT() NOW
        
    );

CREATE TABLE
    DoctorServices (
        doctor_service_id AUTO_INCREMENT PRIMARY KEY,
        doctor_id INT NOT NULL,
        service_id INT NOT NULL,
        FOREIGN KEY(service_id) REFERENCES Services(service_id),
        FOREIGN KEY(doctor_id) REFERENCES Doctor(doctor_id),
        created_at DATETIME DEFAULT() NOW
    );

/* laboratory services: urine , stool, drug testing
 radio : x-ray, ultrasound
 general: gynaecology, immunization
 table:1 1 urine , 2 stool, 3 x-ray, ultrasound, gynaecology, immunization
 */

