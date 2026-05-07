from pytex_merge import read_extracted_file

file = read_extracted_file(".", "main.tex")
file_merged = file.string_merged_outer()

text_file = open("main_merged.tex", "w")
n = text_file.write(file_merged)
text_file.close()

print(file_merged)
