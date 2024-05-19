# 书目表
CREATE TABLE `testdb`.`book`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NULL COMMENT '书名',
  `author` varchar(255) NULL COMMENT '作者',
  `price` float(10, 2) NULL COMMENT '书名价格',
  `edition` int NULL COMMENT '版次',
  PRIMARY KEY (`id`)
);
