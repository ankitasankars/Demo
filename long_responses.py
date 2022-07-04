import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_KNOW = "I am not interested in knowing anyone named Devesh"
R_BEAUTIFUL = "I did put more effort into my hair algorithm this morning, thanks for noticing!"
R_HOBBIES = "Does talking to you count?"
R_URL1 = "(1) https://www.ibm.com/cloud/learn/machine-learning" \
         " (2) https://www.expert.ai/blog/machine-learning-definition/"
R_URL2 = "https://www.oracle.com/chatbots/what-is-a-chatbot/"
R_URL3 = "(1) https://www.coursera.org/learn/machine-learning#syllabus" \
         " (2) https://auth.udacity.com/sign-in?next=https%3A%2F%2Fclassroom.udacity.com%2Fauthenticated" \
         " (3) https://www.udacity.com/course/machine-learning--ud262" \
         " (4) https://www.udacity.com/course/intro-to-tensorflow-for-deep-learning--ud187"
R_URL4 = "(1) https://www.python.org/doc/essays/blurb/" \
         " (2) https://www.w3schools.com/python/python_intro.asp" \
         " (3) https://opensource.com/resources/python" \
         " (4) https://www.pythontutorial.net/getting-started/what-is-python/" \
         " (5) https://www.techtarget.com/whatis/definition/Python"
R_URL5 = "https://en.wikipedia.org/wiki/Data_science"
R_URL6 = "https://en.wikipedia.org/wiki/Data_science#Etymology"
R_URL7 = "https://www.docker.com/"
R_URL8 = "https://www.docker.com/get-started/"
R_URL9 = "https://www.docker.com/community/"
R_URL10 = "https://www.docker.com/community/open-source/"
R_URL11 = "https://www.docker.com/community/get-involved/developer-preview/"

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response