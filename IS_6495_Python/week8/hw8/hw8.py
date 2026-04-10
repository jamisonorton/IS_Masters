import DBbase as db

class Parts(db.DBbase):
    
    def __init__(self):
        super(Parts, self).__init__("week8/hw8/InventoryDB.sqlite")

    def update(self, parts_id, name):
        try:
            super().get_cursor.execute("update Parts set name = ? where id = ?;", (name, parts_id))
            super().get_connection.commit()
            print(f"Updated record to {name} successfully.")
        except Exception as ex:
            print("An error occurred.", ex)

    def add(self, name):
        try:
            super().get_cursor.execute("insert or ignore into Parts (name) values(?);", (name,))
            super().get_connection.commit()
            print(f"Added {name} successfully.")
        except Exception as ex:
            print("An error occurred.", ex)

    def delete(self, parts_id):
        try:
            super().get_cursor.execute("DELETE FROM Parts where id = ?;", (parts_id,))
            super().get_connection.commit()
            print(f"Deleted part ID: {parts_id} successfully.")
            return True
        except Exception as ex:
            print("An error occurred.", ex)
            return False

    def fetch(self, id=None, part_name=None):
        # if Id is null (or None), then get everything, else get by id
        try:
            if id is not None:
                return super().get_cursor.execute("SELECT * FROM Parts WHERE id = ?", (id,)).fetchone()
            elif part_name is not None:
                return super().get_cursor.execute("SELECT * FROM Parts WHERE name = ?", (part_name,)).fetchone()
            else:
                return super().get_cursor.execute("SELECT * FROM Parts").fetchall()
        except Exception as ex:
            print("An error occurred.", ex)

    def reset_database(self):
        try:
            sql = """
                DROP TABLE IF EXISTS Parts;
                
                CREATE TABLE Parts (
                    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    name    TEXT UNIQUE );
                    
                
            
            
            """
            super().execute_script(sql)
        except Exception as ex:
            print("An error occurred.", ex)
        finally:
            super().close_db()
            

class Inventory(Parts):
    
    def add_inv(self, name, qty, price):
        try:
            super().add(name)
        except Exception as ex:
            print("An error occurred in the Parts class.", ex)
        else:
            try:
                part_id = super().fetch(part_name=name)[0]
                if part_id is not None:
                    super().get_cursor.execute("""INSERT INTO Inventory (part_id, quantity, price)
                        VALUES(?,?,?);""", (part_id, qty, price))
                    super().get_connection.commit()
                    print(f"Inventory {name} added successfully.")
                else:
                    raise Exception("The id of the part name was not found")
            except Exception as e:
                print("An error occurred in the Inventory class", e)
        
    def update_inv(self, id, qty, price):
        try:
            super().get_cursor.execute("""UPDATE Inventory SET quantity = ?, price = ? where id = ?;""", (qty, price, id))
            super().get_connection.commit()
            print("Updated inventory record successfully.")
            return True
        except Exception as ex:
            print("An error occurred.", ex)
            return False
            
    def delete_inv(self, inventory_id):
        try:
            part_id = self.fetch_inv(inventory_id)[1]
            if part_id is not None:
                rsts = super().delete(part_id)
                super().get_connection.commit()
                
                if rsts is False:
                    raise Exception("Delete method in parts failed. Delete aborted.")
                
        except Exception as ex:
            print("An error occurred.", ex)
        
        else:
            try:
                super().get_cursor.execute("""DELETE FROM Inventory WHERE id = ?;""", (inventory_id,))
                super().get_connection.commit()
            except Exception as e:
                print("An error occurred in Inventory delete.", e)
            
    def fetch_inv(self, id=None):
        try:
            if id is not None:
                retval = super().get_cursor.execute("""SELECT Inventory.id, part_id, p.name, quantity, 
                                                    price FROM Inventory JOIN Parts p on Inventory.part_id = p.id 
                                                    WHERE Inventory.id = ?;""",(id,)).fetchone()
                return retval
            else:
                return super().get_cursor.execute("""SELECT Inventory.id, part_id, p.name, quantity, 
                                                price FROM Inventory JOIN Parts p on Inventory.part_id = p.id;""").fetchall()
        except Exception as ex:
            print("An error occurred.", ex)
            
    def reset_database(self):
        try:
            sql = """
                DROP TABLE IF EXISTS Inventory;
            
                CREATE TABLE Inventory (
                    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    part_id    INTEGER NOT NULL,
                    quantity    INTEGER NOT NULL,
                    price       varchar(20)
                );
            """
            super().execute_script(sql)
            print("Inventory table successfully created.")
        except Exception as ex:
            print("An error occurred.", ex)
        finally:
            super().close_db()
            
class Project:
    
    def run(self):
        
        inv_options = { "get": "Get all inventory", 
                        "getby": "Get inventory by ID", 
                        "update": "Update inventory", 
                        "add": "Add inventory", 
                        "delete": "Delete inventory",
                        "reset": "Reset database",
                        "exit": "exit program"
                        }
        print("Welcome to my inventory program, Please choose a selection.")
        user_selection = ""
        while user_selection != "exit":
            print("*** Option List ***")
            for option in inv_options.items():
                print(option)
                
            user_selection = input("Select an option: ").lower()
            inventory = Inventory()
            
            if user_selection == "get":
                results = inventory.fetch_inv()
                for item in results:
                    print(item)
                    
            elif user_selection == "getby":
                
                inv_id = input("Enter Inventory ID: ")
                results = inventory.fetch_inv(inv_id)
                print(results)
                input("press return to continue: ")
                
            elif user_selection == "update":
                results = inventory.fetch_inv()
                for item in results:
                    print(item)
                inv_id = input("Enter Inventory ID: ")
                qty = input("Enter quantity amount: ")
                price = input("Enter a price: ")
                inventory.update_inv(inv_id, qty, price)
                print(inventory.fetch_inv(inv_id))
                input("press return to continue: ")
                
            elif user_selection == "add":
                name = input("Enter part name: ")
                qty = input("Enter quantity amount: ")
                price = input("Enter a price: ")
                inventory.add_inv(name, qty, price)
                print("Done\n")
                input("press return to continue: ")
                
            elif user_selection == "delete":
                inv_id = input("Enter Inventory ID: ")
                inventory.delete_inv(inv_id)
                print("Done\n")
                input("press return to continue: ")
                
            elif user_selection == "reset":
                confirm = input("This will delete all records in parts and inventory. Do you still want to continue? (y/n): ").lower()
                if confirm == "y":
                    inventory.reset_database()
                    parts = Parts()
                    parts.reset_database()
                    print("Reset complete")
                    input("press return to continue: ")
                else:
                    print("Reset aborted.")
                    input("press return to continue: ")
                
            else:
                if user_selection != "exit":
                    print("Invalid selection. Please try again\n")
                    
project = Project()
project.run()