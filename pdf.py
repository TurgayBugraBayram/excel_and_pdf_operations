import PyPDF2

file_path = "New Business Policy.pdf"

pdf_file = open(file_path, "rb")

pdf_reader = PyPDF2.PdfReader(pdf_file)

keyword_counts = {
    "PP 00 01 09 18": 0,
    "PP 02 97 09 18": 0,
    "PP 03 71 09 18": 0,
    "PP 04 93 01 19": 0,
    "PP 13 01 09 18": 0,
    "PP 33 31 09 18": 0,
    "PP 33 68 09 18": 0,
    "IL CW 0001 04 21": 0,
    "UI IL 01 04 21": 0,
    "UI IL 03 07 18": 0,
    "UI PP 03 04 21": 0,
    "UI PP 05 07 11": 0
}

# her bir sayfada
#
# for page_num in range(len(pdf_reader.pages)):
#     page_text = pdf_reader.pages[page_num].extract_text()
#     for keyword in keyword_counts:
#         keyword_counts[keyword] += page_text.count(keyword)
#
# pdf_file.close()
# print(keyword_counts)

# geçerli sayfada

page_num = 4

if page_num < len(pdf_reader.pages):
    page_text = pdf_reader.pages[page_num].extract_text()
    for keyword in keyword_counts:
        keyword_counts[keyword] += page_text.count(keyword)

pdf_file.close()

for keyword, counts in keyword_counts.items():
    print(keyword, counts)
