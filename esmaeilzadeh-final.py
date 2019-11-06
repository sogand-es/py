{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unindent does not match any outer indentation level (<tokenize>, line 79)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<tokenize>\"\u001b[1;36m, line \u001b[1;32m79\u001b[0m\n\u001b[1;33m    show_log()\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unindent does not match any outer indentation level\n"
     ]
    }
   ],
   "source": [
    "def print_menu():\n",
    "    print('1. Print Phone Numbers')\n",
    "    print('2. Add a Phone Number')\n",
    "    print('3. call')\n",
    "    print('4. show')\n",
    "    print('5. Quit')\n",
    "    print()\n",
    "###########################################################\n",
    "def call_to(name):\n",
    "    f = open(\"phonebook.txt\",\"r\")\n",
    "    for x in f:\n",
    "        index=x.find(':')\n",
    "        if x[:index] == name :\n",
    "            phone = x[index+1:-2]\n",
    "            callnumber(name,phone)\n",
    "    f.close        \n",
    "    \n",
    "    \n",
    "##################################\n",
    "def callnumber(name,phone):\n",
    "    import datetime\n",
    "    t1 = datetime.datetime.now()\n",
    "    print('Calling to ',phone)\n",
    "    print('For end call, press Enter')\n",
    "    input() \n",
    "    t2 = datetime.datetime.now()\n",
    "    t3 = 'Call Duration = '+ str(t2 - t1)[:7]\n",
    "    t1 = 'Call Time = '+ str(a)[:19]\n",
    "    f = open(\"call_log.txt\",\"t1\")\n",
    "    f.write(name),f.write(', '),f.write(phone),  f.write('\\n')\n",
    "    f.write(a),   f.write('\\n' )\n",
    "    f.write(c),   f.write('\\n\\n' )\n",
    "    f.close()\n",
    "    print(t1)\n",
    "    print(t3)\n",
    "###############################\n",
    "def input_data():\n",
    "    name=input(\"Enter name: \")\n",
    "    phone=input(\"Eneter number: \")\n",
    "    f=open(\"phonebook.txt\",\"a\")\n",
    "    f.write(name ), f.write(':' ) , f.write(phone)\n",
    "    f.write('\\n' )\n",
    "    f.close()\n",
    "    \n",
    "def show_log():\n",
    "    f = open(\"call_log.txt\",\"r\")\n",
    "    for i in f:\n",
    "        print(i)\n",
    "    f.close()\n",
    "    \n",
    "numbers = {}\n",
    "menu_choice = 0\n",
    "print_menu()\n",
    "while menu_choice != 5:\n",
    "    menu_choice = int(input(\"Type in a number (1-6): \"))\n",
    "    if menu_choice == 1:\n",
    "        print(\"Telephone Numbers:\")\n",
    "        for x in numbers.keys():\n",
    "            print(\"Name: \", x, \"\\tNumber:\", numbers[x])\n",
    "        print()\n",
    "    elif menu_choice == 2:\n",
    "        #print(\"Add Name and Number\")\n",
    "        #name = input(\"Name: \")\n",
    "        #phone = input(\"Number: \")\n",
    "        #numbers[name] = phone\n",
    "        input_data()\n",
    "    elif menu_choice == 3:\n",
    "        name = input('Enter the name : ')\n",
    "        call_to(name)\n",
    "        print_menu()\n",
    "    elif menu_choice == 4:\n",
    "         print(\"showlog\")\n",
    "        show_log()      \n",
    "    elif menu_choice != 5:\n",
    "        print_menu()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
