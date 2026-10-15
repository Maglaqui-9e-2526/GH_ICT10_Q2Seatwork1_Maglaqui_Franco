# Club Checker
from pyscript import display, document

def view_user(e):
    document.getElementById('result').innerHTML = ' '
    complete_name = ['Franco Maglaqui', 'Joel Gonzales', 'Ezekiel Bacay', 'Joseph Co', 'Chester Roxas']
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name
    member_checker = candidate.title in complete_name

    messages = (f'Sorry {candidate}, your name is not on the list.', f'Congratulations {candidate}! You are now part of the TLE club.')  # 0 and 1, True or False

    document.getElementById('result').innerHTML = messages[member_checker]
