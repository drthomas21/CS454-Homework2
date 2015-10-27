-- MySQL Script generated by MySQL Workbench
-- Mon Oct 26 23:53:13 2015
-- Model: New Model    Version: 1.0
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema panda
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `panda` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `panda` ;

-- -----------------------------------------------------
-- Table `panda`.`Character`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `panda`.`Character` (
  `idCharacter` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`idCharacter`),
  UNIQUE INDEX `idCharacter_UNIQUE` (`idCharacter` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `panda`.`Player`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `panda`.`Player` (
  `idPlayer` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  PRIMARY KEY (`idPlayer`),
  UNIQUE INDEX `idPlayer_UNIQUE` (`idPlayer` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `panda`.`isPlaying`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `panda`.`isPlaying` (
  `idIsPlaying` INT NOT NULL AUTO_INCREMENT,
  `lastPosition` VARCHAR(45) NULL,
  `Character_idCharacter` INT NOT NULL,
  `Player_idPlayer` INT NOT NULL,
  PRIMARY KEY (`idIsPlaying`, `Character_idCharacter`, `Player_idPlayer`),
  INDEX `fk_isPlaying_Character1_idx` (`Character_idCharacter` ASC),
  INDEX `fk_isPlaying_Player1_idx` (`Player_idPlayer` ASC),
  UNIQUE INDEX `idIsPlaying_UNIQUE` (`idIsPlaying` ASC),
  CONSTRAINT `fk_isPlaying_Character1`
    FOREIGN KEY (`Character_idCharacter`)
    REFERENCES `panda`.`Character` (`idCharacter`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_isPlaying_Player1`
    FOREIGN KEY (`Player_idPlayer`)
    REFERENCES `panda`.`Player` (`idPlayer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
