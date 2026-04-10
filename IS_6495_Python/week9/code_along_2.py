# week 9 code along 2
import db_base as db
import csv


class CollegeScoreCard:

    def __init__(self, row):
        self.id = row[0]
        self.name = row[1]
        self.state = row[2]
        self.act = row[3]
        self.sat = row[4]
        self.enroll = row[5]
        self.tuition = row[6]
        self.postgrad = row[7]
        self.compl_rate = row[8]


class CsvLab(db.DBbase):

    def reset_or_create_db(self):

        try:
            sql = """
                DROP TABLE IF EXISTS CollegeScoreCard;
                
                CREATE TABLE CollegeScoreCard (
                    id INTEGER NOT NULL PRIMARY KEY UNIQUE,
                    name TEXT,
                    state_abbr varchar(2),
                    act_med INTEGER,
                    sat_avg INTEGER,
                    enrollment INTEGER,
                    tuition INTEGER,
                    postgrad_income_10yr INTEGER,
                    completion_rate REAL);
            """
            super().execute_script(sql)
        except Exception as e:
            print(e)

    def read_college_data(self, file_name):
        self.college_scores_list = []

        try:
            with open(file_name, "r") as record:
                csv_contents = csv.reader(record)
                next(record)
                for row in csv_contents:
                    # print(row)
                    college = CollegeScoreCard(row)
                    self.college_scores_list.append(college)

        except Exception as e:
            print(e)

    def save_to_database(self):
        print("Number of records to save: ", len(self.college_scores_list))
        save = input("Continue? ").lower()

        if save == "y":
            for item in self.college_scores_list:
                item.act = item.act.replace("NaN", "0")
                item.sat = item.sat.replace("NaN", "0")
                item.postgrad = item.postgrad.replace("NaN", "0")
                item.compl_rate = item.compl_rate.replace("NaN", "0")

                try:
                    super().get_cursor.execute(
                        """INSERT INTO CollegeScoreCard
                    (id, name, state_abbr, act_med, sat_avg, enrollment, tuition, postgrad_income_10yr, completion_rate)           
                        VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        (
                            item.id,
                            item.name,
                            item.state,
                            item.act,
                            item.sat,
                            item.enroll,
                            item.tuition,
                            item.postgrad,
                            item.compl_rate,
                        ),
                    )
                    super().get_connection.commit()

                    print("Saved item: ", item.id, item.name, item.state)
                except Exception as e:
                    print(e)

        else:
            print("Save to DB aborted")


csv_lab = CsvLab("CollegeScoreCardDB.sqlite")
csv_lab.read_college_data("week9/CollegeScoreCard_Exercise.csv")
csv_lab.save_to_database()
