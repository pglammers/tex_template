from pytex_merge import read_merged_file

file = read_merged_file(".", "main_merged.tex")
file_extracted_list = file.string_extracted_files_list()

for fname, fcontents in file_extracted_list:
    text_file = open(fname, "w")
    n = text_file.write(fcontents)
    text_file.close()
