# program built to see how using indexes can alter the
# cost of database updates and queries in terms of execution time
import random

# assigns one of four possible job titles to an employee
def selectJob(x):
    if x == 0:
        return "engineer" 
    elif x == 1:
        return "manager"
    elif x == 2:
        return "salesperson"
    elif x == 3:
        return "administrator"
    else:
        # to keep compiler happy
        return "engineer"
    
def main():
        # open a file to write to or create a new one if it doesn't exist
        file1 = open('hw11-data-10000.sql', 'w')
        file1.write("INSERT INTO Employee VALUES ")
        # write to file with 10,000 rows
        for i in range(10000):
            int (i)
            # assigns random salary values for each employee
            salary =  random.randint(12000, 150001)
            # assigns random job title for each employee
            x = random.randint(0, 4)
            job = selectJob(x)
            # performs insertion of random employee attribute values
            insert = "(" + str(i + 1) + ", " + str(salary) + ", '" + job + "')"
            if i + 1 == 10000:
                insert += ";"
            else:
                insert += ", "
            file1.write(insert)

        # close the file when finished 
        file1.close()

        # open a file to write to or create a new one if it doesn't exist
        file2 = open('hw11-data-100000.sql', 'w')
        file2.write("INSERT INTO Employee VALUES ")
        
        # write to file 100,000 rows
        for i in range(100000):
            int (i)
            # assigns random salary values for each employee
            salary =  random.randint(12000, 150001)
            # assigns random job title for each employee
            x = random.randint(0, 4)
            job = selectJob(x)
            # performs insertion of random employee attribute values
            insert = "(" + str(i + 1) + ", " + str(salary) + ", '" + job + "')"
            if i + 1 == 100000:
                insert += ";"
            else:
                insert += ", "
            file2.write(insert)

        # close the file when finished 
        file2.close()

        # open a file to write to or create a new one if it doesn't exist
        file3 = open('hw11-data-1000000.sql', 'w')
        file3.write("INSERT INTO Employee VALUES ")
        
        # write to file 1,000,000 rows
        for i in range(1000000):
            int (i)
            # assigns random salary values for each employee
            salary =  random.randint(12000, 150001)
            # assigns random job title for each employee
            x = random.randint(0, 4)
            job = selectJob(x)
            # performs insertion of random employee attribute values
            insert = "(" + str(i + 1) + ", " + str(salary) + ", '" + job + "')"
            if i + 1 == 1000000:
                insert += ";"
            else:
                insert += ", "
            file3.write(insert)

        # close the file when finished 
        file3.close()
        
main()
