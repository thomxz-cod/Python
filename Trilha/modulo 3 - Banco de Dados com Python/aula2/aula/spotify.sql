-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema spotify
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema spotify
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `spotify` DEFAULT CHARACTER SET utf8 ;
USE `spotify` ;

-- -----------------------------------------------------
-- Table `spotify`.`artista`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`artista` (
  `id_artista` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `genero` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id_artista`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`album`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`album` (
  `id_album` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(45) NOT NULL,
  `ano_lancamento` INT NOT NULL,
  `id_artista` INT NULL,
  PRIMARY KEY (`id_album`),
  INDEX `fk_album_artista_idx` (`id_artista` ASC) VISIBLE,
  CONSTRAINT `fk_album_artista`
    FOREIGN KEY (`id_artista`)
    REFERENCES `spotify`.`artista` (`id_artista`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`musica`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`musica` (
  `id_musica` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `genero` VARCHAR(50) NOT NULL,
  `id_album` INT NULL,
  PRIMARY KEY (`id_musica`),
  INDEX `fk_musica_album1_idx` (`id_album` ASC) VISIBLE,
  CONSTRAINT `fk_musica_album1`
    FOREIGN KEY (`id_album`)
    REFERENCES `spotify`.`album` (`id_album`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`usuario` (
  `id_usuario` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id_usuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`playlist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`playlist` (
  `id_playlist` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `id_usuario` INT NULL,
  PRIMARY KEY (`id_playlist`),
  INDEX `fk_playlist_usuario1_idx` (`id_usuario` ASC) VISIBLE,
  CONSTRAINT `fk_playlist_usuario1`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `spotify`.`usuario` (`id_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`musica_playlist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`musica_playlist` (
  `id_musica` INT NULL,
  `id_playlist` INT NULL,
  INDEX `fk_musica_playlist_playlist1_idx` (`id_playlist` ASC) VISIBLE,
  INDEX `fk_musica_playlist_musica1_idx` (`id_musica` ASC) VISIBLE,
  CONSTRAINT `fk_musica_playlist_playlist1`
    FOREIGN KEY (`id_playlist`)
    REFERENCES `spotify`.`playlist` (`id_playlist`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_musica_playlist_musica1`
    FOREIGN KEY (`id_musica`)
    REFERENCES `spotify`.`musica` (`id_musica`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
