import os
import pandas as pd
import re
from datetime import datetime

class Main():
    def __init__(self) -> None:
        # our dataframes with key as the date and the value as the dataframe
        self.dataframes = {}
        # aggregate dataframe of unique unexpected outages 
        self.column_names = [
            "Resource Name",
            "Resource Unit Code",
            "Fuel Type",
            "Outage Type",
            "Available MW Maximum",
            "Available MW During Outage",
            "Effective MW Reduction Due to Outage",
            "Actual Outage Start",
            "Nature Of Work"
            ]
        self.aggregate_dataframes = pd.DataFrame(columns=self.column_names)


    def load_data(self):
        # Get the current working directory
        current_dir = os.getcwd()

        # Get the directory one level up (parent directory)
        parent_dir = os.path.dirname(current_dir)

        directory_path = parent_dir + '/datasets/outages/'

        for filename in os.listdir(directory_path):
            if filename.endswith('.xlsx') or filename.endswith('.xls'):
                # Construct the full file path
                file_path = os.path.join(directory_path, filename)

                workbook_datetime = self.get_workbook_datetime(file_path)
                
                # Read the Excel file into a DataFrame
                df = pd.read_excel(file_path)
                df = pd.read_excel(file_path, [1], skiprows=4)
                if type(df.get(1) is pd.core.frame.DataFrame):
                    df = df.get(1)
                # Remove unecessary data
                df = df.dropna(subset=['Resource Unit Code'])

                # Append the DataFrame to the list
                self.dataframes[workbook_datetime] = df

        print("Quantity of DataFrames loaded: ", len(self.dataframes))

    def process_data(self, dataframe):
        for index, row in dataframe.iterrows():
            if ((row["Actual Outage Start"] > self.get_analytics_start_date()) and 
                (row["Actual Outage Start"] < self.get_analytics_end_date())):
                # we add the item to the df
                temp_dict = {}
                for index in self.column_names:
                    temp_dict[index] = row[index]
                new_row = temp_dict
                self.aggregate_dataframes = pd.concat([self.aggregate_dataframes, pd.DataFrame([new_row])], ignore_index=True)
            else:
                pass
    


    def get_workbook_datetime(self, file_path):

        df = pd.read_excel(file_path, [1], nrows=4)

        workbook_datetime_text = df[1].iloc[2, 0]
        pattern = r'[^:]+:(.+)'

        # Use re.search() to find the first instance of the pattern
        match = re.search(pattern, workbook_datetime_text)

        # Check if a match was found
        if match:
            result = match.group(1)
            result = result.strip()
            # Use strptime to parse the string into a datetime object
            datetime_obj = datetime.strptime(result, "%b %d, %Y %I:%M %p")
            return datetime_obj
        else:
            print("No match found.")


    def sort_dataframes(self):

        # Sort the dictionary by keys
        sorted_dict = dict(sorted(self.dataframes.items(), reverse=False))

        # Print the sorted dictionary
        print(sorted_dict)
        return sorted_dict


    def get_workbooks_info(self):
        print("Here are the dates of the workbooks in sorted order: \n", self.dataframes.keys())
        print("Here are the items of dictionary containing the workbooks in sorted order: \n", self.dataframes.items())
        with open('output.txt', 'w') as file:
            # Write data to the file
            file.write("Here are the dates of the workbooks in sorted order: \n")
            for index in self.dataframes.keys():
                file.write(str(index))
                file.write("\n")
            file.write("Here are the items of dictionary containing the workbooks in sorted order: \n")
            file.write(str(self.dataframes.items()))


    def get_analytics_start_date(self):
        str_date = "2022-12-01 00:00:00"
        datetime_obj = datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")
        return datetime_obj

    def get_analytics_end_date(self):
        str_date = "2023-08-31 23:59:00"
        datetime_obj = datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")
        return datetime_obj

    def write_aggregate_dataframe_info(self):
        print("Writing aggregate dataframe to text file")
        # Get the current working directory
        current_dir = os.getcwd()
        filename = "aggregate_dataframe.csv" 
        file_path = os.path.join(current_dir, filename)
        self.aggregate_dataframes.to_csv(file_path)



# start here
main = Main()
main.load_data()
dataframes = main.sort_dataframes()
# main.get_workbooks_info()
for dataframe_date, dataframe in dataframes.items():
    main.process_data(dataframe)
main.write_aggregate_dataframe_info()