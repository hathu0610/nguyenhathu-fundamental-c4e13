import pyexcel

a_list = [
    {
        "Name": 'Adam',
        "Age": 28

    },
    {
        "Name": 'Beatrice',
        "Age": 30
    }
]
pyexcel.save_as(records=a_list, dest_file_name="your_file.xlsx")