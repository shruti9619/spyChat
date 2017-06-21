from spy_details import spy, Spy, ChatMessage, friends_list
from steganography.steganography import Steganography
from termcolor import colored


#SPECIAL strings for alert generation
SPECIALMSG = ['SOS','HELP','SAVE ME','SAVE US','HELP ME','SAVE OUR SOUL','FACE OFF','COVER BLOWN']

STATUS_MSGS = ['Make hey while the sun shines', 'Burning desire is something you want as bad as air',
                   'Houston! we have a problem!']


#method definition to add a status or choose from the previous ones

def add_status_message():

    updated_status_msg = None

    if spy.current_status_message != None:

        print colored('Your status: %s \n' % spy.current_status_message,'green','on_grey')
    else:
        print colored('Status misses you feed one in! \n','green','on_grey')

    default = raw_input(colored("Choose from the older status (y/n)? ",'green','on_grey'))

    if default.upper() == "N":
        new_status_msg = raw_input(colored("New status please",'green','on_grey'))

        if len(new_status_msg)>0:
            STATUS_MSGS.append(new_status_msg)
            updated_status_msg = new_status_msg

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MSGS:
            print colored('%d. %s' % (item_position, message),'green','on_grey')
            item_position = item_position + 1

        msg_choice = int(raw_input(colored("\nChoose from the above messages ",'green','on_grey')))


        if len(STATUS_MSGS) >= msg_choice:
            updated_status_msg = STATUS_MSGS[msg_choice - 1]

    else:
        print colored('Invalid choice! Be smarter spy. Press either y or n.','red')

    if updated_status_msg:
        print colored('Current status: %s' % updated_status_msg,'green','on_grey')
    else:
        print colored('You current don\'t have a status update','green','on_grey')

    return updated_status_msg


########################################################################################################################

#method to add a friend
def add_friend():

    new_friend = Spy('', '', 0, 0.0)

    new_friend.name = raw_input(colored("Your friend's name: ",'green','on_grey'))
    new_friend.salutation = raw_input(colored("Friend's Mr. or Ms.?: ",'green','on_grey'))

#commented this line because it was making the salutation print twice
    # new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input(colored("Age?",'green','on_grey'))

    try:
        new_friend.age = int(new_friend.age)
    except:
        print colored("The age has to be numerical Spy! Be smart next time! \n Bye!", 'red')
        return -1

    new_friend.rating = raw_input(colored("Spy rating?",'green','on_grey'))

    try:
        new_friend.rating = float(new_friend.rating)
    except:
        print colored("The rating has to be numerical Spy! Be smart next time! \n Bye!",'red')
        return -1


    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends_list.append(new_friend)
        print colored('New Friend Added!','green','on_grey')
    else:
        print colored( 'Sorry! Check the details you\'ve entered again','red')

    return len(friends_list)

########################################################################################################################

def select_a_friend():
    item_num = 0

    friend_choice_pos=-1
    if len(friends_list) != 0:
        for friend in friends_list:
            print colored('%d. %s %s aged %d with rating %.2f is online' % (item_num +1, friend.salutation, friend.name,
                                                       friend.age,
                                                       friend.rating),'green','on_grey')
            item_num = item_num + 1

        frnd_choice = raw_input(colored("Choose from your friends",'green','on_grey'))

        friend_choice_pos = int(frnd_choice) - 1
        if friend_choice_pos < 0 or friend_choice_pos > len(friends_list)-1:
            print colored("The choice doesn't exist Spy! Be smart!",'red')
            friend_choice_pos=select_a_friend()
    else:
        addfrnd = raw_input( colored("Add a friend first (y/n)!",'green','on_grey'))
        if addfrnd.upper()=='Y':
            add_friend()
            friend_choice_pos=select_a_friend()
        else:
            print colored( "No friends found!",'red')
            exit(0)
    return friend_choice_pos


#######################################################################################################################

def send_message():

    friend_choice = select_a_friend()

    original_img = raw_input(colored("Name of the image in which secret messsage is to be encoded:",'green','on_grey'))

    output_path = "secretspycat.jpg"
    text = raw_input(colored("Your secret message:",'green','on_grey'))
    try:
        Steganography.encode(original_img, output_path, text)
    except:
        print colored("ENCODING UNSUCCESSFUL! MISSION ABORT \n!",'red')
        return

    new_chat = ChatMessage(text,True)

    friends_list[friend_choice].chats.append(new_chat)

    print colored( "Your secret is safe spy!",'green','on_grey')

#######################################################################################################################

