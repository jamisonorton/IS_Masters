import db_base as db
import csv


class Veggies:
    def __init__(self, row):
        self.name = row[0]
        self.common_color = row[1]
        self.peal = row[2]
        self.type = row[3]


class VeggieIce1(db.DBbase):
    def reset_or_create_db(self):
        try:
            sql = """
                DROP TABLE IF EXISTS Veggies;

                CREATE TABLE Veggies (
                    name TEXT,
                    common_color varchar(15),
                    peal varchar(25),
                    type varchar(25)
                );
            """
            super().execute_script(sql)
        except Exception as e:
            print(e)

    def read_veggies_data(self, file_name):
        self.veggies_list = []

        try:
            with open(file_name, "r") as record:
                csv_contents = csv.reader(record)
                next(csv_contents)
                for row in csv_contents:
                    print(row)
                    veggies = Veggies(row)
                    self.veggies_list.append(veggies)

        except Exception as e:
            print(e)

    def save_to_database(self):
        print("Number of record to save:", len(self.veggies_list))
        save = input("Continue? ").lower()

        if save == "y":
            for item in self.veggies_list:
                try:
                    super().get_cursor.execute(
                        """INSERT INTO Veggies
                        (name, common_color, peal, type)
                        VALUES(?, ?, ?, ?)""",
                        (
                            item.name,
                            item.common_color,
                            item.peal,
                            item.type,
                        ),
                    )
                    print("Saved item:", item.name, item.type)

                except Exception as e:
                    print(e)

            super().get_connection.commit()

        else:
            print("Save to DB aborted")


veggie_lab = VeggieIce1("VeggiesDB.sqlite")
# veggie_lab.reset_or_create_db()
veggie_lab.read_veggies_data("week9/veggies.csv")
veggie_lab.save_to_database()
