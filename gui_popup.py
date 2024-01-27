#!/usr/bin/env python3
#Kaleb Nails
from tkinter import *
import json
import subprocess
import os
import sys
root = Tk()  # create parent window
#Set the geometry
root.geometry("750x280")
root.title("MOVEUAS_WIZARD.exe")

#screen -dm bash -c "./OPC_Simple_v2.py;exec sh"


#This will actually run the sensors based on the json given
def run_sensors(sensor_ports):
    #subprocess.run("pkill screen", shell=True,text=True)


    bash_script_content = '#!/bin/bash\n\n'

    # Loop through each sensor device
    for i, device in enumerate(sensor_ports['alphasense'], start=0):
        # Set the variable for each sensor
        variable_name = f'alpha{i}_device'
        device_port = sensor_ports['alphasense'][i]
        bash_script_content += f'{variable_name}="{device_port}"\n'

        # Start the logger for each sensor
        bash_script_content += f'echo "Starting alpha{i} logger"\n'
        bash_script_content += f'screen -dm -S alpha{i} python3 OPC_Simple_v2.py ${variable_name}\n\n'
        #print(bash_script_content)




    # Loop through each sensor device
    for i, device in enumerate(sensor_ports['sensirion'], start=0):
        # Set the variable for each sensor
        variable_name = f'sensirion{i}_device'
        device_port = sensor_ports['sensirion'][i]
        bash_script_content += f'{variable_name}="{device_port}"\n'

        # Start the logger for each sensor
        bash_script_content += f'echo "Starting sensirion{i} logger"\n'
        bash_script_content += f'screen -dm -S sensirion{i} python3 SPS30_Sensirion_Run.py ${variable_name}\n\n'
        #print(bash_script_content)


        # Loop through each sensor device
        for i, device in enumerate(sensor_ports['PMS'], start=0):
            # Set the variable for each sensor
            variable_name = f'PMS{i}_device'
            device_port = sensor_ports['PMS'][i]
            bash_script_content += f'{variable_name}="{device_port}"\n'

            # Start the logger for each sensor
            bash_script_content += f'echo "Starting PMS{i} logger"\n'
            bash_script_content += f'screen -dm -S PMS{i} python3 pm25_simpletest.py ${variable_name}\n\n'



        print(bash_script_content)

    # Write the Bash script to a file
    with open('Sensor_Start_Script.sh', 'w') as bash_script_file:
        bash_script_file.write(bash_script_content)

    # Make the Bash script executable
    subprocess.run(['chmod', '+x', 'Sensor_Start_Script.sh'])


#    for i in sensor_ports['alphasense']:
#        print(i)
#        try:
#            command = "sleep 15;./Alphasense/OPC_Simple_v2.py" +" " + i + ";exec sh"
            #p3 = subprocess.run(["sudo", "screen", "-dm",  "./OPC_Simple_v2.py"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT) # you can also put stderr to stdout
            #p3 = subprocess.run(["screen", "-dm","bash","-c" , "sleep 15;./Alphasense/OPC_Simple_v2.py;exec sh"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT) # you can also put stderr to stdout

#            p3 = subprocess.run(["screen", "-dm","bash","-c" , command], stdout=subprocess.PIPE, stderr=subprocess.STDOUT) # you can also put stderr to stdout





#            print('----')
#            print('p3 = {}'.format(p3))
#            print('----')

#        except subprocess.CalledProcessError as err:
#            print( "\n\ncaught an rsync() subprocess error: {0}".format(err) )
#            print( "exiting.")
#            sys.exit(-1)

