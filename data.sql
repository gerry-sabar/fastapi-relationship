CREATE TABLE IF NOT EXISTS `todos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(150) CHARACTER SET utf8 NOT NULL,
  `status` enum('Doing','Finished') DEFAULT 'Doing',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 NOT NULL,
  `email` varchar(255) CHARACTER SET utf8 NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE todos
-- add NULL for educational purpose so if the database has record
-- no need to do more step to modify existing record in todo
ADD COLUMN user_id int NULL after id; 

ALTER TABLE todos             
ADD CONSTRAINT fk_user_todo -- Name of the foreign key constraint
FOREIGN KEY (user_id)       -- Column in the 'todo' table
REFERENCES users(id)    	  -- Referenced column in the 'user' table
ON DELETE CASCADE           -- Delete todos if the user is deleted
ON UPDATE CASCADE;          -- Update user_id in todos if it changes in 'user'