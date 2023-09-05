# PASSWORD-MANAGER

Usage
1. Install MariaDB
  -In sql console write:
  -`CREATE USER 'passwdDB'@localhost IDENTIFIED BY 'qwerty'`
  -`GRANT ALL PRIVILEGES ON *.* TO 'passwdDB'@localhost IDENTIFIED BY 'qwerty'`

2. Navigate to the project directory

3. `python dbmanager.py make`

4. `python main.py add -s <name> -u <url> -e<email> -l <username>`

5. `python main.py extract` to get all entries

6. `python main.py extract -s/-u/-e/-l <entry> --copy` to automatically copy entry to clipboard