#        print('p.stdout = {}'.format(p3.stdout.decode('utf-8')))

        #print(command)

        # Expand the tilde (~) to the full home directory path
        #home_directory = os.path.expanduser('~')

        # Specify the relative path from the home directory
        #relative_path = 'Sensor_Code/Alphasense'

        # Combine the home directory and the relative path
        #full_path = os.path.join(home_directory, relative_path)

        #subprocess.call(['/bin/bash', '-x', 'ls'])

        # Now, you can use the full path as the current working directory
        #subprocess.run(['lxterminal', '-e', 'python3', '-c', "print('hiiiiii')"], cwd=full_path, shell=False)
                #subprocess.run(["lxterminal","-e","cd" "Sensor_Code","cd" "Alphasense","sudo","python3","print('hi')"])


        #subprocess.call(["lxterminal","-e","sudo","nano","/boot/config.txt"])
        #subprocess.call(["lxterminal","-e","bash","sleep","10","cd" "Sensor_Code","cd" "Alphasense"])
        #subprocess.run(["lxterminal", "-e", "bash", "-c", "cd Sensor_Code/Alphasense && sudo python3 -c 'print(\"hi\")'"])




        #This opens a new screen
        #open_screen_command = f"screen -dmS alphasense{i.replace('/', '_')}"
        ##open_screen_command = f"screen -S alphasense{i.replace('/', '_')}"

        #print( "OPEN_SCREEN_COMMAND: " + open_screen_command)
        #subprocess.call(f"screen -dmS alphasense{i.replace('/', '_')}",shell=True)

        #subprocess.call(f"screen -dmS alphasense{i.replace('/', '_')}", shell=True)
        #subprocess.call(f"screen -S alphasense{i.replace('/', '_')} -X stuff 'echo test_hello\\15'", shell=True)
        #subprocess.call(f"screen -S alphasense{i.replace('/', '_')} -X stuff 'ls'$(echo -ne '\015')", shell=True)

        #subprocess.call(f"screen -S alphasense{i.replace('/', '_')} -X stuff 'python3 OPC_Simple_v2.py'$(echo -ne '\015')", shell=True)
        #subprocess.run(f"screen -S alphasense_{i.replace('/', '_')} -X stuff 'python3 OPC_Simple_v2.py > /path/to/output.log 2>&1'", shell=True)



        #run_code_command = f"screen -r alphasense{i.replace('/', '_')}"
        #subprocess.run(f"screen -r alphasense{i.replace('/', '_')}", shell=True,text=True)
        #subprocess.run("echo 'hello'", shell=True,text=True)

        #subprocess.run(f"screen -d", shell=True,text=True)




        #run_code_command = f"screen -r alphasense{i.replace('/', '_')} -X stuff 'python3 OPC_Simple_v2.py'$(echo -ne '\\015')"

        #subprocess.run("echo 'Hello World'")

        #subprocess.run("chmod +x OPC_Simple_v2.py.py")
        #subprocess.run(run_code_command, shell=True,text=True)
        #subprocess.run("echo 'Hello World'")












        #This gives the relative and full path for the subprocess.call() later on
        #relative_path = 'Sensor_Code/Alphasense'
        #full_path = os.path.join(home_directory, relative_path)

        #subprocess.call(['lxterminal' , '-e', 'python3', command], cwd=full_path, shell = False)









#THIS IS THE YES OPTION
def retrieve_old_data():

    shown_text.config(text="USING OLD CONFIGURATION")

    #Open the Json file
    with open ('sensors_UART_configs.json','r') as file:
        sensor_ports = json.load(file)

    print( sensor_ports)

    run_sensors(sensor_ports)





    #FIGURE OUT WHAT THE HECK I AM DOING
    #turn_on.config(text= "NO LONGER YES")

#THIS IS THE NO OPTION
def setup_tty():
    turn_off.config(text="QUIT",command=root.quit)
    shown_text.config(text="UNPLUG ALL SENSORS, when done hit next")


    print("HELLO")

# use Button and Label widgets to create a simple TV remote
turn_on = Button(root, text="YES",command = retrieve_old_data)
#turn_on.pack(side=BOTTOM)

turn_off = Button(root, text="NO", command=setup_tty)

INITIALIZING_TEXT_PROMPT = "HELLO, welcome to the MOVEUAS program."
INITIALIZING_TEXT_PROMPT += " Would you like to use previous sensor USB port setups?"
INITIALIZING_TEXT_PROMPT += " (If this is your first time setting up hit NO)"

shown_text = Label(root, text=INITIALIZING_TEXT_PROMPT, wraplength=300, justify=LEFT)
shown_text.grid(column=1,row=0)


turn_on.grid(column=0,row=1,sticky='se')
turn_off.grid(column=2,row=1,sticky='sw')
root.grid_columnconfigure(1,weight=1)
root.grid_rowconfigure(1,weight=1)




root.mainloop()


    #turn_on.config(text= "NO LONGER YES")
#
# def ask_question(question):
#     root = tk.Tk()
#
#    root.withdraw()
#
#     answer = simpledialog.askstring("Question", question)
#
#     root.destroy()
#
#     return answer
#
# if __name__ == "__main__":
#     questions = [
#         "Question 1: What is your name?",
#         "Question 2: Where are you from?",
#         "Question 3: What is your favorite color?",
#         "Question 4: What is your age?",
#         "Question 5: What is your hobby?"
#     ]
#
#     answers = []
#     for question in questions:
#         answer = ask_question(question)
#         answers.append(answer)
#
#     print("Answers:")
#     for i, answer in enumerate(answers):
#         print(f"Question {i + 1}: {answer}")
