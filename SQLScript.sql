-- MySQL Script generated by MySQL Workbench
-- Fri Oct 23 19:09:25 2015
-- Model: New Model    Version: 2.0
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Character`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Character` (
  `idCharacter` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`idCharacter`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Credentials`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Credentials` (
  `idCredentials` INT NOT NULL,
  `username` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  PRIMARY KEY (`idCredentials`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Player`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Player` (
  `idisPlaying` INT NOT NULL,
  `Credentials_idCredentials` INT NOT NULL,
  PRIMARY KEY (`idisPlaying`, `Credentials_idCredentials`),
  INDEX `fk_Player_Credentials1_idx` (`Credentials_idCredentials` ASC),
  CONSTRAINT `fk_Player_Credentials1`
    FOREIGN KEY (`Credentials_idCredentials`)
    REFERENCES `mydb`.`Credentials` (`idCredentials`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`isPlaying`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`isPlaying` (
  `idIsPlaying` INT NOT NULL,
  `lastPosition` VARCHAR(45) NULL,
  `Character_idCharacter` INT NOT NULL,
  `Player_idisPlaying` INT NOT NULL,
  PRIMARY KEY (`idIsPlaying`, `Character_idCharacter`, `Player_idisPlaying`),
  INDEX `fk_isPlaying_Character1_idx` (`Character_idCharacter` ASC),
  INDEX `fk_isPlaying_Player1_idx` (`Player_idisPlaying` ASC),
  CONSTRAINT `fk_isPlaying_Character1`
    FOREIGN KEY (`Character_idCharacter`)
    REFERENCES `mydb`.`Character` (`idCharacter`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_isPlaying_Player1`
    FOREIGN KEY (`Player_idisPlaying`)
    REFERENCES `mydb`.`Player` (`idisPlaying`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
