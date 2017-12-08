use cvillagomez_DB;
-- Contains employee information that will be used to
-- see how using indexes can alter the cost of database
-- updates and queries in terms of their alloted execution
-- time

-- drops any previously existing Employee table 
DROP TABLE IF EXISTS Employee;

-- Employee table
CREATE TABLE Employee(
	employee_id INT NOT NULL,
	salary INT NOT NULL,
	title VARCHAR(30) NOT NULL,
	PRIMARY KEY(employee_id),
	INDEX comb_idx (title, salary)
) ENGINE = InnoDB;