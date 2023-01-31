DROP TABLE IF EXISTS `db_blind_master`.`tbl_relatives`;
CREATE TABLE `db_blind_master`.`tbl_relatives` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `relation` varchar(45) NOT NULL,
  `mobile` varchar(45) NOT NULL,
   PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;