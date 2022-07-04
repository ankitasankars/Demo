import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello! I am Jarvis.', ['hello', 'hi', 'hey', 'sup', 'heyo','heya','namaskar','hola','heylo'], single_response=True)
    response('See you! Hope you have a great day!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('That makes me happy to know!', ['good', 'amazing', 'great'], required_words=['i','feel'])
    response('Oh, better times will come for sure', ['sad','feel','sick'], required_words=['i','feel'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'coding'], required_words=['coding'])
    response('Talking to you..', ['what', 'are', 'you','doing','wassup'], required_words=['what', 'doing'])
    response('Sure, what is it?', ['can', 'help', 'you', 'me'], required_words=['help', 'can'])
    response('Right back at ya! <3 ', ['loved', 'talking'], required_words=['loved', 'talking'])

    # Longer responses
    response(long.R_URL11, ['docker', 'developer'], required_words=['docker', 'developer'])
    response(long.R_URL10, ['docker', 'open', 'link', 'source'], required_words=['docker', 'source'])
    response(long.R_URL9, ['docker', 'community', 'link'], required_words=['docker', 'community'])
    response(long.R_URL8, ['docker', 'how', 'get', 'started'], required_words=['docker', 'started'])
    response(long.R_URL7, ['docker', 'website', 'link'], required_words=['docker', 'link'])
    response(long.R_URL6, ['etymology', 'wikipedia', 'list', 'some'], required_words=['etymology', 'list'])
    response(long.R_URL5, ['wikipedia', 'link', 'data', 'science'], required_words=['wikipedia', 'data'])
    response(long.R_URL4, ['links', 'python', 'some', 'info'], required_words=['python', 'links'])
    response(long.R_URL3, ['courses', 'links', 'ml', 'some'], required_words=['courses', 'links'])
    response(long.R_URL1, ['could','you','ml', 'send', 'link', 'for','machine', 'learning'], required_words=['machine','learning'])
    response(long.R_URL2, ['chatbots','link','could'], required_words=['chatbots','link'])
    response(long.R_HOBBIES, ['what', 'are', 'your', 'hobbies'], required_words=['your', 'hobbies'])
    response(long.R_BEAUTIFUL, ['you', 'look', 'beautiful', 'pretty'], required_words=['you', 'beautiful'])
    response(long.R_KNOW, ['know', 'devesh'], required_words=['devesh'])
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# Testing the response system
while True:
    print('JARVIS: ' + get_response(input('YOU: ')))