#method selects a friend from the list and the file to decode the message from
def read_message():

    sender = select_a_friend()

    output_path = raw_input(colored("Secret file name:",'green','on_grey'))

    try:
        secret_msg = Steganography.decode(output_path)
    except:
        print colored('Wrong Image! No message encoded','red')
        return

    new_chat = ChatMessage(secret_msg,False)

    friends_list[sender].chats.append(new_chat)

    print colored("Your secret message " + secret_msg,'blue')

    #generate spy alert when special msg is encountered
    if secret_msg.upper() in SPECIALMSG:
        print colored("SPY ALERT! SPY ALERT! SPECIAL MESSAGE GENERATED: "+secret_msg,'green','on_grey')


    #trash him if he speaks more than hundred [words] not letters man!
    if(len(secret_msg.split(" "))) > 100:
        print colored("Spy friend" +friends_list[sender].name+" spoke too much. His profile will now be terminated!",'red')
        del friends_list[sender]

#######################################################################################################################

#method to read friends status
def read_friend_status():
    friendchoice=select_a_friend()
    print colored( friends_list[friendchoice].current_status_message,'green','on_grey')

#######################################################################################################################

#method to read all friends
def read_friends():
    item_num = 0

    if len(friends_list) != 0:
        for friend in friends_list:
            print colored('%d. %s %s aged %d with rating %.2f is online' % (item_num + 1, friend.salutation, friend.name,
                                                                    friend.age,
                                                                    friend.rating),'green','on_grey')
            item_num = item_num + 1
    else:
        addfrnd = raw_input(colored("No Friend found! Add a friend first (y/n)!",'red'))
        if addfrnd.upper() == 'Y':
            add_friend()
        else:
            print colored("No friends found!",'red')

#######################################################################################################################

#method to read chat history
def read_old_msg():
    frnd_choice=select_a_friend()

    print '\n'
    if len(friends_list[frnd_choice].chats) == 0:
        print 'No previous chats exist.'
    else:
        for chat in friends_list[frnd_choice].chats:
#datetime will be printed in black in both the cases hence outside
            print '[%s]' % (chat.time.strftime("%d %B %Y %H:%M"))
            if chat.is_sent_by_me:
                print colored("%s %s" %('You:', chat.message),'red','on_cyan',attrs=['bold','dark'])
            else:
                print colored('%s: %s' % (friends_list[frnd_choice].name,
                                                    chat.message),'blue','on_yellow',attrs=['bold','dark'])

#######################################################################################################################

#method to remove a friend from the list
def remove_friend():
    frnd_pos=select_a_friend()
    del friends_list[frnd_pos]
    return len(friends_list)


#######################################################################################################################

#initiates the menu display and activities for the passed object spy
def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name


    if spy.age > 12 and spy.age < 50:


        print colored( "Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard",'green','on_grey')

        show_menu = True



#show menu will become false when the user selects something that doesnt match any option
        while show_menu:
            menu = "Your Spy tools  \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message " \
                   "\n 4. Read a secret message \n 5. Read Chats from a user \n 6. List all the friends \n "\
                   "7. Remove Friend \n 8. Close Application \n"
            menu_choice = raw_input(colored(menu,'green','on_grey'))

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status_message()
                elif menu_choice == 2:
                    num_of_frnds = add_friend()
                    if num_of_frnds != -1:
                        print 'You have %d friends' % (num_of_frnds)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_old_msg()
                elif menu_choice == 6:
                    read_friends()
                elif menu_choice == 7:
                    remove_friend()
                else:
                    print colored('Pleasure to assist a world class Spy.','green','on_grey')
                    show_menu = False
    else:
        print colored( 'Sorry you are not of the correct age to be a spy','red')



#######################################################################################################################
#######################################################################################################################
#the program starts here



#print colored("Greetings! Biometrics Please",'green','on_grey')

ques = "Continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
ans = raw_input(colored(ques,'green','on_grey'))

#if user wants to continue with the same old name set by default
if ans.upper() == "Y":
    start_chat(spy)

#if user wants to create a new identity
else:

    spy = Spy('', '', 0, 0.00)

#getting various inputs from user as per the class spy
    spy.name = raw_input(colored("SpyChat welcomes you, your spy name please: ",'green','on_grey'))

    if len(spy.name) > 0:
        spy.salutation = raw_input(colored("Great! Mr. or Ms.?: ",'green','on_grey'))

        spy.age = raw_input(colored("Your age please?",'green','on_grey'))


        try:
            spy.age = int(spy.age)
        except:
            print colored("The age has to be numerical Spy! Be smart next time! \n Bye!",'red')
            exit(0)

        spy.rating = raw_input(colored("Your genuine spy rating?",'green','on_grey'))


        try:
            spy.rating = float(spy.rating)
        except:
            print colored("The rating has to be numerical Spy! Be smart next time! \n Bye!",'red')
            exit(0)

        start_chat(spy)
    else:
        print colored("The rating has to be numerical Spy! Be smart next time! \n Bye!",'red')
        exit(0)


