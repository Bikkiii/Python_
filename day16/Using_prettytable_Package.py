from prettytable import PrettyTable

table=PrettyTable()             #creating object named table

table.add_column("Pokemon Name",["Piakchu","Squirtle","Charmender"])
table.add_column("Type",["Electric","Water","Fire"])

table.align="l"             
print(table)