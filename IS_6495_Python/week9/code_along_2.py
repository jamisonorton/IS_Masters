# week 9 code along 2
import db_base as db
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


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
                next(csv_contents)
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

    def visualize_data(self):

        df = pd.read_sql_query("SELECT * FROM CollegeScoreCard", super().get_connection)
        print(df.head())
        print(df.info)

        print(df[df["state_abbr"] == "CA"]["act_med"])
        print(self.columns(df))
        states = df.groupby("state_abbr")
        print("MAX SAT = ", self.max_act(states))
        print(round(states.mean(numeric_only=True)["tuition"].min(), 2))
        print(round(states.mean(numeric_only=True)["tuition"].max(), 2))

        # using pandas for insights
        print("# of unique states", df["state_abbr"].nunique())
        print(df.corr(numeric_only=True))
        states = df.groupby("state_abbr")
        print("MAX SAT = ", self.max_act(states))
        print(round(states.mean(numeric_only=True)["tuition"].min(), 2))
        print(round(states.mean(numeric_only=True)["tuition"].max(), 2))
        print("Mean tuition rate", round(df["tuition"].mean(numeric_only=True), 2))
        print("Mean SAT_Score rate", round(df["sat_avg"].mean(numeric_only=True), 2))

        # using seaborn
        sns.displot(df["tuition"])
        plt.show()

        sns.heatmap(df.corr(numeric_only=True), cmap="coolwarm")
        plt.show()

    def max_act(self, series):
        return series["sat_avg"].max()

    def columns(self, series):
        return series.columns


csv_lab = CsvLab("CollegeScoreCardDB.sqlite")
# csv_lab.read_college_data("week9/CollegeScoreCard_Exercise.csv")
# csv_lab.save_to_database()
csv_lab.visualize_data()
