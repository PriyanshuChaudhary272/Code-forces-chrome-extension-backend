from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
import sys
import json
import time
# import ast # abstract syntax tree
app = Flask(__name__)

@app.route("/")
def scrape_Codeforces_questions():
    # --- Scrape codeforces problem set page and store problem details in a 2D list ----

    html_text = requests.get('https://codeforces.com/problemset').text
    soup = BeautifulSoup(html_text, 'lxml')
    questions_table_html_list = soup.find_all('tr')
    number_of_questions = min(len(questions_table_html_list), 110);

    questions_names_and_topics_list = []

    # # FOR DEVELOPMENT PURPOSE
    for index in range(1, 4):
    # for index in range(1, number_of_questions-1):
        question_data_html = questions_table_html_list[index].find_all('td')[1]
        details_of_a_question_html_list = question_data_html.find_all('a')

        question_details_in_text_list = []

        for details_index, x in enumerate(details_of_a_question_html_list):
            if details_index == 0:
                question_details_in_text_list.append(x.text.strip())
                question_details_in_text_list.append('https://codeforces.com' + x['href'])
            else:
                question_details_in_text_list.append(x.text.strip())

        questions_names_and_topics_list.append(question_details_in_text_list)

    return(jsonify(questions_names_and_topics_list))
    # print(json.dumps(questions_names_and_topics_list))
    # sys.stdout.flush()


    # Dummy Data list
    # dummy_data = [['codeforces', 'https:'],['priyanshu', 'http']];
    # sys.argv :- This function returns a list of command line arguments passed to a Python script. The name of the script is always the item at index 0, and the rest of the arguments are stored at subsequent indices.
    # input = ast.literal_eval(sys.argv[1])
    # output = dummy_data
    # print(json.dumps(output));
    # sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)
    # scrape_Codeforces_questions()
    # time.sleep(4)












