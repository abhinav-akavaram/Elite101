# Elite101 - Prework

def is_valid_num(str, lower_bound_num, upper_bound_num):
  try:
    num = int(str)
  except ValueError:
    return False
  if num >= lower_bound_num and num <= upper_bound_num:
    return True
  return False


def question_screen(question_answer):
  print("\n-----------------------------------------------------------------------------\n")
  print(question_answer[0], "\n")
  print(question_answer[1], "\n")
  while True:
    print("Options: ")
    choice = input("1. Back\n2. Quit\nPlease enter a number: ")
    if (is_valid_num(choice, 1, 2)):
        choice = int(choice)
    else:
      print("invalid input, try again.")
      continue
    if choice == 1:
      return True
    else:
      return False
  

def frequently_asked_questions():
  faqs = [("1. Where can I cancel my flight?","Look for a 'Manage My Flight' section on our website. The 'Cancel my Flight' option can beaccessed by clicking the dropdown arrow next to this section."), ("2. Where can I request a refund for my ticket?","After going to the 'Manage My Flight' Section and clicking on the 'Cancel my Flight' option, a prompt will pop up on your screen with the request a refund option in the bottom right hand corner of the pop up."), ("3. How do I check the status of my baggage claim?","After clicking the dropdown arrow next to the 'Manage My Flight' Section on our website, one of the subsequent options is 'Baggage claim'. Click on that option to check your baggage claim status."), ("4. Where do I reset my account password?", "In the top right hand corner of our website home page, click on the cog icon next to the Profile picture icon. In the settings page, scroll down to the 'Account settings' option and click on it. The 'Change my password' option will show up at the bottom of the page, above the option 'Delete account'."), ("5. I need help with the website, where can I get technical support?", "On the website home page, scroll all the way down until you completely see the dark blue box at the bottom of the page. Click on the 'Technical Support' option under the 'Help' section to either contact a customer service agent or to talk to another chatbot like me.")]
  total_questions = 5
  while True:
    print("\n-----------------------------------------------------------------------------")
    print("Frequently Asked Questions\n")
    for faq in faqs:
      print(faq[0])
    print("{}. Back".format(total_questions + 1))
    print("{}. Quit".format(total_questions + 2))
    choice = input("Please enter  number: ")
    if (is_valid_num(choice, 1, total_questions + 2)):
      choice = int(choice)
    else:
      print("invalid input, try again.")
      continue
    if choice == total_questions + 1:
      return True
    elif choice == total_questions + 2:
      print("Please let us know if you have any other issues.")
      return False
    else:
      if (question_screen(faqs[choice - 1])):
        continue
      else:
        return False
  

def main_menu():
  while True:
    print("\n-----------------------------------------------------------------------------")
    print("Main Menu\n")
    choice = input("1. Frequently Asked Questions\n2. Contact service provider\n3. Quit\nPlease enter a number: ")
    if (is_valid_num(choice, 1, 3)):
      choice = int(choice)
    else:
      print("invalid input, try again.")
      continue
    if choice == 3:
      return False
    elif choice == 2:
      return True
    else:
      if (frequently_asked_questions()):
        continue
      else:
        return False


def init_main():
  print("Hi! how may I help you?")
  if (main_menu()):
    print("\n-----------------------------------------------------------------------------")
    print("Contacting next available customer service agent. Please wait...")
    print("Thank you for your patience, your customer service agent is ready.")
  else:
    print("\n-----------------------------------------------------------------------------")
    print("Thank you for using our services.")
    

if __name__ == "__main__":
  init_main()