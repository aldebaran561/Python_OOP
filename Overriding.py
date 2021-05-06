{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Inside Parent\n",
      "Inside Child\n"
     ]
    }
   ],
   "source": [
    "# Defining parent class\n",
    "class Parent():\n",
    "      \n",
    "    # Constructor\n",
    "    def __init__(self):\n",
    "        self.value = \"Inside Parent\"\n",
    "          \n",
    "    # Parent's show method\n",
    "    def show(self):\n",
    "        print(self.value)\n",
    "          \n",
    "# Defining child class\n",
    "class Child(Parent):\n",
    "      \n",
    "    # Constructor\n",
    "    def __init__(self):\n",
    "        self.value = \"Inside Child\"\n",
    "          \n",
    "    # Child's show method\n",
    "    def show(self):\n",
    "        print(self.value)\n",
    "        \n",
    "# Driver's code\n",
    "obj1 = Parent()\n",
    "obj2 = Child()\n",
    "  \n",
    "obj1.show()\n",
    "obj2.show()"
   ]
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
